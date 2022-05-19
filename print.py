from mkbsc import export
from parse import parse
import os
import json


def printpng(file):
    character = ""
    index1 = 1
    index2 = 1
    f = open(file, 'r')
    os.mkdir("pictures/basegame")
    for line in f:
        data = json.loads(line)
        if(data['stabilises'] > 0):
            character = "stabilised" + str(index1)
            index1 += 1
        else:
            character = "divergent" + str(index2)
            index2 += 1
        os.mkdir("pictures/basegame/" + character)
        game = parse(data)
        g1 = game.KBSC()
        g2 = g1.KBSC()
        g3 = g2.KBSC()
        export(game, "G", folder="pictures/basegame/"+character, view=False)
        export(g1, "GK1", folder="pictures/basegame/"+character, view=False)
        export(g2, "GK3", folder="pictures/basegame/"+character, view=False)
        export(g3, "GK4", folder="pictures/basegame/"+character, view=False)
    print("hi")


printpng('cartesiangames.txt')