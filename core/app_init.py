from flask import Flask
from flask_cors import CORS
import os

# template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# template_dir = os.path.join(template_dir, 'templates')
template_dir = "../templates"
app = Flask(__name__, template_folder=template_dir)
# CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:abc@localhost:5432/udacity_fullstack'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/udacity_fullstack'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False