from flask import Flask, Markup, render_template, make_response, request, jsonify


app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder="templates",
    static_folder="static"
    )


@app.route('/')
def home():
    return "home page"



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)