# Create a scatter_geo of all NBA teams and their total number of assists in a given season.
import requests

# Ask user to provide the year they want data in.
print("Please provide the desired year for top assist leaders by team.")
nba_year = input("Format Year Example (2023-24): ")

# Assign API call to variable and define headers.

url = "https://stats.nba.com/stats/"
url += f"assistleaders?LeagueID=00&PerMode=Totals&PlayerOrTeam=Team&Season={nba_year}&SeasonType=Regular+Season"

STATS_HEADERS = {
    'Host': 'stats.nba.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
}
r = requests.get(url, headers=STATS_HEADERS)

# Confirm API call successful
#
if r.status_code == 200:
    print(f"Status: {r.status_code} (Success!)")
else:
    print(f"API Call Failed! Status Code: {r.status_code}.")
    print("Please verify that the year inputted is correct and try again.")
    exit()

assist_dict = r.json()

# all keys and values for each team 
# use try-except block if the inputted year format is correct but no data available.
try:
    top_team_assists = assist_dict['resultSets'][0]['rowSet'][0]
except IndexError:
    print(f"Unfortunately, there is no data for this year.")
    exit()
else:
    second_team_assists = assist_dict['resultSets'][0]['rowSet'][1]
    third_team_assists = assist_dict['resultSets'][0]['rowSet'][2]

# create a list that holds each team and their data.
all_teams_list = [top_team_assists, second_team_assists, third_team_assists]

# extract the rank, team name, and assist totals for the year.
ranks, team_names, assist_totals = [], [], []
for team in all_teams_list:
    ranks.append(team[0])
    team_names.append(team[3])
    assist_totals.append(team[4])

# format each assist total to include commas with list comprehension.
assist_totals = [format(assist, ",") for assist in assist_totals]

print(f"Assist Totals {nba_year}: Top 3 Teams")
print(f"Rank {ranks[0]}: {team_names[0]} (Assist Totals: {assist_totals[0]})")
print(f"Rank {ranks[1]}: {team_names[1]} (Assist Totals: {assist_totals[1]})")
print(f"Rank {ranks[2]}: {team_names[2]} (Assist Totals: {assist_totals[2]})")
