from core.app_init import app
from flask import Flask, render_template, request, redirect, url_for, abort, jsonify
from models.sqlalchemy_init import db
import sys
from flask_cors import cross_origin

# CORS Headers
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,PATCH,POST,DELETE,OPTIONS')
    return response


# @app.errorhandler(404)
# def not_found(error):
#     return jsonify({
#         "success": False,
#         "error": 404,
#         "message": "Not found"
#         }), 404


@app.route('/messages/<int:msg_id>', methods=['GET', 'POST'])
@cross_origin()
def get_messages(msg_id):
    # OPTIONS requests are automatically implemented and HEAD is also automatically implemented if GET is present.
    if request.method == 'POST':
        pass
    else:
        return 'GETTING MESSAGES %d' % msg_id

#@cross_origin
@app.route('/hello')
def hello_world():
    return jsonify({'message':'HELLO, WORLD!'})