from flask import request, abort

from models.players import Player

# Calculations
# Points per game for player
def calc_points_per_game(player: dict):
    return player['points'] / player['games']


# ATR for player
def calc_ATR(player: dict):
    if player['assists'] != 0 & player['turnovers'] != 0:
        return player['assists'] / player['turnovers']
    return 0


# average points per position
def calc_avg_points_per_position(players: list, position):
    players_count = 0
    points_count = 0
    for player in players:
        if player['position'] == position:
            points_count += calc_points_per_game(player)
            players_count += 1
    return points_count / players_count


# average points per position for all players
def dict_avg_per_position(players: list, positions: list):
    avg_per_positions = {}
    for p in positions:
        result = calc_avg_points_per_position(players, p)
        avg_per_positions[p] = result
    return avg_per_positions


def PPG_ratio(player, positions_avg):
    player_avg = calc_points_per_game(player)
    for position in positions_avg:
        if player['position'] == position:
            return player_avg / positions_avg[position]


# Get all seasons of player
def get_seasons(players, position):
    seasons = []
    for player in players:
        if player.position == position and player.season not in seasons:
            seasons.append(player.season)
            if len(seasons) == 3:
                continue
    return seasons


# Get requested player from db
def get_players(team_request):
    return [Player.query.filter_by(id=player_id).first() for player_id in team_request.get_json()['player_ids']]


# Check for 5 players in request
def not_in_len(team_request):
    return len(request.json['player_ids']) != 5


# Chck for different positions in request
def same_position(players):
    return len({players[0].position, players[1].position, players[2].position, players[3].position, players[4].position}) != 5



