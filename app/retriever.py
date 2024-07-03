from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
import os

class Retriever:
    def __init__(self, data_path):
        self.data_path = data_path
        self.embeddings = OpenAIEmbeddings()
        self.vector_store = Chroma(embedding_function=self.embeddings)

    def index_data(self):
        # Load and index the contracts data from multiple files
        for root, _, files in os.walk(self.data_path):
            for file in files:
                file_path = os.path.join(root, file)
                self.vector_store.index_data(file_path)

    def retrieve(self, query):
        # Retrieve relevant documents based on the query
        return self.vector_store.search(query)
