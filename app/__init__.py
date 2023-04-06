from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
login = LoginManager(app)
login.login_view = "login"  # name of the login  view function
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Migrate is a wrapper around Alembic


from app import routes, models
