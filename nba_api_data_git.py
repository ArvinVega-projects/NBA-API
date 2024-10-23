# Create a bar chart of top 5 NBA teams and their total number of assists in a given season.
import requests

from nba_team_colors import get_team_color as get_color

import plotly.express as px

# Ask user to provide the year they want data for.
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
# This also catches incorrect user input since it will be an invalid URL.
if r.status_code == 200:
    print(f"Status: {r.status_code} (Success!)")
else:
    print(f"API Call Failed! Status Code: {r.status_code}.")
    print("Please verify that the year inputted is correct and try again.")
    exit()

assist_dict = r.json()


# Assign all keys and values for each team to variables.
# Note: format ####-## will always result in 200.
# use try-except block if the inputted year format is correct but no data available.
try:
    top_team_assists = assist_dict['resultSets'][0]['rowSet'][0]
except IndexError:
    print(f"Unfortunately, there is no data for this year.")
    exit()
else:
    second_team_assists = assist_dict['resultSets'][0]['rowSet'][1]
    third_team_assists = assist_dict['resultSets'][0]['rowSet'][2]
    fourth_team_assists = assist_dict['resultSets'][0]['rowSet'][3]
    fifth_team_assists = assist_dict['resultSets'][0]['rowSet'][4]

# Create a list that holds each team and their assists data.
all_teams_list = [top_team_assists, second_team_assists, third_team_assists,
                  fourth_team_assists, fifth_team_assists]

# Extract the rank, team id, team name, and assist totals for the year.
ranks, team_ids, team_names, assist_totals = [], [], [], []
# Create hover_text (hovertemplate) and clickable links (x tick label)
hover_texts, team_ast_video_links = [], []
for team in all_teams_list:
    ranks.append(team[0])
    team_ids.append(team[1])
    team_names.append(team[3])
    assist_totals.append(team[4])

# format the hover_texts and clickable links for the graph.
for rank, team_id, team_name, assist in zip(ranks, team_ids, team_names, assist_totals):
    hover_texts.append(
        f"Rank {rank}: {team_name} (Assist Totals: {format(assist, ',')})"
        "<extra></extra>" # this removes the associated color hovertemplate.
    )
    # href format: <a href='{url}'>{team_name}</a>
    team_ast_video_links.append(
        f"<a href='https://www.nba.com/stats/events?CFID=&CFPARAMS=&ContextMeasure=AST&GameID=&PlayerID=0&Season={nba_year}&SeasonType=Regular%20Season&TeamID={team_id}&flag=1&sct=plot&section=game'>{team_name}</a>"
    )

# Plot data on graph
title = f"Assist Totals {nba_year}: Top 5 Teams"
labels = {'x': 'Team', 'y': 'Assist Totals'}
# define min and max y values for graph.
y_min = assist_totals[4] - 10
y_max = assist_totals[0] + 10

fig = px.bar(x=team_ast_video_links, y=assist_totals, title=title,
             labels=labels,
             color=team_names,
             # custom_data is needed for hovertemplate.
             custom_data=[hover_texts],
             # use get_color to get each top 5 teeam's color for graph.
            color_discrete_map={
                team_name: get_color(team_name) for team_name in team_names
                }
)

# Adjust font size for; title, x, y,
fig.update_layout(title_font_size=20,
                  title_x=0.5,
                  xaxis_title_font_size=16, 
                  yaxis_title_font_size=16,
                  legend_title_text='', # remove legend title.
                  yaxis_range=[y_min, y_max], # set the y axis range
                  )

# have thousands separator included on y axis.
fig.update_yaxes(separatethousands=True)

# set hover display from custom_data (hover_texts)
fig.update_traces(hovertemplate="%{customdata}")

fig.show()