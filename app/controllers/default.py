from app import app
from flask import send_from_directory,render_template,redirect,url_for,request,session

@app.route("/")
def index():
    return render_template("index.html")


