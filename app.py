from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"


@app.route("/")
def home_page():
    """Generate and show form to prompt for words"""
    words = story.prompts
    return render_template("home.html", words=words)


@app.route("/story")
def story_page():
    """Show the story result"""
    text = story.generate(request.args)
    return render_template("story.html", text=text)
