from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Revisar como hacer las configuraciones (archivo)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Initialize Database
db = SQLAlchemy(app)

# Import Routes
from src.routes import masters_routes
from src.routes import global_routes

