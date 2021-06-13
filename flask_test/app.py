#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    app.logger.debug('home()')
    return "Index page! \n"

@app.route('/hello')
def hello():
    app.logger.debug('hello()')
    return 'Hello, World\n'


from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s\n' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d\n' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s\n' % escape(subpath)