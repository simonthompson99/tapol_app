from flask import Flask
from config import Config

# create the Flask app
app = Flask(__name__,
  template_folder='templates'
  )

# apply the SECRET_KEY variable from the config class
app.config.from_object(Config)

from app import routes