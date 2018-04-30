#Importations And Value Table Creation#
from random import randint

bot_field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

player_field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

bot_sonar = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

player_sonar = [["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]]

def printField(A):#Special print command for outputing the above arrays.
    if str.lower(A) == "a":
        print("\n---Players Ships---")
        for i in range(10):
            for j in range(10):
                print(player_field[i][j], "", end = "")
            print()
    if str.lower(A) == "b":
        print("\n---Players Ships--------Tracer Field---")
        for i in range(10):
            for j in range(10):
                print(player_field[i][j], "", end = "")
            for k in range(10):
                print(player_sonar[i][k], "", end = "")
            print()
    print()

def emptyShips(A):#Self check command which helps determine when the game ends.
    isEmpty = True
    for i in range(5):
        if A == "a":
            if bot_ships[i] != 0:
                isEmpty = False
        if A == "b":
            if player_ships[i] != 0:
                isEmpty = False
    return isEmpty

bot_ships = [2, 3, 3, 4, 5]
player_ships = [2, 3, 3, 4, 5]
ship_names = ["Destroyer", "Submarine", "Cruiser", "Battleship", "Aircraft Carrier"]
#End#
#Intro#
print("Welcome to Battleship: Python Edition.")
print("\nIf you are new to the game of Battleship, get instructions by typing \"Help\".")
start_Condition = input("\nOtherwise, if you know how to play already then simply press the Enter key.")

if str.lower(start_Condition) == "help":
    print("""\nThe game of Battleship is simple. There are two players who each have 5 ships.
        Setup:

        These ships are your Destroyer - 2 Units long, Submarine - 3 Units long, Cruiser - 3 Units long,
        Battleship - 4 Units long, and your Aircraft Carrier - 5 Units long. To start the game both
        players begin by placing their ships onto their 10x10 field. You can place your ships either
        horrizontally or vertically.

        Gameplay:

        Each tern a player may fire one shot at the enemy player at any location they choose. If you
        hit one of the enimy players ships, they must announce \"Hit!\". After you hit the ship in
        all of its sections then the ship is \"sunk\" and is no longer in play. After you have sunk
        all of the other players ships then you have won. Likewise if the other player sinks all of
        your ships then you lose. Both players also have a second map to keep track of where they have
        shot before.""")
    input("\nPress Enter to continue. ")
#End#
#Bot Ship Placement#
i = 0
while i < 5:
    x = randint(0,9)#X-Location
    y = randint(0,9)#Y-Location
    z = randint(0,1)#Is Vertical?
    if z == 1:
        if y + bot_ships[i] <= 9:#Checks if there is enough horizontal space.
            checkVerified = True
            for j in range(bot_ships[i]):#Checks if any other ships are present.
                if bot_field[y + j][x] != 0:
                    checkVerified = False
            if checkVerified == True:#Places current ship and increments i only if all previous checks were successful.
                for j in range(bot_ships[i]):
                    bot_field[y + j][x] = i + 1
                i += 1
    if z == 0:
        if x + bot_ships[i] <= 9:#Checks if there is enough vertical space.
            checkVerified = True
            for j in range(bot_ships[i]):#Checks if any other ships are present.
                if bot_field[y][x + j] != 0:
                    checkVerified = False
            if checkVerified == True:#Places current ship and increments i only if all previous checks were successful.
                for j in range(bot_ships[i]):
                    bot_field[y][x + j] = i + 1
                i += 1
#End#
#Player Ship Placement#
i = 0
for i in range(5):
    suc = False
    if i == 0:
        print("You may now begin placing your ships. Ships are placed onto your map using coordinates.")
        print("Remember, your coordinate plane is in the 4th quadrant. That means that your Y-Coordinate")
        print("increases as you go down on the plane, not up.\n")
    while suc == False:
        suc = True
        print("You may now place your", ship_names[i], "which is", player_ships[i], "units long.\n")
        try:
            x = int(input("Please choose your X-Coordinate (1 - 10): ")) - 1
            if x < 0:
                print("Error: You attempted to place a ship using a negative number. This would potentially result in boat wrapping and is not allowed.")
                suc = False
                continue
        except ValueError:
            print("Error: You entered something that was not an acceptable value. Integers only please.")
            suc = False
            continue
        try:
            y = int(input("Please choose your Y-Coordinate (1 - 10): ")) - 1
            if y < 0:
                print("Error: You attempted to place a ship using a negative number. This would potentially result in boat wrapping and is not allowed.")
                suc = False
                continue
        except ValueError:
            print("Error: You entered something that was not an acceptable value. Integers only please.")
            suc = False
            continue
        try:
            z = int(input("Are you placing horizontally(0) or vertically (1)?"))
            if z < 0 or z > 1:
                suc = False
                print("Error: You attempted to place a ship in the 3rd or higher dimension. This is a two dimensional game, please select one of the two.")
                continue
        except ValueError:
            print("Error: You entered something that was not an acceptable value. Integers only please.")
            suc = False
            continue
        if z == 1:
            succ = True
            for j in range(player_ships[i]):#Checks if any other ships are present.
                if suc == False:
                    continue
                try:
                    if player_field[y + j][x] != 0:
                        print("Error: You attempted to place a ship on top of an existing ship. Please choose another spot.")
                        succ = False
                        suc = False
                except IndexError:
                    print("Error: You attempted to place a ship outside of the arena bounds.")
                    suc = False
                    succ = False
            if succ == True:
                    for j in range(player_ships[i]):
                        player_field[y + j][x] = i + 1
        if z == 0:
            succ = True
            for j in range(player_ships[i]):#Checks if any other ships are present.
                if suc == False:
                    continue
                try:
                    if player_field[y][x + j] != 0:
                        print("Error: You attempted to place a ship on top of an existing ship. Please choose another spot.")
                        succ = False
                        suc = False
                except IndexError:
                    print("Error: You attempted to place a ship outside of the arena bounds.")
                    suc = False
                    succ = False
            if succ == True:
                for j in range(player_ships[i]):
                    player_field[y][x + j] = i + 1
    if i != 4:
        printField("a")
#End#
#Begin Gameplay#
gameOver = False
playerWins = False
playerTurn = True
#Bot Values#
originalShot = [0, 0]
previousShot = [0, 0]
firingMode = 0
#End#
while gameOver == False:
    #Begin Player Turn#
    if playerTurn == True:
        printField("b")
        print("It is now your turn.\n")
        try:
            x = int(input("Choose the X-Coordinate (1 - 10) for your shot: ")) - 1
            y = int(input("Choose the Y-Coordinate (1 - 10) for your shot: ")) - 1
        except ValueError:
            print("\nError: You entered something that was not an acceptable value. Integers only please.")
            continue
        if (x < 0 or x > 9) or (y < 0 or y > 9):
            print("\nError: You attempted to fire a shot outside of the arena bounds.")
            continue
        if bot_field[y][x] != 0:#If a ship was hit...
            player_sonar[y][x] = "X"#Updates Players Hit Map
            print("\nYou hit the bots", ship_names[bot_field[y][x] - 1] + ".")#Informs which ship was hit.
            bot_ships[bot_field[y][x] - 1] -= 1#Updates the ship ledger.
            if bot_ships[bot_field[y][x] - 1] == 0:#Checks if the ship was destroyed.
                print("\nYou have destroyed the bots", ship_names[bot_field[y][x] - 1] + ".")
            if emptyShips("a") == True:#Checks if all bot ships have been destroyed and ends the game if they have.
                gameOver = True
                playerWins = True
            bot_field[y][x] = 0#Updates the bots map.
            playerTurn = False
            continue
        else:
            player_sonar[y][x] = "O"
            print("\nYour shot missed.")
            playerTurn = False
            continue
    #End#
    #Begin Bot Turn#
    if playerTurn == False:
        x = randint(0, 9)
        y = randint(0, 9)
        if firingMode == 1:#Fires Up
            x = previousShot[1]
            y = previousShot[0] - 1
            previousShot = [y, x]
        if firingMode == 2:#Fires Down
            x = previousShot[1]
            y = previousShot[0] + 1
            previousShot = [y, x]
        if firingMode == 3:#Fires Left
            x = previousShot[1] - 1
            y = previousShot[0]
            previousShot = [y, x]
        if firingMode == 4:#Fires Right
            x = previousShot[1] + 1
            y = previousShot[0]
            previousShot = [y, x]
        if (x < 0 or x > 9) or (y < 0 or y > 9):#Shot impossible, change firing mode
            firingMode += 1
            previousShot = originalShot
            continue
        if bot_sonar[y][x] == 0: #If the bot hasn't shot here before...
            if firingMode == 0: #This is a whole new ship.
                originalShot = [y, x]
                previousShot = [y, x]
            bot_sonar[y][x] = 1#Register shot.
            if player_field[y][x] != 0:#If A Hit...
                print("\nThe bot fired at ", x + 1,", ", y + 1, " and hit your ", ship_names[player_field[y][x] - 1], ".", sep = "")#Informs the player.
                player_ships[player_field[y][x] - 1] -= 1#Updates ship ledger.
                if firingMode == 0:
                    firingMode = 1#Updates firing mode.
                if player_ships[player_field[y][x] - 1] == 0:#Checks if ship was destroyed
                    print("\nThe bot has destroyed your", ship_names[player_field[y][x] - 1] + ".\n")
                    firingMode = 0
                if emptyShips("b") == True: #Checks if all players ships have been destroyed.
                    gameOver = True #If they have, then end the game.
                player_field[y][x] = 0 #Updates player map.
                playerTurn = True #Informs the swapper that it is now the players turn.
            else: #If the bot missed, then change the firing mode.
                print("\nThe bot fired at ", x + 1,", ", y + 1, " and missed.", sep = "")
                playerTurn = True #Informs the swapper that it is now the players turn.
                if firingMode != 0: #If the bot is already tracking a ship, then migrate to the next mode.
                    firingMode += 1
                    previousShot = originalShot #Resets previousShot values for new firing mode to use.
        else:#If the bot has shot there before, shoot the next spot.
            continue
    #End
#End
if playerWins == True:
    print("\nGame Over: The Player Wins")
else:
    print("\nGame Over: The Bot Wins")
input("\nPress enter to close.")#In terminal the program would close automatically. 
exit()#The input is added to give a break point and the exit command will make the close out work in IDLE.
