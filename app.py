import fantasy, chat, ranking


class App:
    # class to run the app
    # framework for the fantasy football draft bot

    #data structrures to hold players and draft logic
    #dictionary that holds lists
    players  = {'QB' : [],
                'WR' : [],
                'RB' : [],
                'TE' : [],
                'K' : [],
                'DEF' : []}
    # Max number of players per position
    QB_MAX = 4
    WR_MAX = 8
    RB_MAX = 8
    TE_MAX = 3
    K_MAX = 3
    DEF_MAX = 3

    # initiate objects
    def __init__(self):
        fantasy = fantasy()
        chat = chat()
        ranking = ranking()

    def run(self):

        # objects
        fantasy = self.fantasy
        chat = self.chat
        ranking = self.ranking

        # while the draft is going
        while(fantasy.draftGoing()):
            # if its my turn
            if(fantasy.myTurn()):
                #gets top players available
                playersSelected = fantasy.getPlayersSelected()
                topPlayers = ranking.getTopPlayers(playersSelected)
                # query gpt for player to select
                player = chat.query(topPlayers, self.players)
                # select player
                fantasy.selectPlayer(player)


# running
app = App()
app.run()



