import openai

# Initialize OpenAI client
client = openai.OpenAI(api_key="YOUR_OPENAI_API_KEY")

def get_embeddings(text, api_key):
    """Generate a single embedding for the given input text."""
    response = client.embeddings.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding