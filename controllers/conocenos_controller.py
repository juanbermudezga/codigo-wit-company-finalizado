from flask import render_template, request, redirect, url_for
from src.app import app
from flask_controller import FlaskController

@app.route("/conocenos")
def conocenos():
    return render_template('conocenos.html', title="wit company")