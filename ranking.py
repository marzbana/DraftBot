# class that returns a string of highest ranked available players
import csv

class ranking:
#constructor
    def __init__(self):
        self.file = {}
        self.read()

    def getTopPlayers(self, playersSelected):
        for player in playersSelected:
            self.updateRow(player)
        self.write()

    # returns a string of the top 2 players available in each position with their PLAYER NAME, POS, and BYE WEEK as well as the top 10 overall players with the same info 
    def findPlayers(self):
        # dictionary to hold the top 2 players in each position
        topPlayers = {'QB' : [],
                      'WR' : [],
                      'RB' : [],
                      'TE' : [],
                      'K' : [],
                      'DEF' : []}
        # dictionary to hold the top 10 players overall
        topPlayersOverall = []
        taken = False
        for row in self.file:
            if(row['Taken'] == 0):
                if(len(topPlayersOverall) <10):
                    topPlayersOverall.append("PLAYER NAME: " + row['PLAYER NAME'] + " POS: " + row['POS'] + " BYE WEEK: " + row['BYE WEEK'] + ".")
                    taken = True
                if(len(topPlayers[row["POS"]]) < 2):
                    topPlayers[row["POS"]].append("PLAYER NAME: " + row['PLAYER NAME'] + " POS: " + row['POS'] + " BYE WEEK: " + row['BYE WEEK']+ ".")
                    taken = True
                if(taken):
                    taken = False
                    row['Taken'] = 1
                if (len(topPlayersOverall) >= 10 and len(topPlayers[row["POS"]]) >= 2):
                    break
        stringReturn = "Top 2 players in each position: "
        for key in topPlayers:
            for player in topPlayers[key]:
                stringReturn += player + ". "
        stringReturn += " Top 10 players overall: "
        for player in topPlayersOverall:
            stringReturn += player + ". "
        return stringReturn


    def updateRow(self, player):
        for row in self.file:
            if row['PLAYER NAME'] == player:
                row['Taken'] = 1
                break

    def read(self):
        with open ('Ranking.csv', 'r') as file:
            reader = csv.reader('Rankings.csv')
            self.file = reader
    def write(self):
        with open('Rankings.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            fieldnames = list(self.file[0].keys())
            # Write the headers
            writer.writeheader()
            
            # Write the dictionary data
            for row in self.file:
                writer.writerow(row)
