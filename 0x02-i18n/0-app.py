#!/usr/bin/env python3
"""Basic Flask app that renders a template
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Basic page route"""
    return render_template('0-index.html')
