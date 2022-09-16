import os

from flask import (
    Flask,
    Response,
    current_app,
    g,
    jsonify,
    request,
)

# praetorian
import flask_cors
import flask_praetorian

# sqlaclhemy
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# marshmallow
from flask_marshmallow import Marshmallow

# Hack for Ubuntu Mysql
import pymysql

pymysql.install_as_MySQLdb()

from decimal import Decimal

# Import models
from src.models import db

from werkzeug.exceptions import HTTPException

# import views
from src.views import hello 

# login failed handler, from:
# https://computableverse.com/blog/flask-admin-using-basicauth
# 登录失败控制器，来源：
# https://computableverse.com/blog/flask-admin-using-basicauth
class AuthException(HTTPException):
    def __init__(self, message):
        # python 2
        # super(AuthException, self).__init__(message, Response(
        #     message, 401,
        #     {'WWW-Authenticate': 'Basic realm="Login Required"'}
        # ))
        # # python 3
        super().__init__(
            message,
            Response(
                message, 401, {"WWW-Authenticate": 'Basic realm="Login Required"'}
            ),
        )

#praetorian
guard = flask_praetorian.Praetorian()

#CORS
cors = flask_cors.CORS()

#marshmallow
marsh = Marshmallow()

def create_app(test_config=None, run_test=False):
    """Construct the core application."""

    # Load our configs
    app = Flask(__name__, instance_relative_config=True)

    # dynamically change configuration
    if os.environ.get('FLASK_ENV') == 'production':
        app.config.from_object('config.ProductionConfiguration')

    elif os.environ.get('FLASK_ENV') == 'staging':
        app.config.from_object('config.StagingConfiguration')

    app.config.from_pyfile('config.py')  # instance

    # Register BluePrints
    app.register_blueprint(hello.bp)

    return app
