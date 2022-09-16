import os
import tempfile

SECRET_KEY = 'very very secret'
DEBUG = True
ENV = 'development'

# DATABASE
DBUSER = 'root'
DBPASSWORD = 'password'
DBHOST = 'localhost'
DBNAME = 'pycon_business_card'

SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/{}'.format(
            DBUSER, DBPASSWORD, DBHOST, DBNAME)
SQLALCHEMY_TRACK_MODIFICATIONS = False
