# Ben Rothman - Show Randomizer
# this program reads the show info in from the csv file and gives a random show 
# out of the selected shows or a random episode of a random season of the show
# specified by the user based on what was chosen with the parameters.
from random import randint 
import sys
import csv
import pprint

# dictionary of all shows
shows = dict()

# convert args into usable code
arg_names = ['command', 'term']
args = tuple(sys.argv)
term = args[1]

# Support Functions
def keyList(dict):
    list = []
    for key in dict.keys():
        list.append(key)   
    return list

# read show information into a dict
with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row[0] == '#Title':
                continue
            else:
                title = row[0]
                seasons = len(row) + 1
                for x in range(1, len(row)):
                    if title in shows.keys():
                        shows[title].append(row[x])
                    else:
                        shows[title] = [row[x]]



##### Program #####

if ( term == 'show'): # if the user wants a random show
    index = randint(1, len( shows.keys() ) - 1 )
    print(keyList(shows)[index])
else: # if the user wants a random episode from a specific show
    title = term
    info = shows[term]
    season = randint(1, len( info )  )
    episode = randint(1, int( info[season].split(':')[1] ) )  
    print(title + ' s' + str(season) + 'e' + str(episode))

##################