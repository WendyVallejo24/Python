def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    return teams[-1][1]
    pass

print(losing_team_captain([["Antonio", "Miguel", "Juan", "Manuel"], ["Jesus", "Jose", "Luis", "Armando"]]))