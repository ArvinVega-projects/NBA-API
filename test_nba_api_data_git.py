import requests

def get_api_url(year):
    """Returns API URL with static year."""
    url = "https://stats.nba.com/stats/"
    url += f"assistleaders?LeagueID=00&PerMode=Totals&PlayerOrTeam=Team&Season={year}&SeasonType=Regular+Season"
    return url

def test_status_code():
    """Tests if given parameter will provide status code 200."""
    api_url = get_api_url("2020-21")
    STATS_HEADERS = {
    'Host': 'stats.nba.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    }
    r = requests.get(url=api_url, headers=STATS_HEADERS)
    # status code 200 is a successful API call.
    assert r.status_code == 200








    

