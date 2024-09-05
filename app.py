from flask import Flask, jsonify, request
import spacy



nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)

#  This tells Flask that the function following it will handle requests to the homepage (/)
@app.route('/')
def home():
    return "Hi! My name is Sarita, Sara Mirjalili's personal chatbot! I answer questions about her!"


@app.route('/chat', methods = ["POST"])
def chat():
    user_message = request.json.get("message")

    # simple chatbot logic
    if "resume" in user_message.lower():
        response = "You can view my resume at [resume link]"
    
    if "background" in user_message.lower():
        response = "I have a background in Data Science in Cmputational Linguistics."

    if "interests" in user_message.lower():
        response = "I'm interested in Data Science and Computer-Human interaction."
    
    else:
        response = "I'm still learning to respond to that. You can ask this directly from Sara by her email: Saramirjalili.78@gmail.com"

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)