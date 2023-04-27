from flask import (
        abort, Flask, jsonify, redirect, render_template, request, session, url_for
)

app = Flask(__name__)
import os

import os
import subprocess

@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/')
def fortune():
    message = os.system('fortune >temp.txt')
    f = open('temp.txt', 'r')
    output = f.read()
    f.close()
    os.system('rm temp.txt')
    return output

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
    os.system('cowsay | fortune >temp.txt')
    f = open('temp.txt', 'r')
    output = f.read()
    f.close()
    os.system('rm temp.txt')
    return '<pre>' + output + '</pre>'
