from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/html')
def html():
    return render_template("html-cheatsheet.html")

@app.route('/css')
def css():
    return render_template("css-cheatsheet.html")

@app.route('/javascript')
def js():
    return render_template("js-cheatsheet.html")

@app.route('/python')
def python_cheat():
    return render_template("python-cheatsheet.html")

@app.route('/tkinter')
def tkinter_cheat():
    return render_template("tkinter-cheatsheet.html")

@app.route('/flask')
def flask_cheat():
    return render_template("flask-cheatsheet.html")

@app.route('/django')
def django_cheat():
    return render_template("django-cheatsheet.html")


if __name__=="__main__":
    app.run(debug=True, port=5000)