import random
import os
import time



# For Clearing the screen
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')  


#For Inputting values
def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

#This is the menu or start of the game
def gameoption():
    print("""___________________
|     1. Start    |
|     2. Exit     |
___________________""")
    choose = get_integer_input("Choose: ")
    if choose == 1:
        clear_screen()
        gamestart()
    elif choose == 2:
        print("Thanks for Playing")


#This will be for containing options when you play the game
def gamestart():
    print("""___________________
|     1. Zone     |
|     2. Battery  |
|     3. Inventory|
|     4. Quit     |
___________________""")
    choose = get_integer_input("Choose: ")
    if choose == 1:
        clear_screen()
        zonechoose()
    elif choose == 2:
        clear_screen()
        batterycheck()
    elif choose == 3:
        clear_screen()
        inventorycheck()
    elif choose == 4:
        clear_screen()
        quit()
    else:
        print("Please Choose Again!")
        input("Click Enter To Continue")
        clear_screen()
        gamestart()



#This Function will let the user move which zone they'll go to and close that zone once the  user picked it
def zonechoose():
    global battery
    global zone
    global count1
    global count2
    print(f"""        ZONE
___________________
|     |     |     |
|  {list(zone.keys())[0]}  |  {list(zone.keys())[1]}  |  {list(zone.keys())[2]}  |
|     |     |     |
___________________
|     |     |     |
|  {list(zone.keys())[3]}  |  {list(zone.keys())[4]}  |  {list(zone.keys())[5]}  |
|     |     |     |
___________________
|     |     |     |
|  {list(zone.keys())[6]}  |  {list(zone.keys())[7]}  |  {list(zone.keys())[8]}  |
|     |     |     |
___________________""")
    choose = get_integer_input("Zone: ")
    print("")
    if choose in zone:
        z = zone[choose]
        
            
        if z == 1:
            count1 -=1
            battery += 10
            if battery > 100:
                battery = 100
            print(f"+10 Power Cell")
            print(f"Battery: {battery}%")
            print(f"Number of Power Cells: {count1}")
            print("")
            zone[choose] = 3
            
        elif z == 2:
            battery -= 20
            count2 -= 1
            if battery < 0:
                battery = 0
            print(f"-20 Cell Bomb")
            print(f"Battery: {battery}%")
            print(f"Number of Power Cells: {count1}")
            print("")
            zone[choose] = 3
        elif z == 3:
            print("Already Chosen, Try Again!")
            input("Click Enter To Continue")
            clear_screen()
            zonechoose()

    #This will allow once the value from the function return a certain number depending on the conditions, it'll be game over or continue playing
    num = gameover(0)
    if num == 1:
        input("Press Enter to continue...")
        clear_screen()
        gamestart()
    elif num == 2:
        for x in range(3):
            print(".")
            time.sleep(1)
        clear_screen()
        print("""_____________________________
|                           |
|     Congratulations!      |
|         You Won           |
|                           |
_____________________________
|    Thanks For Playing!    |
_____________________________""")
            
    elif num == 3:
        for x in range(3):
            print(".")
            time.sleep(1)
        clear_screen()
        print("""_____________________________
|                           |
|         Game Over!        |
|          You Lost         |
|                           |
_____________________________
|    Thanks For Playing!    |
_____________________________""")
        
    
    
#This is for the user to see the battery
def batterycheck():
    global battery
    print(f"Battery: {battery}%")
    input("Press Enter to continue...")
    clear_screen()
    gamestart()
    
    
#This is for user to see the inventory and use it
def inventorycheck():
    global inventory
    global battery
    print(f"""___________________
|    Inventory    |
-------------------
|     1. {inventory}%      |
___________________""")
    choose = get_integer_input("Choose: ")
    if choose == 1:
        if inventory > 0:
            battery += inventory
            if battery > 100:
                battery = 100
            print(f"+{inventory} Power Cell Acquired")
            inventory = 0
        elif inventory == 0:
            print("Empty Power Cell")
    elif choose == 2:
        print("Nothing Use")
    input("Press Enter to continue...")
    clear_screen()
    gamestart()
        

#This will return a certain number once a certain condition is fulfilled
def gameover(num):
    global count1
    global battery
    global count2
    if count1 == 0 and battery > 0:
        num = 2
        return num
    elif count2 == 0 or battery <= 0:
        num = 3
        return num
    else:
        num = 1
        return num

        

#This will make 3 values in the zone to have battery cells and once it does, the game will start
battery = random.randint(50,75)
inventory = 20
zone = {1 : random.randint(1,2), 2 : random.randint(1,2), 3 : random.randint(1,2), 4 : random.randint(1,2), 5 : random.randint(1,2), 6 : random.randint(1,2), 7 : random.randint(1,2), 8 : random.randint(1,2), 9 : random.randint(1,2)}
count1 = 0
count2 = 0
x = True
while x:
    for i in zone.values():
        number = i
        if number == 1:
            count1 += 1
        else:
            count2 += 1
    if count1 == 3:
        x = False
        gameoption()