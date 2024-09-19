from os import abort

from flask import Blueprint, request, jsonify, abort
from services.players import *
from models.players import Player

players_bp = Blueprint('players', __name__)



# todo, make sure this is ok and finish percentage and list of seasons
@players_bp.route('/players', methods=['GET'])
def get_player_by_season():
    position = request.args.get('position')
    season = request.args.get('season')
    all_players = Player.query.all()
    if not all_players:
        abort(404, description="Players not found")
    if season and position:
        # players = []
        # for player in all_players:
        #     if player.season == season and player.position == position:
        #         player.season = get_seasons(all_players, position)
        #         players.append(player.to_dict())
        #         print('player checked succesfully')
        # return jsonify(players)
        return jsonify([player.to_dict() for player in all_players if player.position == position and player.season == season])
    elif position:
        players = []

        return jsonify([player.to_dict() for player in all_players if player.position == position])
    else:
        return jsonify([player.to_dict() for player in all_players])




