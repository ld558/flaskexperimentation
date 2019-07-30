from app import db


class Balhead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    user_predictions = db.relationship('Predict',backref='author', lazy = 'dynamic')

    def __repr__(self):
        return '<Balhead: {}>'.format(self.username)


class Team(db.Model):
    id = db.Column(db.String(3), primary_key=True, index=True)
    name = db.Column(db.String(64), unique=True)
    team_predictions = db.relationship('Predict', backref='team', lazy = 'dynamic')

    def __repr__(self):
        return '<Team: The {}'.format(self.name)

class Predict(db.Model):
    prediction = db.Column(db.Integer)
    balhead_id = db.Column(db.Integer, db.ForeignKey('balhead.username'))
    team_id = db.Column(db.String(3), db.ForeignKey('team.id'))
    id = db.Column(db.String(70), primary_key=True, index=True)

    def __init__(self,balhead_id,team_id,prediction):
        self.balhead_id = balhead_id
        self.team_id = team_id
        self.prediction = prediction
        self.id = balhead_id + " ; " + team_id

    def __repr__(self):
        return '<Prediction by {}; Team: {} - Wins: {}>'.format(self.balhead_id,self.team_id,self.prediction)
