from flask import Flask, render_template


# Flask app creation
app = Flask(__name__)

# Ugly and confusing tangent of in-line config stuff
app.config['TESTING'] = True
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = 'development'
app.config['SECRET_KEY'] = 'GDtfDCFYjD'
app.config['DEBUG'] = False  # actually I want debug to be off now


# Actual app logic
@app.route('/5')
def home():
    return render_template('index.html')
