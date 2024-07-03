from retriever import Retriever
from generator import Generator

class QnAPipeline:
    def __init__(self, data_path):
        self.retriever = Retriever(data_path)
        self.generator = Generator()
        self.retriever.index_data()

    def answer_query(self, query):
        context = self.retriever.retrieve(query)
        answer = self.generator.generate(context, query)
        return answer
