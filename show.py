# Ben Rothman - Show Randomizer
# this program reads the show info in from the csv file and gives a random show
# out of the selected shows or a random episode of a random season of the show
# specified by the user based on what was chosen with the parameters.
from random import randint
import sys
import csv
import pprint
import os

# Class Definitions
class Show:
    def __init__(self, row):
        self.title = row[0]
        self.seasons = list()
        for x in row:
            if x == self.title:
                continue
            elif len(self.seasons) > 0:
                (self.seasons).append(x)
            else:
                self.seasons = [x]

    def getSeasons(self):
        return self.seasons

    def getEpisodes(self, season):
        return self.seasons[season - 1]

    def getRandomSeason(self):
        return randint(0, len( self.seasons) )

    def __str__(self):
        return self.title + ' ' + str(len(self.seasons)) + ' seasons'

# Support Functions
def keyList(dict):
    list = []
    for key in dict.keys():
        list.append(key)
    return list

def readShows(path):
    retval = dict()
    with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if row[0] == '#Title':
                    continue
                else:
                    show = Show(row)
                    retval[row[0]] = show
    return retval



##### Program #####
shell_mode = True # by default

# path to this file
path = os.path.dirname(__file__)

# dictionary of all shows
shows = dict()

#instantiate variable
title = ''

# get input and decide what to do
arg_names = ['command', 'term']
args = tuple(sys.argv)
if shell_mode == True:
    term = input('args: ')
    title = term
else:
    term = args[1]

# read the shows and create a list of 'Show's
shows = readShows('data.csv')

# get the show with title specified in the input
if ( term == 'show'): # if the user wants a random show
    print(keyList(shows)[randint(1, len( shows.keys() ) - 1 )])
else:
    try:
        show = shows[title]
        season = show.getRandomSeason()
        episode = randint(1, int( show.getEpisodes(season).split(':')[1] ) )
        print(title + ' s' + str(season) + 'e' + str(episode))
    except:
        print('"',title,'" is not in the list of shows',sep='')


##################
