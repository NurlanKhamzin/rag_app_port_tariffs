               RAG Pipeline Application
# Retrieval-Augmented Generation (RAG) Pipeline Application

This README file provides a step-by-step guide to set up, install dependencies, and use the Retrieval-Augmented Generation (RAG) Pipeline Application. Follow the instructions below to get started.

## Project Structure

The application consists of several modular components:

rag_app/
├── pdf_utils.py          # PDF extraction functions
├── token_utils.py        # Functions for text chunking
├── embeddings.py         # Functions for embedding generation
├── vector_store.py       # FAISS vector store functions
├── rag_query.py          # RAG query logic
├── main.py               # Entry point for the pipeline
├── pdfs/                 # Folder for storing PDF files
├── requirements.txt      # Project dependencies


## Prerequisites

Make sure you have the following installed:

* **Python 3.8** or higher
* `pip` (Python's package manager)

## Setup Instructions

1.  **Clone the Repository**

    Clone the project repository to your local system:

    ```bash
    git clone <repository_url>
    cd rag_app
    ```

2.  **Install Dependencies**

    Install the required Python libraries listed in `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

    This will install:

    * `openai`: for embedding and GPT queries.
    * `PyPDF2`: for extracting text from PDF files.
    * `faiss-cpu`: for FAISS vector store integration.

## How to Use the Application

1.  **Prepare Input Files**

    Place your PDF files in the `pdfs/` folder. Ensure the file names are correct, as you'll need to reference them later (e.g., `pdfs/port_tariff.pdf`).

2.  **Run the Application**

    Execute the pipeline by running the `main.py` script:

    ```bash
    python main.py
    ```

3.  **Expected Workflow**

    The script will perform the following steps sequentially:

    * **Extract text from the PDF:**
        Reads the PDF file and extracts its textual content.

    * **Chunk the text:**
        Splits the extracted text into smaller, tokenized chunks based on size limits.

    * **Generate embeddings:**
        Creates embeddings for each text chunk using OpenAI's `text-embedding-ada-002` model.

    * **Create FAISS index:**
        Builds a FAISS vector store from the generated embeddings.

    * **Perform RAG Query:**
        Retrieves relevant text chunks based on the input query and generates a response using OpenAI's GPT model.

4.  **Customizing Queries**

    To perform a RAG query:

    Modify the `query` variable in `main.py` to include your own question. Example:

    ```python
    query = "What are the tariffs for port services?"
    ```

## Detailed Steps for Integration

### A. Import Modular Components

Each Python file serves a specific role:

* `pdf_utils.py`: Extracts text from PDF files.
* `token_utils.py`: Breaks text into smaller chunks for embeddings.
* `embeddings.py`: Generates embeddings from text chunks.
* `vector_store.py`: Creates and queries the FAISS index.
* `rag_query.py`: Handles the RAG query workflow.

These files are imported into `main.py` for seamless orchestration.

### B. Modify the Pipeline

You can modify individual components to adapt the workflow. For example:

* Adjust `max_tokens` in `token_utils.py` to alter chunk sizes.
* Update the OpenAI model used for embeddings or GPT responses in `embeddings.py` and `rag_query.py`.

## Example Output

When you run the application, you’ll see logs for each step, e.g.:

Step 1: Extracting text from PDF...
Extracted Text (First 500 characters): ...

Step 2: Chunking the extracted text...
Number of Chunks Created: 5

Step 3: Generating embeddings for each chunk...
Embeddings generated successfully.

Step 4: Creating FAISS index...
FAISS index created successfully.

Step 5: Performing RAG query...
RAG Response:
"The port tariffs include charges for light dues, port dues, towage dues, etc."


## Troubleshooting

### Common Issues

* **"File not found" error:** Ensure the file path for the PDF is correct and the file exists in the `pdfs/` folder.
* **OpenAI API errors:** Double-check your OpenAI API key in `main.py` and ensure your account has access to the required models.
* **Empty FAISS results:** Verify that your query is relevant to the text in the PDF, and adjust the `top_k` parameter to retrieve more chunks.

You're all set! If you have questions or need assistance, feel free to reach out. Happy querying! 🚀