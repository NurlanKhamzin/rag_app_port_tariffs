import openai
from embeddings import get_embeddings
from vector_store import query_faiss_index
import os
from dotenv import load_dotenv
load_dotenv()


# Initialize OpenAI client
openai_api_key = os.environ.get("OPENAI_API_KEY")
client = openai.OpenAI(api_key=openai_api_key)

def rag_query(query, faiss_index, text_chunks, api_key, top_k=3, model="gpt-4o"):
    """
    Perform a Retrieval-Augmented Generation (RAG) query.

    Parameters:
    - query: The user's input query as a string.
    - faiss_index: The FAISS index for similarity search.
    - text_chunks: The list of text chunks corresponding to the embeddings in the FAISS index.
    - api_key: Your OpenAI API key.
    - top_k: Number of relevant text chunks to retrieve.
    - model: The GPT model to use for generating responses (e.g., "gpt-4").

    Returns:
    - A response string generated by the GPT model.
    """
    # Step 1: Generate query embedding
    print("Generating embedding for query...")
    query_embedding = get_embeddings(query, api_key)

    # Step 2: Search FAISS index for relevant text chunks
    print(f"Retrieving top {top_k} relevant chunks from FAISS index...")
    relevant_texts = query_faiss_index(query_embedding, faiss_index, text_chunks, top_k=top_k)

    # Combine the retrieved text chunks into a context string
    context = "\n\n".join(relevant_texts)
    print(f"Retrieved Context:\n{context[:500]}...")  # Preview the context (first 500 characters)

    # Step 3: Generate response using OpenAI's GPT model
    print("Generating response using GPT model...")
    openai.api_key = api_key
    vessel_info = """Vessel Details:
        General
        Vessel Name: SUDESTADA
        Built: 2010
        Flag: MLT - Malta
        Classification Society: Registro Italiano Navale
        Call Sign: [Not provided]
        Main Details
        Lloyds / IMO No.: [Not provided]
        Type: Bulk Carrier
        DWT: 93,274
        GT / NT: 51,300 / 31,192
        LOA (m): 229.2
        Beam (m): 38
        Moulded Depth (m): 20.7
        LBP: 222
        Drafts SW S / W / T (m): 14.9 / 0 / 0
        Suez GT / NT: - / 49,069
        Communication
        E-mail: [Not provided]
        Commercial E-mail: [Not provided]
        DRY
        Number of Holds: 7
        Cargo Details
        Cargo Quantity: 40,000 MT
        Days Alongside: 3.39 days
        Arrival Time: 15 Nov 2024 10:12
        Departure Time: 22 Nov 2024 13:00
        Activity/Operations
        Activity: Exporting Iron Ore
        Number of Operations: 2"""
    ports = ["Durban","Saldanha","Richard's Bay"]
    tariffs = "light dues, port dues, towage dues,vehicle traffic services (VTS) dues, pilotage dues, running of vessel lines dues"
    light_dues = "Light dues are calculated simply by multiplying GT/100 to Per 100 tons or part thereof tariff"
    #port_dues = "No specific instructions"
    towage_dues = "Towage dues are calculated as per TUGS/VESSEL ASSISTANCE tariffs as per port and GT category adding 100% surcharge for additional tug for no own power at the end"
    #vts_dues = "No specific instructions"
    pilot_dues = "As per Pilotage Services tariffs calculate pilotage for entering and leaving per service and per 100 tons or part thereof"
    #vessel_line_dues = "No specific instructions"
    query = (f"Calculate the {tariffs} payable by the following vessel berthing at the port of {ports[0]} for {vessel_info}. "
             #f"Use the following instructions on how to calculate: "
             #f"{light_dues}, {port_dues}, {towage_dues}, {vts_dues}, {pilot_dues}, and {vessel_line_dues}. "
             f"Do not describe how to calculate. Provide the exact amounts in ZAR.")
    response = client.chat.completions.create(model=model,max_tokens=500,
            messages=[
                    {"role": "system", "content": "You are a helpful assistant that helps to calculate port tariffs for South African Ports."},
                    {"role": "user",
                    "content": f"Use the following context to answer the question:\n\n{context}\n\nQuestion: {query}"},
                    {"role": "user",
                    "content": f"You can use the following hints in your calculations - {light_dues}, {pilot_dues}, {towage_dues}"}
    ]
                                              )
    return response.choices[0].message.content.strip()