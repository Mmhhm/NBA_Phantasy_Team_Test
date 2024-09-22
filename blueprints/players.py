from os import abort
from db import db
from flask import Blueprint, request, jsonify, abort
from services.players import *
from models.players import Player, Team

players_bp = Blueprint('players', __name__)


@players_bp.route('/players', methods=['GET'])
def get_player_by_season():
    position = request.args.get('position')
    season = request.args.get('season')
    all_players = Player.query.all()
    if not all_players:
        abort(404, description="Players not found")
    if season and position:
        return jsonify([player.to_dict() for player in all_players if player.position == position and player.season == season])
    elif position:
        return jsonify([player.to_dict() for player in all_players if player.position == position])
    else:
        return jsonify([player.to_dict() for player in all_players])


@players_bp.route('/teams', methods=['POST'])
def create_team():
    players = get_players(request)
    if not_in_len(request):
        abort (400, description="A team has to contain 5 players")
    if same_position(players):
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
    team_request = get_players(request)
    if not_in_len(team_request):
        abort (400, description="A team has to contain 5 players")
    if same_position(team_request): # make sure this is the name in the request
        return jsonify({"message": "Duplicate positions are not allowed"}), 400
    team.name = request.json['team_name']
    team.players = team_request
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


@players_bp.route('/teams/<int:team_id>', methods=['GET'])
def get_team_by_id(team_id):
    team = Team.query.filter_by(id=team_id).first()
    if not team:
        abort(404, description="Team not found")
    return jsonify(team.to_dict())


@players_bp.route('/teams', methods=['GET'])
def get_teams():
    teams = Team.query.all()
    if not teams:
        abort(404, description="No teams exist")
    return jsonify([team.to_dict() for team in teams])



