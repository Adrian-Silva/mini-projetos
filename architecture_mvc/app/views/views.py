from flask import render_template
from app import app
from app.models.report import reports

@app.route('/')
def index():
    return render_template('index.html', reports=reports)

