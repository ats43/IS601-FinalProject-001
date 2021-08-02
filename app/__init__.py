from flask import Flask, render_template, url_for, redirect, flash
from forms import ContactForm, SignupForm


app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder="templates",
    static_folder="static"
)

app.config['SECRET_KEY']="1q2w3e4r5t6y7u8i9o0p"


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


@app.route('/contact', methods=['GET', 'POST'])
def contactinit():
    """Standard 'contact' form """
    form = ContactForm()
    if form.validate_on_submit():
        flash(f'Account Created!', 'success')
        return redirect(url_for("home"))
    return render_template("contact.jinja2", form=form, template="form-template")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Standard 'contact' form """
    form = SignupForm()
    if form.validate_on_submit():
        return redirect(url_for("home"))
    return render_template("contact.jinja2", form=form, template="form-template")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
