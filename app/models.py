from app import db


class Balhead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    user_predictions = db.relationship('Predict',backref='author', lazy = 'dynamic')

    def __repr__(self):
        return '<Balhead: {}>'.format(self.username)


class Team(db.Model):
    id = db.Column(db.String(3), primary_key=True)
    name = db.Column(db.String(64), unique=True)
    team_predictions = db.relationship('Predict', backref='team', lazy = 'dynamic')

    def __repr__(self):
        return '<Team: The {}'.format(self.name)

class Predict(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prediction = db.Column(db.Integer)
    balhead_id = db.Column(db.Integer, db.ForeignKey('balhead.id'))
    team_id = db.Column(db.String(3), db.ForeignKey('team.id'))

    def __repr(self):
        return '<Prediction by UserId: {}, Team: {} ; Wins: {}>'.format(self.balhead_id,self.team_id,self.prediction)
