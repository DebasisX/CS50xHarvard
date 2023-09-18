from flask import Flask, flash, redirect, render_template, request, session
app = Flask(__name__)

@app.route("/")
def index():
    if request.method == "GET":
        return render_template("index.html")
