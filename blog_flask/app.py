from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name", "world")
    return render_template("index.html", name = name)

@app.route("/post", methods = ["POST"])
def post():
    return "<h1>Ejemplo post</h1>"