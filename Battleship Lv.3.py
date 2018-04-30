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

def printField(A): #Special print command for outputting the above arrays.
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

def emptyShips(A): #Self check command which helps determine when the game ends.
    isEmpty = True
    for i in range(5):
        if A == "a":
            if bot_ships[i] != 0:
                isEmpty = False
        if A == "b":
            if player_ships[i] != 0:
                isEmpty = False
    return isEmpty

def hasHit(A): #Checks if a given ship has been hit before.
    hasHit = False
    if A == 1:
        if player_ships[0] < 2:
            hasHit = True;
    elif A == 2:
        if player_ships[1] < 3:
            hasHit = True;
    elif A == 3:
        if player_ships[2] < 3:
            hasHit = True;
    elif A == 4:
        if player_ships[3] < 4:
            hasHit = True;
    elif A == 5:
        if player_ships[4] < 5:
            hasHit = True;
    return hasHit

bot_ships = [2, 3, 3, 4, 5] #Number of units left for each of the bots ships.
player_ships = [2, 3, 3, 4, 5] #Number of units left for each of the players ships.
ship_names = ["Destroyer", "Submarine", "Cruiser", "Battleship", "Aircraft Carrier"] #Names for ship referencing.
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
gameOver = False #Boolean that triggers a game-over
playerWins = False #Boolean used to determine whether or not the player has won the game.
playerTurn = True #Boolean value that tells the if-loops whose turn it is.
#Bot Values#
originalShot = [0, 0] #Integer array value that tells the bot where it first hit the current ship. Used by targeting swapper.
previousShot = [0, 0] #Integer array value that tells the bot where it last shot. 
firingMode = 0 #Tells the bot the current firing behavior to follow.
attack_origin = [[0, 0, 0, 0]] #Intended to keep track of ships currently being attacked with the format of [x-location, y-location, firing-mode, ship-id]
is_hitting = 0 #Used by the bot to keep track of the ship it's currently hitting. If this value changes outside of mode 0 then the previous array should log the ship.
modes_used = [0] #Keeps track of the firing modes used on the current ship.
ship_just_finished = False #Toggles true when a ship is killed. Used to toggle attack_origin override.
#End Bot Values#
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
        if bot_field[y][x] != 0: #If a ship was hit...
            player_sonar[y][x] = "X" #Update the players Hit Map
            print("\nYou hit the bots", ship_names[bot_field[y][x] - 1] + ".") #Informs the player which ship was hit.
            bot_ships[bot_field[y][x] - 1] -= 1 #Update the ship ledger.
            if bot_ships[bot_field[y][x] - 1] == 0: #Check if the ship was destroyed.
                print("\nYou have destroyed the bots", ship_names[bot_field[y][x] - 1] + ".")
            if emptyShips("a") == True: #Check if all of the bots ships have been destroyed and ends the game if they have.
                gameOver = True
                playerWins = True
            bot_field[y][x] = 0 #Update the bots map.
            playerTurn = False
            continue
        else:
            player_sonar[y][x] = "O"
            print("\nYour shot missed.")
            playerTurn = False
            continue
    #End#

    #Add handling for issue: Attacks multiple ships, adding them to the array but in the process of killing the primary ship, a non primary ship is destroyed, but not removed from array.
        
    #Begin bot turn#
    if playerTurn == False:
        #Firing mode 0 - Shoots randomly until ship is found. Values will be overridden if the bot is in a firing mode.
        x = randint(0, 9)
        y = randint(0, 9)
        #################
        if ship_just_finished == True & attack_origin[0][3] != 0: #If this shot is occurring immediately after a ship has been destroyed AND another ship had been found...
            x = attack_origin[0][0] #Override X Value
            y = attack_origin[0][1] #Override Y Value
            modes_used.append(attack_origin[0][2]) #Inform bot that this firing mode was already used.
            while firingMode in modes_used: #Set new random firing mode.
                firingMode = randint(1, 4)
            is_hitting = attack_origin[0][3] #Override ship recognition value.
            originalShot = [y, x] #Override found ship condition values.
            previousShot = [y, x]
            ship_just_finished = False
        else:
            ship_just_finished = False
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
        if (x < 0 or x > 9) or (y < 0 or y > 9):#If shot is impossible, change firing mode.
            while firingMode in modes_used: #Set new random firing mode.
                firingMode = randint(1, 4)
            previousShot = originalShot #Refresh value for the modes above to use.
            continue
        if firingMode != 0 and firingMode not in modes_used: #If modes_used does not contain the current firing mode, add it.
            modes_used.append(firingMode)
        if bot_sonar[y][x] == 0: #If the bot hasn't shot here before...
            if firingMode == 0: #and this is a whole new ship...
                originalShot = [y, x]
                previousShot = [y, x]
            bot_sonar[y][x] = 1 #Register shot.
            if player_field[y][x] != 0: #If the shot hit...
                if is_hitting != player_field[y][x]: #If hitting a new ship...
                    if attack_origin[0][3] == 0 and hasHit(player_field[y][x]) == False: #Note the new ships location and mode the bot was in at the time.
                        attack_origin[0][0] = x
                        attack_origin[0][1] = y
                        attack_origin[0][2] = firingMode
                        attack_origin[0][3] = player_field[y][x]
                    elif hasHit(player_field[y][x]) == False: #Appends array if it isn't empty.
                        attack_origin.append([x, y, firingMode, player_field[y][x]])
                is_hitting = player_field[y][x] 
                print("\nThe bot fired at ", x + 1,", ", y + 1, " and hit your ", ship_names[player_field[y][x] - 1], ".", sep = "")#Inform the player.
                player_ships[player_field[y][x] - 1] -= 1 #Update the ship ledger.
                if firingMode == 0: #Update the firing mode.
                    while firingMode in modes_used: #This allows this loop to start. Loop continues while the firing mode has been used before.

                        firingMode = randint(1, 4) #Note: randint is range inclusive.
                if player_ships[player_field[y][x] - 1] == 0: #Check if the ship was destroyed
                    print("\nThe bot has destroyed your", ship_names[player_field[y][x] - 1] + ".\n")
                    firingMode = 0 #Resets firing mode to 0 to start a new search.
                    modes_used = [0]
                    is_hitting = 0
                    if len(attack_origin) > 1: #The current ship is removed, and the next ship moves up.
                        del attack_origin[0]
                    elif len(attack_origin) == 1: #If this was the last ship...
                        attack_origin = [[0, 0, 0, 0]] #Reset the array.
                    ship_just_finished = True
                if emptyShips("b") == True: #Check if all of the players ships have been destroyed.
                    gameOver = True #If they have, then end the game.
                player_field[y][x] = 0 #Update the players map. Note: The official map is updated last so all previous statements have the necessary information to function without having to hold an extra value.
                playerTurn = True #Informs the turn toggler that it is now the players turn.
            else: #If the bot missed, then change the firing mode.
                print("\nThe bot fired at ", x + 1,", ", y + 1, " and missed.", sep = "")
                playerTurn = True #Informs the swapper that it is now the players turn.
                if firingMode != 0: #If the bot is already tracking a ship, then migrate to the next mode.
                    while firingMode in modes_used:
                        firingMode = randint(1, 4)
                    previousShot = originalShot #Resets previousShot values for new firing mode to use.
        else: #If the bot has shot there before, shoot the next spot. The mode shouldn't change here since it is possible for a ship to still be here even if the bot has shot here before.
            continue
    #End
#End
if playerWins == True:
    print("\nGame Over: The Player Wins")
else:
    print("\nGame Over: The Bot Wins")
input("\nPress enter to close.")#In terminal the program would close automatically, making the game over section un-readable.
exit()#The exit command will make the close out work in IDLE.
