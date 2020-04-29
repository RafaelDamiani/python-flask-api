from flask import Flask
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///c:/projects/python-flask-api/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False