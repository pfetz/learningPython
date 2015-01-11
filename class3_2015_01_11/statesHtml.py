# Read in a CSV file of state abbreviations and names
# Create an HTML drop down for states

# Create two empty lists
abbrevs= []
state_names=[]

# Read the csv file
# split each apprev, name pair into separate lists
with open("states.csv", "r") as states_file:
    states = states_file.read().split("\n")
    for state in states:
        abbrev, state_name = state.split((","))
        abbrevs.append(abbrev)
        state_names.append(state_name)

# create the html element
# associate the two separate lists
print "<select>"
for abbrev, state_name in zip(abbrevs, state_names):
    print "<option value=\"{0}\">{1}</option>".format(abbrev, state_name)
print "</select>"


