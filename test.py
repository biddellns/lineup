from matchup import Matchup
from lineup import Lineup

def main():
    lineup = Lineup('1','2')
    lineup.addMatch('Kohonski', '907', 'excloud', '123', 'Dusk Towers', 'Platinum')
    lineup.addMatch('tbham', '274', 'notsofast', '737', 'Overgrowth', 'Silver')
    lineup.addMatch('Riker', '810', 'OddHonor', '600', 'Frost', 'Gold')
    lineup.addMatch('Intuion', '233', '|||||||||', '918', 'King Sejong Station', 'Masters')
    print(lineup)

if __name__ == '__main__':
    main()
