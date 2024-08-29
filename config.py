import os

DEBUG=True
APP_NAME="Twitter"
BASEDIR=os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI="sqlite:///"+os.path.join(BASEDIR,"twitter_database.sqlite")
SQLALCHEMY_TRACK_MODIFICATIONS=False
SECRET_KEY="MyAppIsUnaccessible"
LOGIN_DISABLED=False