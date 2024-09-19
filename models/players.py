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

    # def __repr__(self):
    #     return f'<Player {self.name} {self.email}>'


    def to_dict(self):
        return {
            'id': self.id,
            'player_id': self.player_id,
            'name': self.name,
            'team': self.team,
            'position': self.position,
            'games': self.games,
            'goals': self.goals,
            'points': self.points,
            'attempts': self.attempts,
            'fieldPercent': self.fieldPercent,
            'twoPercent': self.twoPercent,
            'threePercent': self.threePercent,
            'assists': self.assists,
            'turnovers': self.turnovers,
            'ATR': self.ATR,
            'points_per_game': self.points_per_game,
            'PPG_ratio': self.PPG_ratio,
            'season': self.season,
            'team_id': self.team_id
        }
