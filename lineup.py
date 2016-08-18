import matchup
class Lineup:
    NUM_MATCHES_PER_MATCHUP = 8

    def __init__(self, season, week):
        self.season = season
        self.week = week
        self.matchups = []
        self.num_matches = 0

    def addMatch(self, player1_name, player1_id, player2_name, player2_id,
                    map_name, league_level):
        mu = matchup.Matchup(player1_name, player1_id, player2_name, player2_id, map_name, league_level)

        # Prelim work to ensure
        self.matchups.append(mu)
        self.num_matches += 1

    def __str__(self):
        pretty_print = ""
        for match in self.matchups:
            pretty_print += str(match)
        return pretty_print
