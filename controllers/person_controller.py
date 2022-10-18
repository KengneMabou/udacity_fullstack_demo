from core.app_init import app
from models.person import Person
from flask import Flask, render_template, request, redirect, url_for, abort, jsonify
from models.sqlalchemy_init import db
import sys
from flask_cors import cross_origin


@app.route('/persons/create', methods=['POST'])
def create_person():
   body={}
   error = False
   try:
       name =  request.get_json()['name']
       age = request.get_json()['age']
       person = Person(name=name,age=age)
       body['name'] = person.name
       db.session.add(person)
       db.session.commit()
   except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
   finally:
        db.session.close()
        if  error == True:
            abort(400)
        else:
            return jsonify(body)


@app.route('/')
def index():
    return render_template('index.html', data=Person.query.all())

