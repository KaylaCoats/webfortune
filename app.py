from flask import (
        abort, Flask, jsonify, redirect, render_template, request, session, url_for
)

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/')
def fortune():
    return 'fortune'

@app.route('/cowsay/<message>/')
def cowsay(message):
    #return '<pre>' + message + '</pre>'
    return 'cowsay'

@app.route('/cowfortune/')
def cowfortune():
    return 'cowfortune'
