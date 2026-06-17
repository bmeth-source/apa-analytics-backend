from flask import Flask, jsonify

app = Flask(__name__)

players = [
    {"name": "Player 1", "skill_level": 5},
    {"name": "Player 2", "skill_level": 4}
]

@app.route("/")
def home():
    return "APA Analytics Backend Running"

@app.route("/players")
def get_players():
    return jsonify(players)

if __name__ == "__main__":
    app.run()
