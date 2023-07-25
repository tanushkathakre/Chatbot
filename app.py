from flask import Flask, render_template, request, jsonify
import openai

openai.api_key = "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"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input_text = msg
    chat_log = f"You are a helpful assistant.\nUser: {input_text}\n"
    return get_openai_response(chat_log)

def get_openai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
    )

    return response['choices'][0]['text']

if __name__ == '__main__':
    app.run()
