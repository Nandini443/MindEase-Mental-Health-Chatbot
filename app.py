from flask import Flask, render_template, request, session
from chatbot import get_response
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route("/", methods=["GET", "POST"])
def home():
    if "chat" not in session:
        session["chat"] = []

    if request.method == "POST":
        user_message = request.form.get("message")

        if user_message:
            bot_reply = get_response(user_message)

            session["chat"].append({
                "user": user_message,
                "bot": bot_reply
            })

    return render_template("index.html", chat=session["chat"])

if __name__ == "__main__":
    app.run(debug=True)
