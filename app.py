from flask import Flask, jsonify, request
import spacy
from transformers import GPT2LMHeadModel, GPT2Tokenizer



model_name = "distilgpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

app = Flask(__name__)

#  This tells Flask that the function following it will handle requests to the homepage (/)
@app.route('/')
def home():
    return "Hi! My name is Sarita, Sara Mirjalili's personal chatbot! I answer questions about her!"


@app.route('/chat', methods = ["POST"])
def chat():
    user_message = request.json.get("message")

    #encode the input and generate a response
    inputs = tokenizer.input(user_message, return_tensors="pt")
    outputs = model.generate(inputs, max_length =150, do_sample=True, top_k=50 )

    #decode the output and generate the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)