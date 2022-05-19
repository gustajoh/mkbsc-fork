
from parse import parse
import json

def firstIteration():
    with open('50k3games.txt') as f:
        file = open('GK1only.txt', 'w')
        count = 0
        pos = 1
        for line in f:
            game = json.loads(line)
            ##iterate mkbscsc acncaioncancand write
            print(pos)
            pos += 1
            # remember kinda yikes in iterate_until_isomorphic with consider_observations=True
            magiian = parse(game)
            asd = magiian.KBSC()

            data = {}
            #Konstruerar sigma
            aleph = []
            for tuple in asd.alphabet:
                aleph.append(''.join(tuple))
            data["sigma"] = aleph

            index = 0
            translator = {}
            for state in asd.states:
                translator[state] = index
                index+=1


            #Konstruerar obs
            obs = []
            for i in range (asd.player_count):
                playerobs = []
                for j in range (len(asd.partitionings[i].observations)):
                    individualobs = []
                    for k in range (len(asd.partitionings[i].observations[j].states)):
                        individualobs.append(translator[asd.partitionings[i].observations[j].states[k]])
                    playerobs.append(individualobs)
                obs.append(str(playerobs))

            data["obs"] = obs

            ##yea
            data["L0"] = translator[asd.initial_state]
            data["players"] = asd.player_count
            data["stabilises"] = game["stabilises"]

            #Konstruerar delta
            delta = []
            for transition in asd.transitions:
                trans = "["
                trans+=(str(translator[transition.start]))
                trans+=","
                trans+=(''.join(transition.joint_action))
                trans+=","
                trans+=(str(translator[transition.end]))
                trans+= "]"
                delta.append(trans)
            data["delta"] = delta

            states = []
            for state in asd.states:
                states.append(translator[state])

            data["states"] = states

            json.dump(data, file)
            file.write('\n')
        print(count)


#Reads data from generated game and formats it as usable data for the implemented mkbsc algorithm
#Returns the game data with information if it stabilises or not

firstIteration()
