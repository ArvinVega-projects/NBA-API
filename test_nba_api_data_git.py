# Test code sections
# Note: Since user input is included, ensure to type the following in terminal:
# python3 -m pytest -s
import requests
import nba_api_data as nba

def get_status_code(url, headers):
    """Retrieve status code from API URL."""
    r = requests.get(url, headers=headers)
    return r.status_code

def get_len_axes(axis):
    """Retrieve number of elements for each axis."""
    count = len(axis)
    return count

def get_color_values():
    """Retrieve the hex color code values for each team"""
    team_colors = [nba.get_color(team) for team in nba.team_names]
    return team_colors

def test_status_code():
    """Will test status code == 200 based on API call and user input?"""
    status_code = get_status_code(nba.url, headers=nba.STATS_HEADERS)
    assert status_code == 200

def test_assist_values():
    """Will each element in assist_totals contain values (>=0)?"""
    assist_values = [assist >= 0 for assist in nba.assist_totals]
    assert assist_values == [assist == True for assist in assist_values]

def test_axes_match_count():
    """
    Will the axes have the same length of elements?
    x = 5 (number of teams)
    y = 5 (number of assist totals, not the values themselves.)
    """
    x_axis = get_len_axes(nba.team_ast_video_links)
    y_axis = get_len_axes(nba.assist_totals)
    assert x_axis == y_axis

def test_color_null():
    """Will each team have an associated color value?"""
    values = get_color_values()
    assert None not in values
