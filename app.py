# -*- coding: utf-8 -*-
"""
    jQuery Example
    ~~~~~~~~~~~~~~

    A simple application that shows how Flask and jQuery get along.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from flask import Flask, jsonify, render_template, request, Response
app = Flask(__name__)
import words
import json


@app.route('/_add_numbers')
def add_numbers():
    """Add two numbers server side, ridiculous but well..."""
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/get_num_stopwords')
def get_num_stopwords():
    """Get number of stop words"""
    print request.args
    words = request.args.getlist('wordsArray', [], type=int)
    # found_stopwords = [word for word in words if word in words.stopwords]
    # resp = Response(response=words,
    #                 status=200, 
    #                 mimetype="application/json")
    # return(resp)
    # return Response(json.dumps(words), mimetype='application/json')
    return jsonify(result=words)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()


