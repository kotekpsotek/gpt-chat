from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from time import sleep
from llm.main import gpt_2_neo

app = Flask(__name__, template_folder="static")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.post("/question")
@cross_origin()
def question():
    # print(request.json)
    question = request.json['question']

    if len(question):
        answer = gpt_2_neo(question) # Fill this field
        
        return jsonify({
            "answer": answer
        }), 200
    else:
        return "", 400

if __name__ == "__main__":
    app.run(port=5454, debug=True)