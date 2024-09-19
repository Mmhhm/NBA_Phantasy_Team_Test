from flask import session

from models.players import Player

# Calculations
def calc_points_per_game(player: dict):
    return player['points'] / player['games']


def calc_ATR(player: dict):
    if player['assists'] != 0 & player['turnovers'] != 0:
        return player['assists'] / player['turnovers']
    return 0


def calc_avg_points_per_position(players: list, position):
    players_count = 0
    points_count = 0
    for player in players:
        if player['position'] == position:
            points_count += calc_points_per_game(player)
            players_count += 1
    return points_count / players_count


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



#
# def get_players_by_season(players: list):
#
#
#
#
#
#
def get_seasons(players, position):
    seasons = []
    for player in players:
        if player.position == position and player.season not in seasons:
            seasons.append(player.season)
            if len(seasons) == 3:
                continue
    return seasons




