from flask import Flask
from blueprints.players import players_bp
from db import db

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///NBA_phantasy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


app.register_blueprint(players_bp, teams_bp)

if __name__ == '__main__':
    app.run()
