import vector
class chat:
    def __init__(self):
        self.vector = vector()
        self.vector.init()
    prompt  = "You are a espn nfl draft bot. Your job is to select a player for the user to draft. A list of available players, and already drafted players will be passed in. The goal is to produce the best draft team. Some things to consider are the position of the player, the team they play for, their bye weeks, and their stats. The user can draft 4 QBs max, 8 WRs max, 8 RBs max, 3 TEs max, 3 Ks max, and 3 DEFs max. The user will draft 18 players total. The exact breakdown of the number of players to select in each postion is up to you but can't exceed the max. Please respond with only the name of a single player and nothing else."
    
    def query(self, topPlayers, players):
        prompt = self.prompt + "The top players available are: " + topPlayers + ". The players already selected are: " + players + ". Who does the user select?"
        self.vector.setquery(prompt)
        return self.vector.setresponse()
        