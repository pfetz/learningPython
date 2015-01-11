# Read in a CSV file of state abbreviations and names
# Create an HTML drop down for states
# Print the HTML element to a file

# read in the states file
with open("states.csv", "r") as states_file:
    states = states_file.read().split("\n")

# loop through the entries in the states file
# split the abbreviation and the state
# create the HTML element
print "<select>"
for state in states:
    abbrev, state_name = state.split(",")
    print "<option value=\"{0}\">{1}</option>".format(abbrev, state_name)
print "</select>"

# write to a new file
with open('states.html', 'w') as state_html_file:
    state_html_file.write("<select>")
    for state in states:
        abbrev, state_name = state.split(",")
        state_html_file.write("<option value=\"{0}\">{1}</option>".format(abbrev, state_name))
    state_html_file.write("</select>")
