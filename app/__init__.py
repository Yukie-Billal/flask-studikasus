from flask import Flask
from helpers import get_env

app = Flask(__name__)

app.template_folder = get_env('VIEW_FOLDER')

from . import routes