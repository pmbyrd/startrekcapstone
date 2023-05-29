from flask import render_template
from app.main import main


@main.route('/')
def index():
    return render_template('index.html') 

@main.route('/test')
def test():
    return render_template('test.html')