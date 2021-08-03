from flask import Flask, Markup, render_template, make_response, request, jsonify


app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder="templates",
    static_folder="static"
    )


@app.route('/home')
def home():
    nav = [
        {'name': 'google', 'url': 'https://google.com/'},
        {'name': 'njit', 'url': 'https://njit.edu'},
        {'name': 'youtube', 'url': 'https://youtube.com/'}
    ]
    return render_template(
        'home.html',
        nav=nav,
        title="Jinja Demo Site",
        description="Smarter page template with Flask & Jinja. this is the description."
    )



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)