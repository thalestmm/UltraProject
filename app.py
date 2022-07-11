from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return r"<p>Working</p>"


@app.route("/question/<string:question_id>")
def render_question(question_id):
    pass
