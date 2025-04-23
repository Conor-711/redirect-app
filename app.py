from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("https://www.vibing.today", code=301)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
