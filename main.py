from flask import Flask, jsonify

app = Flask(__name__)

players = [
    {"team":"Team Bud","name":"Wayne Amerson","sl":5},
    {"team":"Underdawgs","name":"Joey Ellis","sl":5},
    {"team":"Shape is Overrated","name":"Curt Mayo III","sl":5},
    {"team":"Wildcards","name":"David Dent","sl":5},
    {"team":"The Outsiders","name":"Kelley Kitchens","sl":5},
    {"team":"Cobra Kai Pool","name":"Robert Giles","sl":5},
    {"team":"The Chalk Syndicate","name":"Bradley Hill","sl":5},
    {"team":"Ivey Generals","name":"Leesa Green","sl":4},
    {"team":"Pool Hall Junkies","name":"Billy Johnson","sl":4},
    {"team":"Merely Surviving","name":"Mitch Smith","sl":4},
]

standings = [
    ("Team Bud",107),
    ("Underdawgs",102),
    ("Shape is Overrated",99),
    ("Wildcards",96),
    ("The Outsiders",94),
    ("Cobra Kai Pool",91),
    ("The Chalk Syndicate",88),
    ("Ivey Generals",84),
    ("Pool Hall Junkies",80),
    ("Merely Surviving",76),
]

def roster(team):
    return [p for p in players if p["team"] == team]

def avg_sl(team):
    r = roster(team)
    if not r:
        return 0
    return round(sum(p["sl"] for p in r) / len(r), 2)

def matchup_score(my_sl, opp_sl):
    diff = my_sl - opp_sl
    if diff == 0:
        return "Even"
    if diff == 1:
        return "Slight edge"
    if diff >= 2:
        return "Strong edge"
    if diff == -1:
        return "Risky"
    return "Avoid if possible"

@app.route("/")
def dashboard():
    cards = ""
    for rank, item in enumerate(standings, start=1):
        team, pts = item
        r = roster(team)
        names = "".join([f"<li>{p['name']} — SL{p['sl']}</li>" for p in r])
        cards += f"""
        <div class='card'>
            <h2>{rank}. {team}</h2>
            <p><b>Points:</b> {pts}</p>
            <p><b>Average Skill Level:</b> {avg_sl(team)}</p>
            <button onclick="analyzeTeam('{team}')">Scout Team</button>
            <ul>{names}</ul>
        </div>
        """

    return f"""
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {{
    font-family: Arial;
    background: #f2f6fb;
    margin: 0;
    padding: 0;
}}
header {{
    background: #0b67a3;
    color: white;
    padding: 18px;
    text-align: center;
}}
.panel {{
    background: white;
    margin: 12px;
    padding: 14px;
    border-radius: 12px;
    box-shadow: 0 2px 8px #ccc;
}}
.card {{
    background: white;
    margin: 12px;
    padding: 14px;
    border-radius: 12px;
    box-shadow: 0 2px 8px #ccc;
}}
.stats {{
    display: flex;
    gap: 8px;
    margin: 12px;
}}
.box {{
    flex: 1;
    background: white;
    padding: 12px;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0 2px 8px #ccc;
}}
input, select, button {{
    width: 100%;
    padding: 12px;
    margin-top: 8px;
    font-size: 16px;
    border-radius: 8px;
    border: 1px solid #ccc;
}}
button {{
    background: #0b67a3;
    color: white;
    font-weight: bold;
}}
li {{
    margin-bottom: 6px;
}}
.result {{
    background: #e9f5ff;
    padding: 12px;
    border-radius: 10px;
    margin-top: 10px;
}}
</style>

<script>
async function searchPlayers() {{
    let q = document.getElementById("search").value.toLowerCase();
    let res = await fetch("/players");
    let data = await res.json();
    let out = "";
    data.forEach(p => {{
        if (p.name.toLowerCase().includes(q) || p.team.toLowerCase().includes(q)) {{
            out += `<li><b>${{p.name}}</b> — ${{p.team}} — SL${{p.sl}}</li>`;
        }}
    }});
    document.getElementById("searchResults").innerHTML = out;
}}

async function analyzeTeam(team) {{
    let res = await fetch("/analyze/" + team);
    let data = await res.json();
    let out = `<div class='result'><h3>${{data.team}} Scout Report</h3>`;
    out += `<p><b>Average SL:</b> ${{data.avg_sl}}</p>`;
    out += `<p><b>Strongest Player:</b> ${{data.strongest}}</p>`;
    out += `<h4>Recommended Matchups</h4><ul>`;
    data.recommendations.forEach(r => out += `<li>${{r}}</li>`);
    out += `</ul></div>`;
    document.getElementById("scoutReport").innerHTML = out;
    window.scrollTo(0,0);
}}
</script>
</head>

<body>
<header>
    <h1>APA Analytics</h1>
    <p>Ivey G 8-Ball Division Dashboard</p>
</header>

<div class="stats">
    <div class="box"><b>10</b><br>Teams</div>
    <div class="box"><b>{len(players)}</b><br>Players Entered</div>
    <div class="box"><b>Phase 3</b><br>Analytics</div>
</div>

<div class="panel">
    <h2>Player Search</h2>
    <input id="search" onkeyup="searchPlayers()" placeholder="Search player or team">
    <ul id="searchResults"></ul>
</div>

<div class="panel">
    <h2>Opponent Scout Report</h2>
    <div id="scoutReport">Tap “Scout Team” on any team below.</div>
</div>

{cards}

</body>
</html>
"""

@app.route("/analyze/<team>")
def analyze(team):
    opp = roster(team)
    bud = roster("Team Bud")

    if not opp:
        return jsonify({
            "team": team,
            "avg_sl": 0,
            "strongest": "No roster entered",
            "recommendations": []
        })

    strongest = max(opp, key=lambda p: p["sl"])

    recs = []
    for o in sorted(opp, key=lambda p: p["sl"], reverse=True):
        best = sorted(bud, key=lambda b: abs(b["sl"] - o["sl"]))[0] if bud else None
        if best:
            recs.append(
                f"{best['name']} SL{best['sl']} vs {o['name']} SL{o['sl']} — {matchup_score(best['sl'], o['sl'])}"
            )

    return jsonify({
        "team": team,
        "avg_sl": avg_sl(team),
        "strongest": f"{strongest['name']} SL{strongest['sl']}",
        "recommendations": recs
    })

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
    app.run(host="0.0.0.0", port=5000)