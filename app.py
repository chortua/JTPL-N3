from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    choice = request.form.get("choices")
    if request.method == 'POST':
        print(choice)
        return render_template("index.html")
    else:
        print(choice)
        return render_template("index.html")
if __name__ == '__main__':
    app.run(debug=True)
