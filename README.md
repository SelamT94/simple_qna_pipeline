# Simple Q&A Pipeline with RAG using LangChain

This project demonstrates how to build a simple Q&A pipeline using Retrieval-Augmented Generation (RAG) with LangChain.

## Directory Structure
- `data/`: Contains the sample contracts data.
- `src/`: Source code for the retriever, generator, pipeline, and API.
- `tests/`: Unit tests for the components.
- `notebooks/`: Jupyter notebook for running experiments.
- `requirements.txt`: Dependencies for the project.
- `README.md`: Project documentation.

## Setup
1. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the Flask API:
    ```bash
    python src/api.py
    ```

## Usage
- Send a POST request to the `/query` endpoint with a JSON body containing the query.

## Example
```bash
curl -X POST http://localhost:5000/query -H "Content-Type: application/json" -d '{"query": "What is the term of the contract?"}'
