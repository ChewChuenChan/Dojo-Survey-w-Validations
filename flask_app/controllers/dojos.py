from flask_app import app
from flask import render_template, request, redirect,session,flash
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return render_template ("index.html")

@app.route('/dojo/create',methods=["POST"])
def create_dojo():
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    data ={
    "name" :request.form["name"],
    "location" : request.form["location"],
    "language" : request.form["language"],
    "comment" : request.form["comment"]
    }
    Dojo.create(data)
    return redirect('/result')

# Have the '/result' route display the information from the form on a new HTML page
@app.route('/result')
def result():
    return render_template("result.html", show_dojo = Dojo.show_last_survey())