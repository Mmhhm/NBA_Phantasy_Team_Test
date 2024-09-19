from os import abort

# from flask import Blueprint, request, jsonify, abort
#
# from db import db
# from services.players import *
# from models.players import Player, Team
#
# teams_bp = Blueprint('teams', __name__)
#
# @teams_bp.route('/teams', methods=['POST'])
# def create_team():
#     players = []
#     ids = request.get_json()['player_ids']
#     for id in ids:
#         players.append(Player.query.filter_by(id=id).first())
#     new_team = Team(name=request.json['team_name'], players=players)
#     db.session.add(new_team)
#     db.session.commit()
#     return jsonify(new_team.to_dict())