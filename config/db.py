from helpers import get_env
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class ConfigDB(object) :
    HOST = get_env("DB_HOST")
    DATABASE = get_env("DB_DATABASE")
    USERNAME = get_env("DB_USERNAME")
    PASSWORD = get_env("DB_PASSWORD")

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True