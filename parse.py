# Python program to read
# json file
from mkbsc import MultiplayerGame

import ast

# Reads data from generated game and formats it as usable data for the implemented mkbsc algorithm
# Returns the game data with information if it stabilises or not

def parse(data):
    L = data["states"]
    L0 = data["L0"]
    Sigma = data["sigma"]
    Delta = data["delta"]
    Obs = data["obs"]

    # Sigma will always be size 1?
    sigma = []
    for element in Sigma:
        sigma.append(tuple(element))
    sigma = tuple(sigma)

    delta = []
    for element in Delta:
        # remove a bunch of non-essential brackets, commas and '
        transition = str(element).replace('[', '').replace(']', '').replace("'", "").replace(",", "")
        transition = tuple([int(transition[0:1])]) + (tuple(transition[1:-1]),) + tuple([int(transition[-1:])])
        delta.append(transition)

    obs = []
    for element in Obs:
        element = ast.literal_eval(element)
        obs.append(element)

    game = MultiplayerGame.create(L, L0, sigma, delta, obs)

    return game
