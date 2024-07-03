from langchain import OpenAI

class Generator:
    def __init__(self):
        self.model = OpenAI(model="text-davinci-003")

    def generate(self, context, query):
        # Generate answers based on the context and query
        response = self.model({"context": context, "query": query})
        return response["choices"][0]["text"].strip()
