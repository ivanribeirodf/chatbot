from flask import Flask, request, jsonify
from openai_service import chat_with_openai
from llama_service import chat_with_llama
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])

def chat():
    data = request.get_json()
    message = data.get("message", "")
    mode = data.get("mode", "openai")

    if mode == "openai":
        response = chat_with_openai(message)
    else:
        response = chat_with_llama(message)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
