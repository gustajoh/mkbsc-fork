from mkbsc import MultiplayerGame, iterate_until_isomorphic
from parse import parse
import json
with open('generatedgames.txt') as f:
    file = open('analysedgames.txt', 'w')
    count = 0
    pos = 1
    for line in f:
        game = json.loads(line)
        ##iterate mkbsc and write
        print(pos)
        pos += 1
        # remember kinda yikes in iterate_until_isomorphic with consider_observations=True
        G = parse(game)

        #check if game stabilises
        result = iterate_until_isomorphic(G, limit=-1, print_size=False, verbose=False, sizelimit=500)
        game['stabilises'] = result[-1]
        if(game["stabilises"] > 0): count += 1
        json.dump(game, file)
        file.write('\n')

    print(count)