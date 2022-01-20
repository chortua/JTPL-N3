from flask import Flask, render_template,request
import sqlite3
import db
import os

currentdirectory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    choice = request.form.get("choices")
    if request.method == 'POST':
        print(choice)
        return render_template("index.html")
    else:
        questions = db.jlpt_data()
        print(choice)
        return render_template("index.html", questions=questions)

if __name__ == '__main__':
    app.run(debug=True)
