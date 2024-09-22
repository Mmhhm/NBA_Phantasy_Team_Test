import requests, json
from models.players import Player
from db import db
from services.players import *
from app import app

# Paths
players_2024_season = 'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2024&&pageSize=1000'
players_2023_season = 'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2023&&pageSize=1000'
players_2022_season = 'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2022&&pageSize=1000'

# simple api request
def requet_to_json(url):
    request = requests.get(url).json()
    return request

season_2022 = requet_to_json(players_2022_season)
season_2023 = requet_to_json(players_2023_season)
season_2024 = requet_to_json(players_2024_season)

positions = ['PG', 'SG', 'SF', 'PF', 'C']

avg_per_position_2022 = dict_avg_per_position(season_2022, positions)
avg_per_position_2023 = dict_avg_per_position(season_2023, positions)
avg_per_position_2024 = dict_avg_per_position(season_2024, positions)

def iter_season():
    seasons = [2022, 2023, 2024]
    iterate = iter(seasons)
    return next(iterate)


def create_player(players: list):
    season = iter_season()
    with app.app_context():
        for data in players:
            new_player = Player(
                player_id=data["id"],
                name=data["playerName"],
                team=data["team"],
                position=data["position"],
                games=data["games"],
                goals=data["fieldGoals"],
                points=data["points"],
                attempts=data["fieldAttempts"],
                fieldPercent=data["fieldPercent"],
                twoPercent=data["twoPercent"],
                threePercent=data["threePercent"],
                assists=data["assists"],
                turnovers=data["turnovers"],
                season=2024,
                points_per_game=calc_points_per_game(data),
                ATR=calc_ATR(data),
                PPG_ratio=PPG_ratio(data, avg_per_position_2022)
            )
            print('created new player', new_player)
            db.session.add(new_player)
            print('added player successfully')
        db.session.commit()
        print('finished adding players successfully')

create_player(season_2024)
