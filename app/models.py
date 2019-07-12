from app import db


class Balhead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<Balhead: {}>'.format(self.username)


class Teams(db.Model):
    abbreviation = db.Column(db.String(3), primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Team: The {}'.format(self.name)