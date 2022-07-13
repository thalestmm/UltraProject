from flask import Flask,render_template
from markupsafe import escape
import disciplines as disc

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("base.html")


@app.route("/question/<string:question_id>")
def render_question(question_id):
    pass


@app.route("/register-question")
def register_new_question():
    disciplines = disc.get_all_discipline_names()
    return render_template("register_question.html", disciplines=disciplines)