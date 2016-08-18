class Matchup(object):
    def __init__(self, player_name, player_id, 
            player_name2, player_id2, map_name, league_level):
        self.map_name = map_name
        self.player_name = player_name
        self.player_id = player_id
        self.player_name2 = player_name2
        self.player_id2 = player_id2
        self.league_level = league_level

    def __str__(self):
        return '{}#{} vs {}#{} on {}\n'.format(self.player_name, self.player_id, 
                                                self.player_name2, self.player_id2, self.map_name)


'''def main():
    mu = Matchup('Kohonski', '123', 'excloud', '456', 'Dusk Towers', 'Platinum')
    print(mu)

if __name__ == '__main__':
    main()'''
