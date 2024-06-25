from flask import Flask,render_template
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Seja bem vindo<h1>"

@app.route("/projects")
def about():
    return render_template("projects.html")


if __name__=="__main__":
    app.run(debug=True)