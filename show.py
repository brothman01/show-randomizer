from random import randint 
import sys

# convert args into usable code
arg_names = ['command', 'term']
args = dict(zip(arg_names, sys.argv))
term = args['term']

# read data file into program
f = open('data.txt', "r")
lines = f.readlines()
f.close()

# if the user wants a random show
if ( term == 'show'):
    chosen_index = randint(1, len( lines ) - 1 )
    chosen_line = lines[chosen_index].split(',')
    show = chosen_line.pop(0)
    season = randint(1, len( chosen_line )  )
    season = season - 1
    episode = randint(1, int( chosen_line[season] ) )
    print(show)
else: # if the user wants a random episode from a specific show
    for line in lines:
        if (line.startswith(str(term))):
            chosen_index = l
            chosen_line = lines[chosen_index].split(',')
            show = chosen_line.pop(0)
            season = randint(1, len( chosen_line )  )
            season = season - 1
            episode = randint(1, int( chosen_line[season] ) )       
    print(show + ' s' + str(season) + 'e' + str(episode))
