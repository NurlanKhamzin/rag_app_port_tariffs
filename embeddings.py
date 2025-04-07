import openai
import os
from dotenv import load_dotenv
load_dotenv()

# Initialize OpenAI client
openai_api_key = os.environ.get("OPENAI_API_KEY")
client = openai.OpenAI(api_key=openai_api_key)

def get_embeddings(text, api_key):
    """Generate a single embedding for the given input text."""
    response = client.embeddings.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding