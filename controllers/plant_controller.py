from core.app_init import app
from models.plant import Plant
from flask import Flask, render_template, request, redirect, url_for, abort, jsonify
from models.sqlalchemy_init import db
import sys
from flask_cors import cross_origin


@app.route('/plants', methods=['GET','POST'])
# @cross_origin
def get_plants():
    # Implement pagination
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * 10
    end = start + 10

    plants = Plant.query.all()
    formatted_plants = [plant.format() for plant in plants]
    return jsonify({
        'success': True,
        'plants':formatted_plants[start:end],
        'total_plants':len(formatted_plants)
        })


@app.route('/plants/<int:plant_id>')
def get_specific_plant(plant_id):
    plant = Plant.query.filter(Plant.id==plant_id).one_or_none()
    if plant is None:
        abort(404)
    else:
        return jsonify({
            'success': True,
            'plant': plant.format()
        })

