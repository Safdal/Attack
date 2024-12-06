from flask import Flask, render_template, request

app = Flask(__name__)

# Hardcoded username and password for testing purposes
USERNAME = "admin"
PASSWORD = "password123"

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == USERNAME and password == PASSWORD:
        return "Login successful! Welcome, admin."
    else:
        return "Login failed. Invalid username or password.", 401

if __name__ == "__main__":
    app.run(debug=True)
