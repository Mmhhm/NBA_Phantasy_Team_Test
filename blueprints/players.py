from os import abort
from db import db
from flask import Blueprint, request, jsonify, abort
from services.players import *
from models.players import Player, Team

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



@players_bp.route('/teams', methods=['POST'])
def create_team():
    players = get_players(request)

    # players = [Player.query.filter_by(id=id).first() for id in request.get_json()['player_ids']]

    # ids = request.get_json()['player_ids']
    # players = []
    # for id in ids:
    #     players.append(Player.query.filter_by(id=id).first())
    if not_in_len(request):
    # if len(request.json['player_ids']) != 5:
        abort (400, description="Bad request")
    if same_position(players):
    # if len({players[0].position, players[1].position, players[2].position, players[3].position, players[4].position}) != 5:
        return jsonify({"message": "Duplicate positions are not allowed"}), 400
    new_team = Team(name=request.json['team_name'], players=players)
    db.session.add(new_team)
    db.session.commit()
    return jsonify(new_team.to_dict())

@players_bp.route('/teams/<int:team_id>', methods=['PUT'])
def update_team(team_id):
    team = Team.query.filter_by(id=team_id).first()
    if not team:
        abort(404, description="Team not found")
    team_request = request.json()
    if not_in_len(team_request):
    # if len(request.json['player_ids']) != 5:
        abort (400, description="Bad request")
    if same_position(team_request['players']): # make sure this is the name in the request
        return jsonify({"message": "Duplicate positions are not allowed"}), 400
    team.name = team_request['name']
    team.players = team_request['players']
    db.session.commit()
    return jsonify({'message': 'Team updated successfully'}), 200

@players_bp.route('/teams/<int:team_id>', methods=['DELETE'])
def delete_team(team_id):
    team = Team.query.filter_by(id=team_id).first()
    if not team:
        abort(404, description="Team not found")
    db.session.delete(team)
    db.session.commit()
    return jsonify({"message": "Team deleted successfully"}), 200




