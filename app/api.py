from flask import Flask, request, jsonify
from pipeline import QnAPipeline

app = Flask(__name__)
pipeline = QnAPipeline(data_path="/mnt/data/simple_qna_pipeline/data/sample_contracts/data/")

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    query = data.get('query')
    if not query:
        return jsonify({"error": "Query not provided"}), 400

    answer = pipeline.answer_query(query)
    return jsonify({"query": query, "answer": answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
