from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import os
from server.config import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/late_show_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.urandom(24).hex()  # Secure random key

migrate = Migrate(app, db)
jwt = JWTManager(app)