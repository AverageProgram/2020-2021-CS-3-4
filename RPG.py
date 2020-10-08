import random
import time

def printText(sentence):
    for char in sentence:
        print(char, end = '')
        time.sleep(.004)
    print()

items= ["sword","Bow","Potion"]
playerHealth= 20
inventory= []
running = True
while(running == True):
    printText("*** RPG ***")

    name= input("What is your name? >> ")
    time.sleep(1)
    printText( name + ", you are one of the last people alive on this planet.")
    time.sleep(2)
    printText("On January 2nd, 2021, the majority of the human race was wiped out by an unknown force.")
    time.sleep(2)
    printText("It is now your responsibility to find the cause of this and destroy it.")
    time.sleep(2)
    print()
    print()

    #The game begins
    currentRoom= "building"
    while(currentRoom == "building"):
        choice = input("Choose a direction, n, w, s, e (Q to quit)>> ")
        if(choice == "e"):
            printText("You go out of the building through a hole in the wall, you enter the building's courtyard")
            currentRoom = "courtyard"
        else:
            printText("The path is blocked by debris")
    #The player enters the courtyard
    while(currentRoom == "courtyard"):
        item= random.choice(items)
        printText("You found a " + item + " in a bush")
        inventory.append(item)
        time.sleep(1)
        printText("The courtyard looks like it used to have a pond, but it has since dried up, there's an opening in the east side of the building that's obscured so that you can't see what's inside.")
        time.sleep(2)

        #Asks the user where they want to go
        choice2 = input("Choose a direction, n, w, s, e (Q to quit)>> ")
        if(choice2 == "e"):
            printText("You go through the hole in the wall")
            currentRoom = "boss"
        elif(choice2 == "w"):
            printText("Okay, going back inside the building")
            currentRoom = "building"
        else:
            printText("There's no way out from here")

    #The player enters the boss room
    while(currentRoom == "boss"):

        printText("The hole in the wall led to a secluded cave-like area, you can see a cloaked figure in the distance")
        time.sleep(2)
        printText("The cloaked figure comes charging towards you!")
        currentRoom = "fight"
        enemyHealth = 2

    while(currentRoom == "fight"):
        
        

        if(enemyHealth > 0):
            enemyAttack = random.randint(1, 6)
            playerHealth= playerHealth - enemyAttack
            print("The enemy attacked you for " , enemyAttack , " damage!")
            
            
        if(playerHealth <= 0):
            printText("The enemy attacked quickly, and you fell to the ground. I think this is the end.")
            currentRoom= "False"
            

        time.sleep(1)

        playerAttack = 1
        print("You have a " , item, " in your inventory.")
        attackChoice = input("Do you want to attack? (y or n) >> ")
        if(attackChoice == "y"):
            enemyHealth= enemyHealth - playerAttack
            print("You attacked the enemy with your " , item , ", And it took 1 damage!")
            time.sleep(1)

        if(enemyHealth <= 0):
            printText("The cloaked figure fell to the ground.")
            printText("There's no way to bring back the dead, but you somehow know this won't happen again.")
            currentRoom = "false"
            
       
            
        time.sleep(1)

        



