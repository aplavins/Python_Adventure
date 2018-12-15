import random
import time

trap = True
club = True
sword = False
result = True
boss = True
delay = 2

weapons = {
    None: (1, 4),
    'rock': (2, 6),
    'club': (5, 10),
    'sword': (10, 20)
}

item = {
    None: (0),
    'rock': (1),
    'bone': (2),
}

player = {
    'weapon': None,
    'health': 20,
    'item': None
    }

skeleton = {
    'name': 'skeleton',
    'health': 5,
    'attack': (1, 5)
}

ogre = {
    'name': 'ogre',
    'health': 20,
    'attack': (5, 10)
}


def intro():
    print("Intro")
    time.sleep(delay)
    print("Welcome to Python Adventure!")
    time.sleep(delay)
    print("A text-based mini dungeon.")
    time.sleep(delay)
    print("use commands to reach the treasure.")
    time.sleep(delay)
    print("available commands are look, get and use followed by a noun")
    time.sleep(delay)
    room1()


def room1():
    print("You stand in an empty room surrounded by rubble.")
    time.sleep(delay)
    print("Exits are north and west")
    time.sleep(delay)
    while True:
        choice = input("What do you do? : ")
        if choice == "look rubble":
            print("There are many rocks and bricks on the floor.")
            time.sleep(delay)
        if choice == "get rock":
            player['weapon'] = 'rock'
            player['item'] = 'rock'
            print("You pick up a rock!")
            time.sleep(delay)
        elif choice == "north":
            print("You exit north")
            time.sleep(delay)
            room3()
        elif choice == "west":
            print("You exit west")
            time.sleep(delay)
            room2()


def room2():
    print("You are in a dimly lit room.")
    time.sleep(delay)
    global club
    if club is True:
        print("There is something on the floor by your feet.")
        time.sleep(delay)
    print("Exit is east")
    time.sleep(delay)
    while True:
        choice = input("What do you do? : ")
        if choice == "look floor" and club is True:
            print("There is a wooden club on the floor")
            time.sleep(delay)
        elif choice == "look floor" and club is False:
            print("There nothing there...")
            time.sleep(delay)
        if choice == "get club" and club is True:
            player['weapon'] = 'club'
            print("You pick up the club!")
            time.sleep(delay)
            club = False
        elif choice == "get club" and club is False:
            print("You've already picked it up.")
            time.sleep(delay)
        if choice == "east":
            print("You exit east")
            time.sleep(delay)
            room1()


def room3():
    print("The room you are in contains a coffin.")
    time.sleep(delay)
    print("There are bones strewn about the floor.")
    time.sleep(delay)
    print("exits are north and south")
    time.sleep(delay)
    while True:
        choice = input("What do you do? : ")
        if choice == "look coffin":
            print("As you approach the coffin you hear the rattling of bones")
            time.sleep(delay)
            print("The lid of the coffin opens and a sword wielding skeleton emerges!")
            time.sleep(delay)
            battle(skeleton)
            if result is True:
                global sword
                sword = True
                print("The skeleton falls to the ground")
            elif result is False:
                lose()
        if choice == "get sword" and sword is True:
            player['weapon'] = 'sword'
            sword = False
            print("You picked up the sword!")
            time.sleep(delay)
        elif choice == "get sword" and sword is False:
            print("What sword?")
            time.sleep(delay)
        if choice == "get bone":
            player['item'] = 'bone'
            print("You picked up a bone!")
            time.sleep(delay)
        if choice == "north":
            print("You exit north")
            time.sleep(delay)
            room4()
        if choice == "south":
            print("You exit south")
            time.sleep(delay)
            room1()


