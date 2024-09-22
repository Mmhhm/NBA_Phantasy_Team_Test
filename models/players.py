from db import db

class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(70), nullable=False)
    team = db.Column(db.String(70), nullable=False)
    position = db.Column(db.String(70), nullable=False)
    games = db.Column(db.Integer, nullable=True)
    goals = db.Column(db.Integer, nullable=True)
    points = db.Column(db.Integer, nullable=True)
    attempts = db.Column(db.Integer, nullable=True) # Check if necessary
    fieldPercent = db.Column(db.Float, nullable=True, default=0.0)
    twoPercent = db.Column(db.Float, nullable=True, default=0.0)
    threePercent = db.Column(db.Float, nullable=True, default=0.0)
    assists = db.Column(db.Integer, nullable=True)
    turnovers = db.Column(db.Integer, nullable=True)
    ATR = db.Column(db.Integer, nullable=True)
    points_per_game = db.Column(db.Float, nullable=True)
    PPG_ratio = db.Column(db.Float, nullable=True)
    season = db.Column(db.String(10), nullable=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=True)



    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'team': self.team,
            'position': self.position,
            'games': self.games,
            'points': self.points,
            'twoPercent': self.twoPercent,
            'threePercent': self.threePercent,
            'ATR': self.ATR,
            'PPG_ratio': self.PPG_ratio,
            'season': self.season,
        }


class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    players = db.relationship('Player', backref='group', lazy='dynamic')

    def to_dict(self):
        return {
            'name': self.name,
            'players': [player.to_dict() for player in self.players]
        }
