from flask import (
        abort, Flask, jsonify, redirect, render_template, request, session, url_for
)

app = Flask(__name__)
import os

@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/')
def fortune():
    message = os.system('fortune')
    return message

@app.route('/cowsay/<message>/')
def cowsay(message):
    return '<pre>' + message + '</pre>'

@app.route('/cowfortune/')
def cowfortune():
    return 'cowfortune'