def room4():
    print("This room is empty.")
    global trap
    if trap is True:
        print("You feel uneasy.")
        time.sleep(delay)
    print("exits are south and west")
    time.sleep(delay)
    while True:
        choice = input("What do you do? : ")
        if choice == "look floor" and trap is True:
            print("The floor of this room looks different than the others.")
            time.sleep(delay)
        elif choice == "look floor" and trap is False:
            print("The trap has been sprung.")
            time.sleep(delay)
            print("It should be safe to pass now.")
            time.sleep(delay)
        if (choice == "use rock" or choice == "use bone") and trap is True:
            print("You toss it into the middle of the room it sets off")
            print("a pressure plate and the floor falls away revealing a large pit")
            trap = False
            time.sleep(delay)
            print("Good thing you weren't standing there!")
            time.sleep(delay)
        if choice == "west" and trap is True:
            print("As you make your way toward the western exit, the stones beneath")
            time.sleep(delay)
            print("your feet begin to give way. You try to regain your footing but")
            time.sleep(delay)
            print("it is already too late. You fall several meters into a pit of spikes.")
            time.sleep(delay)
            print("You spend your last moments wishing you had seen the trap earlier.")
            time.sleep(delay)
            lose()
        elif choice == "west" and trap is False:
            print("You exit west")
            time.sleep(delay)
            room5()
        if choice == "south":
            print("You exit south")
            time.sleep(delay)
            room3()


def room5():
    global boss
    print(boss)
    if boss is True:
        print("You come face to face with a giant Ogre!")
        time.sleep(delay)
    else:
        print("There is a dead ogre in this room.")
        time.sleep(delay)
    print("exits are south and east")
    time.sleep(delay)
    while True:
        choice = input("What do you do? : ")
        if choice == "look ogre" and boss is True:
            print("He looks angry")
            time.sleep(delay)
        elif choice == "look ogre" and boss is False:
            print("He looks dead")
            time.sleep(delay)
        if choice == "use ogre" and boss is True:
            print("He didn't appreciate that.")
            time.sleep(delay)
            battle(ogre)
            if result is True:
                boss = False
                print("The ogre falls to the floor, dead.")
            elif result is False:
                lose()
        elif choice == "use ogre" and boss is False:
            print("The only use he has now is fertilizer")
            time.sleep(delay)
        if choice == "get ogre" and boss is True:
            print("You attack the ogre head on!")
            time.sleep(delay)
            battle(ogre)
            if result is True:
                boss = False
                print("The ogre falls to the floor, dead.")
            elif result is False:
                lose()
        elif choice == "get ogre" and boss is False:
            print("He's far too big for you to carry.")
            time.sleep(delay)
        if choice == "east":
            print("You exit east")
            time.sleep(delay)
            room4()
        if choice == "south" and boss is True:
            print("The ogre blocks your path and attacks!")
            battle(ogre)
            if result is True:
                boss = False
                print("The ogre falls to the floor, dead.")
            elif result is False:
                lose()
        elif choice == "south" and boss is False:
            print("You exit south")
            time.sleep(delay)
            room6()


def room6():
    print("There is a large chest on the floor of this room.")
    time.sleep(delay)
    print("exit is north")
    time.sleep(delay)
    while True:
        choice = input("What do you do? : ")
        if choice == "look chest":
            print("Looks like treasure!")
            time.sleep(delay)
        elif choice == "use chest":
            print("You should probably take the loot out instead of storing your")
            print("belongings here. The ogre is no longer an effective guard.")
            time.sleep(delay)
        elif choice == "get chest":
            print("You fill your pockets and sack to the breaking point")
            print("with mounds and mounds of gold and jewels.")
            time.sleep(delay)
            win()


def battle(enemy):
    print("You are in a fight with a(n) enemy")
    time.sleep(delay)
    print("The battle part isn't finished yet, so just tell me...")
    time.sleep(delay)
    result = bool(input("Did you win? [True/False]: "))
    return(result)

def win():
    print("Congratulations!")
    time.sleep(delay)
    print("You found the treasure!")
    time.sleep(delay)
    print("You Win!")
    time.sleep(20)
    quit()


def lose():
    print("You have died.")
    time.sleep(delay)
    print("Game Over.")
    time.sleep(delay)
    choice = input("Would you like to try again? [y/n] : ")
    if choice is "y":
        room1()
    elif choice is "n":
        quit()

intro()