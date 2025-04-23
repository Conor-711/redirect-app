from flask import Flask, redirect
import os

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("https://www.vibing.today", code=301)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Railway环境兼容
    app.run(host="0.0.0.0", port=port)
