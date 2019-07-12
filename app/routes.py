#Comprises the different URLS that the application implements
from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm


@app.route('/')
def homepage():
    season_info={'day':0}
    team_stats = [
        {'name':'Clippers','wins': 23},
        {'name':'Lakers','wins':14}
    ]
    return render_template('homepage.html',title='Home', season_info=season_info, team_stats=team_stats)


@app.route('/login')
def login():
    form = LoginForm()
    # Provided provision of valid input.
    if form.validate_on_submit():
        # Momentarily present string information to the user
        flash('Login requested for user {}, remember_me={}'.format(form.username.data,form.remember_me.data))
        return redirect('/')
    return render_template('login.html',title='Sign In', form=form)