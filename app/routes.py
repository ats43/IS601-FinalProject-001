from flask import current_app as app
from flask import render_template


@app.route("/home.html")
def home():
    return render_template(
        'home.html',
        title="Jinja Demo Site",
        description="Smarter page template with Flask & Jinja. this is the description."
    )
