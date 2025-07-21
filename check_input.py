def check_user_input(nba_year):
    """Checks validity of user input."""
    # Check that the last two numbers and 3rd and 4th numbers are accurate year
    # formats.
    try:
        # Extract last two characters of nba_year.
        last_two = int(nba_year[-2:])
        # Extract the two characters after the first two and before the last 3.
        first_two = int(nba_year[2:-3])

        difference = last_two - first_two
        # Check to see if difference is 1 or -99 (to account for 1999-00).
        if difference == 1 or difference == -99:
            pass
        else:
            exit_bad_input()
    except ValueError:
        exit_bad_input()

def exit_bad_input():
    """Exits program if user input is incorrect. Error message will be
    displayed."""

    bad_input = print("Invalid format. Please verify that the year inputted is correct and try again.")
    exit()
    return bad_input



    