from flask import Flask, jsonify, request

app = Flask(__name__)

players = [
{"team":"Team Bud","name":"Wayne Amerson","sl":6},{"team":"Team Bud","name":"Bill Methvin","sl":5},{"team":"Team Bud","name":"Jerry Barron","sl":4},{"team":"Team Bud","name":"Julie Barron","sl":2},{"team":"Team Bud","name":"Steven Asbell","sl":4},{"team":"Team Bud","name":"Rodney Amerson Sr","sl":4},{"team":"Team Bud","name":"Jeff Powell","sl":6},{"team":"Team Bud","name":"Josh Amerson","sl":4},
{"team":"Underdawgs","name":"Joey Ellis","sl":4},{"team":"Underdawgs","name":"Stephanie Lindsey","sl":3},{"team":"Underdawgs","name":"Wayne Johnson","sl":5},{"team":"Underdawgs","name":"Chase Lindsey","sl":2},{"team":"Underdawgs","name":"Dustin Stapleton","sl":7},{"team":"Underdawgs","name":"Little T Durden","sl":6},{"team":"Underdawgs","name":"Boss Hogg McCune","sl":2},{"team":"Underdawgs","name":"Candy Skinner","sl":3},
{"team":"Shape is Overrated","name":"Curt Mayo III","sl":6},{"team":"Shape is Overrated","name":"Curt Mayo IV","sl":5},{"team":"Shape is Overrated","name":"Anna Ellis","sl":3},{"team":"Shape is Overrated","name":"Chris Mayo","sl":4},{"team":"Shape is Overrated","name":"Chris Roberts","sl":5},{"team":"Shape is Overrated","name":"Eric Caneega","sl":4},{"team":"Shape is Overrated","name":"Josh Higgs","sl":4},
{"team":"Wildcards","name":"David Dent","sl":5},{"team":"Wildcards","name":"Linda Toskes","sl":2},{"team":"Wildcards","name":"Greg Becraft","sl":4},{"team":"Wildcards","name":"John Mullis","sl":4},{"team":"Wildcards","name":"Mike Creekmore","sl":4},{"team":"Wildcards","name":"Tiffany McCoy","sl":3},{"team":"Wildcards","name":"Brian Bentley","sl":4},{"team":"Wildcards","name":"Daniel McCoy","sl":4},
{"team":"The Outsiders","name":"Kelley Kitchens","sl":3},{"team":"The Outsiders","name":"Hubert Kitchens Jr","sl":4},{"team":"The Outsiders","name":"Bubba Kitchens III","sl":5},{"team":"The Outsiders","name":"Terri Ford","sl":4},{"team":"The Outsiders","name":"Bill Ford","sl":6},{"team":"The Outsiders","name":"Tracie Harris","sl":4},{"team":"The Outsiders","name":"Krystal Kitchens","sl":3},{"team":"The Outsiders","name":"David Everett","sl":3},
{"team":"Cobra Kai Pool","name":"Robert Giles","sl":5},{"team":"Cobra Kai Pool","name":"Joey Richard","sl":6},{"team":"Cobra Kai Pool","name":"Stephen Moore","sl":5},{"team":"Cobra Kai Pool","name":"Brandi Rollins","sl":4},{"team":"Cobra Kai Pool","name":"Alexis Clance","sl":3},{"team":"Cobra Kai Pool","name":"Michael Hendricks","sl":5},{"team":"Cobra Kai Pool","name":"Nicklos Nolan","sl":3},{"team":"Cobra Kai Pool","name":"Jon Jon Scott","sl":6},
{"team":"The Chalk Syndicate","name":"Bradley Hill","sl":5},{"team":"The Chalk Syndicate","name":"Travis Holloway","sl":4},{"team":"The Chalk Syndicate","name":"David Keller","sl":4},{"team":"The Chalk Syndicate","name":"Michael Bates","sl":5},{"team":"The Chalk Syndicate","name":"Julie Price","sl":2},{"team":"The Chalk Syndicate","name":"Hunter Brett","sl":6},{"team":"The Chalk Syndicate","name":"Colin Bagwell","sl":2},
{"team":"Ivey Generals","name":"Leesa Green","sl":3},{"team":"Ivey Generals","name":"Camo Crutchfield","sl":4},{"team":"Ivey Generals","name":"Abby Mixon","sl":5},{"team":"Ivey Generals","name":"Justin Mixon","sl":7},{"team":"Ivey Generals","name":"Mike Howell","sl":4},{"team":"Ivey Generals","name":"Kyle Swicord","sl":5},{"team":"Ivey Generals","name":"Kaylee Johnson","sl":3},
{"team":"Pool Hall Junkies","name":"Billy Hurt","sl":3},{"team":"Pool Hall Junkies","name":"Larry Sellars","sl":5},{"team":"Pool Hall Junkies","name":"Nathan Nation","sl":5},{"team":"Pool Hall Junkies","name":"Casey owes $15 Ash","sl":2},{"team":"Pool Hall Junkies","name":"Frank McClure","sl":6},{"team":"Pool Hall Junkies","name":"T-Dog Brantley","sl":5},{"team":"Pool Hall Junkies","name":"Daniel Izquierdo","sl":2},
{"team":"Merely Surviving","name":"Mitch Scoggins","sl":3},{"team":"Merely Surviving","name":"Chainsaw Wright","sl":3},{"team":"Merely Surviving","name":"Sam Jones","sl":3},{"team":"Merely Surviving","name":"Wolf Rice","sl":2},{"team":"Merely Surviving","name":"Red Birmingham","sl":2},{"team":"Merely Surviving","name":"Vernon Snellings","sl":2},{"team":"Merely Surviving","name":"Mary Peach Bembry","sl":2},{"team":"Merely Surviving","name":"Yolanda Rowlands","sl":2},
]

