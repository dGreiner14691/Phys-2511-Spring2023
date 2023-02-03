#!/usr/bin/env python
# coding: utf-8

# In[12]:


import random

#finding number of players
numplay = int(input("how many people will be playing? "))

#asking each players name
players = []
for i in range(numplay):
    playername = input("please put in player name: ")
    players.append({ "Name": str(playername), "Position": 1 })
    
def move(player, roll):
    player["Position"] += roll
    if player["Position"] > 50:
        player["Position"] = 50
    return player

def ladders(player): #dictionary of ladders in the game
    ladders = {
        3:3+random.randint(1,5), #using randint function so that not every game is the same :)
        9:9+random.randint(1,5),
        15:15+random.randint(1,5),
        21:21+random.randint(1,5),
        25:25+random.randint(1,5),
        31:31+random.randint(1,5),
        37:37+random.randint(1,5),
        43:43+random.randint(1,5)
    }
    if player["Position"] in ladders.keys():
        print("Player {} landed on a ladder and is moved from {} to {}".format(player["Name"], player["Position"], ladders[player["Position"]]))
        player["Position"] = ladders[player["Position"]]
    return player

def snakes(player): #dictionary of snakes in the game
    snakes = {
        6:6-random.randint(1,5), #same as ladders, except -randint so value is smaller
        12:12-random.randint(1,5),
        18:18-random.randint(1,5),
        24:24-random.randint(1,5),
        30:30-random.randint(1,5),
        36:36-random.randint(1,5),
        42:42-random.randint(1,5),
        48:48-random.randint(1,5)
    }
    if player["Position"] in snakes.keys():
        print("Player {} landed on a snake and is moved from {} to {}".format(player["Name"], player["Position"], snakes[player["Position"]]))
        player["Position"] = ladders[player["Position"]]
    return player

def game(players): #loop of the game
    for player in players:
        roll = random.randint(1,6) #dice roll 
        print("Player", players["Name"],"rolled a", roll)
        player = move(player,roll)
        player = ladders(player) #running new position through ladder & snake function to see if they are on either
        player = snakes(player)
        print("Player", players["Name"] , "is now on space", players["Position"])
        if player["Position"] == 50:
            print("player", players["Name"], "wins!")
            return

while True:
    game(players)
    for i in range(numplay):
        if players[i]["Position"] == 50:
            break

