from flask import Flask, render_template

app = Flask(__name__)


@app.route("/4")
@app.route("/home4")
def home4():
    return "Hello World"


@app.route("/user/<username>", methods=["GET", "POST", "PUT"])
def profile(username):
    return "This is the username page"


@app.route("/index4")
def index4():
    return render_template("index4.html",
                           title="INDEX PAGE",
                           body="This is the body")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
