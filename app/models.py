from app import db


class Balheads(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    predictions = db.relationship('Predictions', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Balhead: {}>'.format(self.username)


class Teams(db.Model):
    id = db.Column(db.String(3), primary_key=True)
    name = db.Column(db.String(64), unique=True)
    predict_id = db.Column(db.Integer, db.ForeignKey('predictions.id'))
    predictions = db.relationship('Estimated wins', backref='team', lazy='dynamic')
    def __repr__(self):
        return '<Team: The {}'.format(self.name)

class Predictions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    predicts = db.Column(db.String(60))
    user_id = db.Column(db.Integer, db.ForeignKey('balheads.id'))
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    def __repr__(self):
        return "<{}'s Predictions>".format(self.user_id)