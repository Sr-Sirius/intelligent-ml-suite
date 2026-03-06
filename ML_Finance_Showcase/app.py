# Import Flask and the function used to render HTML templates
from flask import Flask, render_template

# Create the Flask application instance
app = Flask(__name__)

# Main route of the website
# When the user visits "/", Flask loads the home.html page
@app.route('/')
def home():
    return render_template("home.html")

# Second route that loads the main project page
# This page contains the expense classifier interface
@app.route('/FirstPage')
def first_page():
    return render_template("index.html")

# Starts the Flask development server
# debug=True allows automatic reload when code changes
if __name__ == "__main__":
    app.run(debug=True)