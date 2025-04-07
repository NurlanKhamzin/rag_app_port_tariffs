from pdf_utils import extract_text_from_pdf
from token_utils import split_text_into_chunks
from embeddings import get_embeddings
from vector_store import create_faiss_index
from rag import rag_query

def main():
    # Define your OpenAI API key
    api_key = "YOUR_OPENAI_API_KEY"  # Replace with your actual API key

    # Path to your PDF file
    pdf_path = "pdfs/port_tariff.pdf"  # Replace with your actual file path

    # Step 1: Extract text from the PDF
    print("Step 1: Extracting text from PDF...")
    extracted_text = extract_text_from_pdf(pdf_path)
    print("Extracted Text (First 500 characters):")
    print(extracted_text[:500])  # Preview the first 500 characters

    # Step 2: Chunk the extracted text
    print("\nStep 2: Chunking the extracted text...")
    text_chunks = split_text_into_chunks(extracted_text, max_tokens=4500)
    print(f"Number of Chunks Created: {len(text_chunks)}")

    # Step 3: Generate embeddings for each chunk
    print("\nStep 3: Generating embeddings for each chunk...")
    embeddings = [get_embeddings(chunk, api_key) for chunk in text_chunks]
    print("Embeddings generated successfully.")

    # Step 4: Create FAISS index
    print("\nStep 4: Creating FAISS index...")
    faiss_index = create_faiss_index(embeddings)
    print("FAISS index created successfully.")

    # Step 5: Handle RAG query
    print("\nStep 6: Performing RAG query...")
    query = "What are the tariffs for port services?"
    response = rag_query(query, faiss_index, text_chunks, api_key, top_k=1, model="gpt-4")
    print("\nRAG Response:")
    print(response)

if __name__ == "__main__":
    main()
