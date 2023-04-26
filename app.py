from flask import (
        abort, Flask, jsonify, redirect, render_template, request, session, url_for
)

app = Flask(__name__)

import os
import subprocess

@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/')
def fortune():
    message = 'fortune'
    #message = os.system('fortune')
    return 'fortune'

@app.route('/cowsay/<message>/')
def cowsay(message):
    os.system('cowsay ' + message + ' >temp.txt')
    f = open('temp.txt', 'r')
    output = f.read()
    f.close()
    os.system('rm temp.txt')
    return '<pre>' + output + '</pre>'

@app.route('/cowfortune/')
def cowfortune():
    return 'cowfortune'
