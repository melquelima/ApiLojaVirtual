from flask import Flask
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
cors = CORS(app)
app.config.from_object('config')
ma = Marshmallow(app)
db = SQLAlchemy(app)

from app.controllers import default, token, user, product,order



