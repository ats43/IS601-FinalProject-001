from flask import Flask, render_template, make_response, redirect, url_for

app = Flask(__name__)


@app.route("/4")
@app.route("/home4")
def home4():
    return "HomePage: Hello World"


@app.route("/user/<username>", methods=["GET", "POST", "PUT"])
def profile(username):
    return "This is the username page"


@app.route("/index4")
def index4():
    return render_template("index4.html",
                           title="INDEX PAGE",
                           body="This is the body")


@app.route("/api/v2/test_response")
def users4():
    headers = {"Content-Type": "application/json"}
    return make_response('Test Worked', 200)


@app.route("/landing")
def landing():
    return redirect((url_for('home4')))




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
