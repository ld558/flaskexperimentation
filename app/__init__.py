from flask import Flask
app = Flask(__name__)
# Imported subsequent to prevent circular imports
from app import routes




