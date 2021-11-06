import random

def generateGameBoard(obstaclePercentage):
    return [0 if random.randint(0, 100) > obstaclePercentage else random.randrange(1, 101) for i in range(101)]

def diceroll():
    return random.randint(1, 6)
    
def gameSimulation(gameboard, numberOfPlayer):
    players = {}
    

    for i in range(numberOfPlayer):
        players[i] = 0

    gameWon = False
    while(not gameWon):
        status = []
        for i in range(numberOfPlayer):
            roll = diceroll()
            players[i] += roll if players[i] + roll <= 100 else 0
            if gameboard[players[i]] !=  0:
                if gameboard[players[i]] > players[i]:
                    status.append("player number " + str(i) + " landed on a latter moving to " + str(gameboard[players[i]]))
                else:
                    status.append("player number " + str(i) + " landed on a snake moving to " + str(gameboard[players[i]]))
                players[i] = gameboard[players[i]]
        printStatus(players, status)
        if(max(players.values()) == 100):
            gameWon = True
    return


def printStatus(players, statuses):
    print("Events:")
    for i in range(len(statuses)):
        print(statuses[i])
    for i in players:
        print(i, ":", players[i])


gameSim = generateGameBoard(15)
gameSimulation(gameSim, 2)
