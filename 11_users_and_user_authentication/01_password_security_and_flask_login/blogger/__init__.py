from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = 'hello_world'
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


login_manager = LoginManager()
login_manager.login_view = "signin"

bootstrap = Bootstrap()

login_manager.init_app(app)
bootstrap.init_app(app)

from blogger import models
from blogger import views

