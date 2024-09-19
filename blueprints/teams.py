from os import abort

from flask import Blueprint, request, jsonify, abort
from services.players import *
from models.players import Player

teams_bp = Blueprint('teams', __name__)

@teams_bp.route('/teams', methods=['POST'])
def create_team():
    players = []
    ids = request.get_json()['player_ids']
    for id in ids:
        players.append(Player.query.filter_by(id=id).first())