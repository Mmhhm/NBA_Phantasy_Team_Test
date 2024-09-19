# from ..db import db
#
# class Team(db.Model):
#     __tablename__ = 'teams'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=True, nullable=False)
#     players = db.relationship('Player', backref='group', lazy='dynamic')
#
#     def to_dict(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'players': [player.to_dict() for player in self.players]
#         }
