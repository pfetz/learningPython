with open("states.csv", "r") as states_file:
    states = states_file.read().split("\n")

for index, state in enumerate (states) :
    states[index] = state.split(",")
    print index, states[index]
    print state

#print states
