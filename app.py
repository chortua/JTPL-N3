from flask import Flask, render_template,request
import sqlite3
import db
import os

currentdirectory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # Variables return from index.html
    rowid = request.form.get('rowid')
    answer = request.form.get('answer')
    choice = request.form.get("choices")
    # Methods post, request from index.html
    if request.method == 'POST':
        if choice == answer:
            questions = db.jlpt_data()
            text = "Right, Answer was {}".format(answer)
            color = "#C0D8C0"
            return render_template("index.html", questions=questions, text=text, color=color)
        else:
            questions = db.jlpt_data()
            text = "Wrong,Answer was {}".format(answer)
            color = "#F05454"
            return render_template("index.html", questions=questions, text=text, color=color)



    # if page is not requested,then it submits this.
    else:
        questions = db.jlpt_data()
        color = "white"
        return render_template("index.html", questions=questions, color=color)

if __name__ == '__main__':
    app.run(debug=True)
