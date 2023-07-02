from flask import Flask
from helpers import get_env
from config.db import ConfigDB

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(ConfigDB)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.template_folder = get_env('VIEW_FOLDER')

from .models import user
from . import routes