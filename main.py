from flask import Flask, jsonify

app = Flask(__name__)

players = [
{"team":"Team Bud","name":"Wayne Amerson","skill_level":6},{"team":"Team Bud","name":"Bill Methvin","skill_level":5},{"team":"Team Bud","name":"Jerry Barron","skill_level":4},{"team":"Team Bud","name":"Julie Barron","skill_level":2},{"team":"Team Bud","name":"Steven Asbell","skill_level":4},{"team":"Team Bud","name":"Rodney Amerson Sr","skill_level":4},{"team":"Team Bud","name":"Jeff Powell","skill_level":6},{"team":"Team Bud","name":"Josh Amerson","skill_level":4},

{"team":"Underdawgs","name":"Joey Ellis","skill_level":4},{"team":"Underdawgs","name":"Stephanie Lindsey","skill_level":3},{"team":"Underdawgs","name":"Wayne Johnson","skill_level":5},{"team":"Underdawgs","name":"Chase Lindsey","skill_level":2},{"team":"Underdawgs","name":"Dustin Stapleton","skill_level":7},{"team":"Underdawgs","name":"Little T Durden","skill_level":6},{"team":"Underdawgs","name":"Boss Hogg McCune","skill_level":2},{"team":"Underdawgs","name":"Candy Skinner","skill_level":3},

{"team":"Shape is Overrated","name":"Curt Mayo III","skill_level":6},{"team":"Shape is Overrated","name":"Curt Mayo IV","skill_level":5},{"team":"Shape is Overrated","name":"Anna Ellis","skill_level":3},{"team":"Shape is Overrated","name":"Chris Mayo","skill_level":4},{"team":"Shape is Overrated","name":"Chris Roberts","skill_level":5},{"team":"Shape is Overrated","name":"Eric Caneega","skill_level":4},{"team":"Shape is Overrated","name":"Josh Higgs","skill_level":4},

{"team":"Wildcards","name":"David Dent","skill_level":5},{"team":"Wildcards","name":"Linda Toskes","skill_level":2},{"team":"Wildcards","name":"Greg Becraft","skill_level":4},{"team":"Wildcards","name":"John Mullis","skill_level":4},{"team":"Wildcards","name":"Mike Creekmore","skill_level":4},{"team":"Wildcards","name":"Tiffany McCoy","skill_level":3},{"team":"Wildcards","name":"Brian Bentley","skill_level":4},{"team":"Wildcards","name":"Daniel McCoy","skill_level":4},

{"team":"The Outsiders","name":"Kelley Kitchens","skill_level":3},{"team":"The Outsiders","name":"Hubert Kitchens Jr","skill_level":4},{"team":"The Outsiders","name":"Bubba Kitchens III","skill_level":5},{"team":"The Outsiders","name":"Terri Ford","skill_level":4},{"team":"The Outsiders","name":"Bill Ford","skill_level":6},{"team":"The Outsiders","name":"Tracie Harris","skill_level":4},{"team":"The Outsiders","name":"Krystal Kitchens","skill_level":3},{"team":"The Outsiders","name":"David Everett","skill_level":3},

{"team":"Cobra Kai Pool","name":"Robert Giles","skill_level":5},{"team":"Cobra Kai Pool","name":"Joey Richard","skill_level":6},{"team":"Cobra Kai Pool","name":"Stephen Moore","skill_level":5},{"team":"Cobra Kai Pool","name":"Brandi Rollins","skill_level":4},{"team":"Cobra Kai Pool","name":"Alexis Clance","skill_level":3},{"team":"Cobra Kai Pool","name":"Michael Hendricks","skill_level":5},{"team":"Cobra Kai Pool","name":"Nicklos Nolan","skill_level":3},{"team":"Cobra Kai Pool","name":"Jon Jon Scott","skill_level":6},

{"team":"The Chalk Syndicate","name":"Bradley Hill","skill_level":5},{"team":"The Chalk Syndicate","name":"Travis Holloway","skill_level":4},{"team":"The Chalk Syndicate","name":"David Keller","skill_level":4},{"team":"The Chalk Syndicate","name":"Michael Bates","skill_level":5},{"team":"The Chalk Syndicate","name":"Julie Price","skill_level":2},{"team":"The Chalk Syndicate","name":"Hunter Brett","skill_level":6},{"team":"The Chalk Syndicate","name":"Colin Bagwell","skill_level":2},

{"team":"Ivey Generals","name":"Leesa Green","skill_level":3},{"team":"Ivey Generals","name":"Camo Crutchfield","skill_level":4},{"team":"Ivey Generals","name":"Abby Mixon","skill_level":5},{"team":"Ivey Generals","name":"Justin Mixon","skill_level":7},{"team":"Ivey Generals","name":"Mike Howell","skill_level":4},{"team":"Ivey Generals","name":"Kyle Swicord","skill_level":5},{"team":"Ivey Generals","name":"Kaylee Johnson","skill_level":3},

{"team":"Pool Hall Junkies","name":"Billy Hurt","skill_level":3},{"team":"Pool Hall Junkies","name":"Larry Sellars","skill_level":5},{"team":"Pool Hall Junkies","name":"Nathan Nation","skill_level":5},{"team":"Pool Hall Junkies","name":"Casey owes $15 Ash","skill_level":2},{"team":"Pool Hall Junkies","name":"Frank McClure","skill_level":6},{"team":"Pool Hall Junkies","name":"T-Dog Brantley","skill_level":5},{"team":"Pool Hall Junkies","name":"Daniel Izquierdo","skill_level":2},

{"team":"Merely Surviving","name":"Mitch Scoggins","skill_level":3},{"team":"Merely Surviving","name":"Chainsaw Wright","skill_level":3},{"team":"Merely Surviving","name":"Sam Jones","skill_level":3},{"team":"Merely Surviving","name":"Wolf Rice","skill_level":2},{"team":"Merely Surviving","name":"Red Birmingham","skill_level":2},{"team":"Merely Surviving","name":"Vernon Snellings","skill_level":2},{"team":"Merely Surviving","name":"Mary Peach Bembry","skill_level":2},{"team":"Merely Surviving","name":"Yolanda Rowlands","skill_level":2},
]

@app.route("/")
def home():
    return jsonify({"status":"APA Analytics Backend Running","division":"Ivey G 8-Ball","teams_loaded":10,"players_loaded":len(players)})

@app.route("/players")
def get_players():
    return jsonify(players)

@app.route("/teams")
def get_teams():
    teams = {}
    for p in players:
        teams.setdefault(p["team"], []).append(p)
    return jsonify(teams)

if __name__ == "__main__":
    app.run()
