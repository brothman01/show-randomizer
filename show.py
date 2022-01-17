# Ben Rothman - Show Randomizer
# this program reads the show info in from the csv file and gives a random show 
# out of the selected shows or a random episode of a random season of the show
# specified by the user based on what was chosen with the parameters.
from random import randint 
import sys
import csv
import pprint
import os

path = os.path.dirname(__file__) ## directory of file
# os.path.dirname(os.path.dirname(file)) ## directory of directory of file
# os.chdir(path)

# dictionary of all shows
shows = dict()

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
# convert args into usable code
arg_names = ['command', 'term']
args = tuple(sys.argv)
term = args[1]

# read the shows and create a list of 'Show's
shows = readShows('data.csv')

if ( term == 'show'): # if the user wants a random show
    print(keyList(shows)[randint(1, len( shows.keys() ) - 1 )])
else: # if the user wants a random episode from a specific show
    title = ' '.join(args[1:])
    try:
        show = shows[title]
    except:
        print('"',title,'" is not in the list of shows',sep='')

    season = show.getRandomSeason()
#     # seasonInfo = show.getEpisodes(season)
    episode = randint(1, int( show.getEpisodes(season).split(':')[1] ) )  
    print(title + ' s' + str(season) + 'e' + str(episode))

##################