standings = [("Team Bud",107),("Underdawgs",101),("Shape is Overrated",100),("Wildcards",93),("The Outsiders",91),("Cobra Kai Pool",86),("The Chalk Syndicate",73),("Ivey Generals",72),("Pool Hall Junkies",69),("Merely Surviving",63)]

def roster(team):
    return [p for p in players if p["team"] == team]

def avg_sl(team):
    r = roster(team)
    return round(sum(p["sl"] for p in r) / len(r), 2)

def matchup_score(my_sl, opp_sl):
    diff = my_sl - opp_sl
    if diff == 0: return "Even"
    if diff == 1: return "Slight edge"
    if diff >= 2: return "Strong edge"
    if diff == -1: return "Risky"
    return "Avoid if possible"

@app.route("/")
def dashboard():
    options = "".join([f"<option>{t}</option>" for t,pts in standings if t != "Team Bud"])
    cards = ""
    for rank,(team,pts) in enumerate(standings,1):
        r = roster(team)
        high = max(r, key=lambda p:p["sl"])
        low = min(r, key=lambda p:p["sl"])
        plist = "".join([f"<li>{p['name']} <b>SL{p['sl']}</b></li>" for p in r])
        cards += f"<div class='card'><h2>{rank}. {team}<span>{pts} pts</span></h2><p><b>Avg SL:</b> {avg_sl(team)} | <b>Strongest:</b> {high['name']} SL{high['sl']} | <b>Lowest:</b> {low['name']} SL{low['sl']}</p><ul>{plist}</ul></div>"
    return f"""
<html><head><meta name='viewport' content='width=device-width, initial-scale=1'><title>APA Analytics</title>
<style>
body{{font-family:Arial;background:#f2f6fb;margin:0;color:#111}}header{{background:#006cb7;color:white;padding:22px;text-align:center}}.stats{{display:flex;gap:8px;padding:10px}}.box{{flex:1;background:white;padding:12px;border-radius:12px;text-align:center}}.card,.panel{{background:white;margin:12px;padding:14px;border-radius:12px;box-shadow:0 1px 4px #ccc}}h2{{color:#006cb7}}h2 span{{float:right;color:#333;font-size:16px}}li{{font-size:17px;padding:5px}}input,select,button{{width:94%;margin:8px;padding:13px;font-size:18px;border-radius:10px;border:1px solid #aaa}}button{{background:#006cb7;color:white;border:0;font-weight:bold}}
</style>
<script>
function searchPlayers(){{let q=document.getElementById('search').value.toLowerCase();document.querySelectorAll('.card').forEach(c=>c.style.display=c.innerText.toLowerCase().includes(q)?'block':'none');}}
async function analyze(){{let t=document.getElementById('team').value;let r=await fetch('/analyze/'+encodeURIComponent(t));let d=await r.json();let html='<h2>Scout Report: '+t+'</h2><p><b>Avg Skill:</b> '+d.avg_sl+'</p><p><b>Strongest:</b> '+d.strongest+'</p><p><b>Best Team Bud Matchups:</b></p><ul>';d.matchups.forEach(m=>html+='<li>'+m+'</li>');html+='</ul>';document.getElementById('report').innerHTML=html;}}
</script></head>
<body>
<header><h1>APA Analytics</h1><p>Ivey G 8-Ball Division</p></header>
<div class='stats'><div class='box'><b>10</b><br>Teams</div><div class='box'><b>{len(players)}</b><br>Players</div><div class='box'><b>Team Bud</b><br>Your Team</div></div>
<div class='panel'><h2>Opponent Scout Report</h2><select id='team'>{options}</select><button onclick='analyze()'>Analyze Opponent</button><div id='report'></div></div>
<input id='search' onkeyup='searchPlayers()' placeholder='Search team or player...'>
{cards}
</body></html>
"""

@app.route("/analyze/<team>")
def analyze(team):
    opp = roster(team)
    bud = roster("Team Bud")
    strongest = max(opp, key=lambda p:p["sl"])
    recs = []
    for o in sorted(opp, key=lambda p:p["sl"], reverse=True):
        best = sorted(bud, key=lambda b: abs(b["sl"]-o["sl"]))[0]
        recs.append(f"{best['name']} SL{best['sl']} vs {o['name']} SL{o['sl']} — {matchup_score(best['sl'], o['sl'])}")
    return jsonify({"team":team,"avg_sl":avg_sl(team),"strongest":f"{strongest['name']} SL{strongest['sl']}","matchups":recs})

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