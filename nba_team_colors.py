def get_team_color(team_name):
    """Return color hex code. Pass full team name as parameter."""
    colors_dict={
        "Atlanta Hawks": "#c8102e",
        "Brooklyn Nets": "#010101",
        "Boston Celtics": "#007a33",
        "Charlotte Hornets": "#201747",
        "Chicago Bulls": "#ba0c2f",
        "Cleveland Cavaliers": "#6f263d",
        "Dallas Mavericks": "#0050b5",
        "Denver Nuggets": "#418fde",
        "Detroit Pistons": "#003da5",
        "Golden State Warriors": "#ffc72d",
        "Houston Rockets": "#ba0c2f",
        "Indiana Pacers": "#041e42",
        "Los Angeles Clippers": "#d50032",
        "Los Angeles Lakers": "#702f8a",
        "Memphis Grizzlies": "#23375b",
        "Miami Heat": "#862633",
        "Milwaukee Bucks": "#2c5234",
        "Minnesota Timberwolves": "#002b5c",
        "New Jersey Nets": "#002a60",
        "New Orleans Pelicans": "#002b5c",
        "New York Knicks": "#003da5",
        "Oklahoma City Thunder": "#007dc3",
        "Orlando Magic": "#007dc5",
        "Philadelphia 76ers": "#006bb6",
        "Phoenix Suns": "#e56020",
        "Portland Trail Blazers": "#f0163a",
        "Sacramento Kings": "#724c9f",
        "San Antonio Spurs": "#b6bfbf",
        "Seattle SuperSonics": "#00653a",
        "Toronto Raptors": "#ce1141",
        "Utah Jazz": "#002b5c",
        "Washington Wizards": "#0c2340",
        }
    for key, value in colors_dict.items():
        if team_name == key:
            return value
        



