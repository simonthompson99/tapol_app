from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# create the Flask app, database and db migration instances
app = Flask(__name__,
  template_folder='templates'
  )
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# apply the SECRET_KEY variable from the config class
app.config.from_object(Config)

from app import routes, models