#!/usr/bin/env python3

from flask import Flask, render_template
import numpy
import pandas

app = Flask(__name__)

@app.route('/', methods=['GET'])

def index_page_landing():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()