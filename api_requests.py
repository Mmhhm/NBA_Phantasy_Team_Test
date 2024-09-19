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
print('hi')
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


print('hello')

def create_player(players: list):
    season = iter_season()
    with app.app_context():
        for data in players:
            # try:
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
                season=2022,
                points_per_game=calc_points_per_game(data),
                ATR=calc_ATR(data),
                PPG_ratio=PPG_ratio(data, avg_per_position_2022)

            )
            print('created new player', new_player)
            db.session.add(new_player)
            print('added player successfully')
        db.session.commit()

        print('finished adding player successfully')

create_player(season_2022)
    # return new_player.to_dict()
    # except Exception as e:
    #     db.session.rollback()
    #     return {"error": str(e)}





#
# 'id': self.id,
# 'player_id': self.player_id,
# 'name': self.task,
# 'team': self.due_date,
# 'position': self.position,
# 'games': self.games,
# 'goals': self.goals,
# 'points': self.points,
# 'attempts': self.attempts,
# 'fieldPercent': self.fieldPercent,
# 'twoPercent': self.twoPercent,
# 'threePercent': self.threePercent,
# 'assists': self.assists,
# 'turnovers': self.turnovers,
# 'ATR': self.ATR,
# 'points_per_game': self.points_per_game,
# 'PPG_ratio': self.PPG_ratio,