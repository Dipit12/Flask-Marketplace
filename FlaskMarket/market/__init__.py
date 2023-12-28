from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///market.db"
app.config['SECRET_KEY'] = "1275e186f427443a6ceb5c75"
print(app)

db = SQLAlchemy(app)

#db.init_app(app)




bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from market.models import create_tables

from market import route

with app.app_context():
    create_tables()
