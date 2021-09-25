from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
#setting the secret key protects the forms against certain attacks
app.config['SECRET_KEY'] = 'f7ef3218fb22dc9f50adf7766404a646' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'#relative path the 3 forward slashes
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes