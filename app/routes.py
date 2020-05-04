from app import app
from flask import render_template, request

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/keyboards')
def keyboards():
    return render_template('keyboards.html')