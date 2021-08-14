from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import os
from flask.app import Flask
from flask import Blueprint
from flask_restplus import Api
from .api import api as user_ns

basedir = os.path.abspath(os.path.dirname(__file__))

blueprint = Blueprint("api", __name__)
# authorizations = {
#     "Authorization": {"type": "apiKey", "in": "header", "name": "Authorization"}
# }

api = Api(
    blueprint,
)

api.add_namespace(user_ns, path="/go")



def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    CORS(app)
 


    return app