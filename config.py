import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'salutaions'
    # Specifies where to create the database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir,'app.db')
    # prevents the database from notifying the app at each alteratoin
    SQLALCHEMY_TRACK_MODIFICATIONS = False