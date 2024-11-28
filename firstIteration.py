from parse import parse
import json

#Reads data from generated game and formats it as usable data for the implemented mkbsc algorithm
#Returns the game data with information if it stabilises or not

def firstIteration():
    with open('generatedgames.txt') as f:
        file = open('firstiterations.txt', 'w')
        count = 0
        pos = 1
        for line in f:
            game = json.loads(line)
            # Iterate mkbsc and write
            print(pos)
            pos += 1
            magiian = parse(game)
            asd = magiian.KBSC()

            data = {}
            # Construct sigma
            sigma = []
            for tuple in asd.alphabet:
                sigma.append(''.join(tuple))
            data["sigma"] = sigma

            index = 0
            translator = {}
            for state in asd.states:
                translator[state] = index
                index+=1


            # Construct obs
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

            data["L0"] = translator[asd.initial_state]
            data["players"] = asd.player_count
            data["stabilises"] = game["stabilises"]

            # Construct delta
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

firstIteration()
