from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from core import app
db = SQLAlchemy(app)
migrate = Migrate(app, db)