#Comprises the different URLS that the application implements
from app import app

@app.route('/')
@app.route('/index')
def index():
    return("Salutations")