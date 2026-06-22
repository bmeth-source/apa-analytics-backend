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

standings = [
("Team Bud",107),("Underdawgs",101),("Shape is Overrated",100),("Wildcards",93),
("The Outsiders",91),("Cobra Kai Pool",86),("The Chalk Syndicate",73),
("Ivey Generals",72),("Pool Hall Junkies",69),("Merely Surviving",63)
]

@app.route("/")
def dashboard():
    rows = ""
    for rank, (team, pts) in enumerate(standings, 1):
        roster = [p for p in players if p["team"] == team]
        plist = "".join([f"<li>{p['name']} <b>SL{p['skill_level']}</b></li>" for p in roster])
        rows += f"""
        <div class='card'>
          <h2>{rank}. {team} <span>{pts} pts</span></h2>
          <ul>{plist}</ul>
        </div>
        """
    return f"""
    <html>
    <head>
      <title>APA Analytics</title>
      <meta name='viewport' content='width=device-width, initial-scale=1'>
      <style>
        body {{ font-family: Arial; background:#f2f6fb; margin:0; color:#111; }}
        header {{ background:#006cb7; color:white; padding:18px; text-align:center; }}
        .stats {{ display:flex; gap:10px; padding:12px; }}
        .box {{ flex:1; background:white; padding:14px; border-radius:12px; text-align:center; }}
        .card {{ background:white; margin:12px; padding:14px; border-radius:12px; box-shadow:0 1px 4px #ccc; }}
        h2 {{ margin:0 0 8px; color:#006cb7; font-size:20px; }}
        h2 span {{ float:right; color:#333; font-size:16px; }}
        li {{ padding:6px 0; font-size:17px; }}
        input {{ width:92%; margin:12px; padding:14px; font-size:18px; border-radius:10px; border:1px solid #aaa; }}
      </style>
      <script>
        function searchPlayers() {{
          let q = document.getElementById('search').value.toLowerCase();
          document.querySelectorAll('.card').forEach(c => {{
            c.style.display = c.innerText.toLowerCase().includes(q) ? 'block' : 'none';
          }});
        }}
      </script>
    </head>
    <body>
      <header>
        <h1>APA Analytics</h1>
        <p>Ivey G 8-Ball Division</p>
      </header>
      <div class='stats'>
        <div class='box'><b>10</b><br>Teams</div>
        <div class='box'><b>{len(players)}</b><br>Players</div>
        <div class='box'><b>Team Bud</b><br>Your Team</div>
      </div>
      <input id='search' onkeyup='searchPlayers()' placeholder='Search team or player...'>
      {rows}
    </body>
    </html>
    """

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