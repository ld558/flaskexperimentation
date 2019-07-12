from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Imported subsequent to prevent circular imports
from app import routes




