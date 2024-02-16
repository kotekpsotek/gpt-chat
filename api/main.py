from flask import Flask, jsonify, request
from time import sleep
from .llm.main import gpt_2_neo

app = Flask(__name__, template_folder="static")

@app.post("/question")
def question():
    question = request.json

    if len(question):
        answer = gpt_2_neo(question) # Fill this field
        
        return jsonify({
            "answer": answer
        }), 200
    else:
        return 400

if __name__ == "__main__":
    app.run(port=5454, debug=True)