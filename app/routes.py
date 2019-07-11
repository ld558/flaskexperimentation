#Comprises the different URLS that the application implements
from app import app
from flask import render_template
@app.route('/')
def homepage():
    season_info={'day':0}
    team_stats = [
        {'name':'Clippers','wins': 23},
        {'name':'Lakers','wins':14}
    ]
    return render_template('homepage.html',title='Home', season_info=season_info, team_stats=team_stats)

