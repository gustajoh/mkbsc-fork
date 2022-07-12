import copy

from mkbsc import multiplayer_game, iterate_until_isomorphic
import json
from parse import parse

def reduce():
    with open('generatedgames.txt') as f:
        file = open('reduced.txt', 'w')
        for line in f:
            game = json.loads(line)
            deeplist = copy.deepcopy(game["delta"])
            previous = -1
            while len(deeplist) != previous:
                previous = len(deeplist)
                for edge in deeplist:
                    game["delta"] = copy.deepcopy(deeplist)
                    game["delta"].remove(edge)
                    magiian = parse(game)
                    res = iterate_until_isomorphic(magiian, limit=100, print_size=False, verbose=False, sizelimit=500)
                    #print(res)
                    if res[-1] == 0:        #divergent game
                        deeplist.remove(edge)
                game["delta"] = deeplist
            json.dump(game, file)
            file.write('\n')

reduce()