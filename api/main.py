from flask import Flask, jsonify, request

app = Flask(__name__, template_folder="static")

@app.post("/question")
def question():
    question = request.json

    if len(question):
        answer = "" # Fill this field

        # TODO: Here should be AI Generative LLM model processing output
        
        return jsonify({
            answer
        }), 200
    else:
        return 400

if __name__ == "__main__":
    app.run(port=5454, debug=True)