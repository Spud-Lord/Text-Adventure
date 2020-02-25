#Jake Eaton

from room import Room
from character import Character, Enemy
from item import Item
import time                         #Imports requried Programs and Modules
import typing
import os
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"       #Hides the "Welcome to Pygame" Message
from pygame import mixer

def type(string):
  for char in string:
    sys.stdout.write(char)          #Defines what "type" command does
    sys.stdout.flush()
    time.sleep(0.02)

mixer.init()                                    #Initializes Music Player
mixer.music.load("Duel of the Fates.mp3")       #Loads the Music
mixer.music.play(5)                             #Plays Music 5 times

lift = Room("Lift")
lift.set_description("You can go up or down!")      #Sets name and description for Lift

command_center = Room("Command Center")
command_center.set_description("A vast room filled with your minions working to keep your ship working\n")    #Sets name and description for Command Center

hangar = Room("Hangar Bay")
hangar.set_description("A wide bay bustling with pilots and engineers ready to fly out into battle when they are called upon\n")  #Sets name and description for Hangar Bay

engine_room = Room("Engine Room")
engine_room.set_description("The room where your fusion engines are managed\n")   #Sets name and description for Engine Room

communications_center = Room("Communications Center")
communications_center.set_description("All your communication flows through here. You can see everyones communication over the network\n")    #Sets name and description for Communications Center

lift.link_room(command_center, "Top")
lift.link_room(hangar, "Bottom")                          #Links all the rooms to the Lift
lift.link_room(engine_room, "42")
lift.link_room(communications_center, "66")

command_center.link_room(lift, "Back")
hangar.link_room(lift, "Back")                            #Links the Lift to all the rooms
engine_room.link_room(lift, "Back")
communications_center.link_room(lift, "Back")

bob = Character("Bob", "Your micromanager. He will keep watch on your minions\n")
bob.set_conversation("Hello There Sir! All systems functioning normally!\n")      #Sets name, conversation and place for Bob
command_center.set_character(bob)

penny = Character("Penny", "Your Hangar Commander. She gives the orders around here\n")
penny.set_conversation("Hello There Sir! Let me know if you want to deploy fighters!\n")      #Sets name, conversation and place for Penny
hangar.set_character(penny)

terry = Character("Terry", "Your Comms Master. He can read through chatter like its his job\n")
terry.set_conversation("Hello There Sir! No suspicous activity flowing through the network. Yet...\n")     #Sets name, conversation and place for Terry
communications_center.set_character(terry)

clara = Character("Clara", "Your Head Engineer. Not only can she create a cold fusion reactor blindfolded with her hands tied behind her back, she doesn't like tea...\n")
clara.set_conversation("Hello There Sir! I am working to repair the engines now! We got hit pretty bad!\n")     #Sets name, conversation and place for Clara
engine_room.set_character(clara)

soldier = Enemy("FF Soldier", "A Formula Front soldier equipped with a rifle\n")
soldier.set_conversation("Prepare to die scum!\n")             #Sets name, conversation, weakness and place for FF Soldier
soldier.set_weakness("Pistol")
engine_room.set_character(soldier)

swordsman = Enemy("FF Swordsman", "A Formula Front Swordsman wielding a long shining sword\n")
swordsman.set_conversation("Face me and prepare to feel the pain of head landing on the floor!\n")      #Sets name, conversation, weakness and place for FF Swordsman
swordsman.set_weakness("Sword")
communications_center.set_character(swordsman)

cruiser = Enemy("FF Cruiser", "A Formula Front Cruiser that has its guns blazing\n")
cruiser.set_weakness("Infinity's Guns")                   #Sets name, weakness and place for FF Cruiser
command_center.set_character(cruiser)                     #Enemy is in multiple rooms
hangar.set_character(cruiser)

fighters = Enemy("FF Fighters", "A Formula Front Fighter Squadron zooming towards you\n")
fighters.set_weakness("WSC Fighters")                   #Sets name, weakness and place for FF Fighters
command_center.set_character(fighters)                  #Enemy is in multiple rooms
hangar.set_character(fighters)

battleship = Enemy("FF Battleship", "A Formula Front Battleship. Heavy armour. Heavy firepower. Treat with care\n")
battleship.set_weakness("Infinity's Guns")
command_center.set_character(battleship)

destroyer = Enemy("FF Destroyer", "A Formula Front Destroyer. Fast... but not fast enough\n")
destroyer.set_weakness("Infinity's Guns")                   #Sets name, weakness and place for FF Destroyer
engine_room.set_character(destroyer)                        #Enemy is in multiple rooms
communications_center.set_character(destroyer)

gun = Item("Pistol")
gun.set_description("Your trusty pistol. One shot, one kill\n")   #Sets name, description and location for Pistol
command_center.set_item(gun)

sword = Item("Sword")
sword.set_description("It may not be a lightsaber, but it will slice you clean in half\n")    #Sets name, description and location for Sword
lift.set_item(sword)

infinity = Item("Infinity's Guns")
infinity.set_description("The contorls for the guns of the most powerful warship ever created. Use these to destroy any ship attempting to bring you down\n")     #Sets name, description and location for Infinity's Guns
command_center.set_item(infinity)

fighters = Item("WSC Fighters")
fighters.set_description("Command your fighters to attack the enemy as they approach\n")      #Sets name, description and location for WSC Fighters
hangar.set_item(fighters)

current_room = lift                 #Places User in that room for start of program
on_hand = []                        #Empty list containing what the User is able to use in fights

dead = False                        #Identifies the User as not dead

type("Your mission... should you choose to accept it...\n")       #Type calls upon the type() above and places the characters down one by one
print(" ")                                                        #Prints out a new line for the type function
time.sleep(2)                                                     #Pauses Program for that many seconds
type("Fend off the Formula Front from taking Geneva...\n")        #\n moves to a new line
print(" ")
time.sleep(2)
type("Take everything you can")
print(" ")
type("Type 'Take' to take items")
print(" ")
type("Type 'Talk' to talk to friendlies")
print(" ")
type("Type 'Fight' to fight enemies")
print(" ")
type("Type where you want to go from the selection exactly as you see it\n")
print(" ")
time.sleep(5)
type("Now... you are The Captain of the brand new Spacecraft... the WSC Infinity...\n")
print(" ")
time.sleep(2)
type("You must command your crew to victory.\n")
print(" ")
time.sleep(2)
type("Defeat all enemies in your path.\n")
print(" ")
time.sleep(2)
type("You lost your sword recently. You may need that. See if you can find it on your mission\n")
print(" ")
time.sleep(2)
type("The WSC Vengeance has recently disabled the enemies shields.\n")
print(" ")
time.sleep(2)
type("Use your gun turrets and fighters to your advantage and outskill the Formula Front Fleet.\n")
print(" ")
time.sleep(2)
type("Be careful though...\n")
print(" ")
time.sleep(2)
type("Our orbital defences are down and the WSC Home Fleet is crumbling...\n")
print(" ")
time.sleep(2)
type("As the most powerful warship ever... you are our last hope...\n")
print(" ")
time.sleep(2)
type("You must lead the charge with the WSC Home Fleet by your side\n")
print(" ")
time.sleep(2)
type("Wait...\n")
print(" ")
time.sleep(2)
type("Command is moving the Home Fleet further out to crush incoming FF Reinforcements...\n")
print(" ")
time.sleep(2)
type("You're on your own now...\n")
print(" ")
time.sleep(2)
type("Let us go forth and defend Geneva!\n")
print(" ")
time.sleep(2)

while dead == False:                                #While loop to run the main game until the user is dead - Which happens if they win or lose...

    current_room.get_details()                      #Gets the details of the current room the user is up to

    inhabitant = current_room.get_character()       #Gets the characters in the current room the user is in and assigns it to a variable for easy working
    if inhabitant is not None:                      #If there is an inhabitant, the indented code will run
        for person in inhabitant:
            person.describe()                       #Describes the person in the room

    items = current_room.get_item()                 #Gets the current items in the room and assigns them to a variable for easy working
    if items is not None:                           #If there is an item, the indented code will run
        for item in items:
            item.describe()                         #Describes the item

    print(" ")
    command = input("> ")
    if command in ["Top", "Bottom", "42", "66", "Back"]:    #If the command is one of the ones in the list, the user will be moved to the room accordingly
        current_room = current_room.move(command)

    elif command == "Talk":                                 #If the user wants to talk, the indented code will run
        print("Who do you want to talk with? ")
        talker = input()
        found = False                                       #True or False Boolean deciding if there is a person there
        for person in inhabitant:                           #If there is an inhabitant, the following code will run
            if person.get_name() == talker:                 #Gets the name of the Person if they are registered as a talker
                found = True                                #Changes Boolean to True
                person.talk()                               #Makes the person talk
        if not found:                                       #If the person is not there the indented code runs
            print("That person is not here!")

    elif command == "Fight":                                #If the user wants to fight, the indented code will run
        print("Who do you want to fight?")
        fighter = input()                                   #Allows user to input who they want to fight
        there = False                                       #True or False Boolean deciding if there is a fighter there or not
        for person in inhabitant:                           #If there is a person who fights then the following code will run
            if person.get_name() == fighter:
                print("What will you fight with?")
                fight_with = input()                        #Fight with variable allowing user to input what they want to fight with

                if fight_with in on_hand:                   #If what the user wants to fight with is on hand (as determined by list), the indented code will run

                    if person.fight(fight_with) == True:    #If the weapon is the enemies weakness
                        print("You destroy your enemy...\n")
                        current_room.get_character().remove(person)   #Removes the person if they are defeated
                        if person.get_defeated() == 9:      #When all the enemies are defeated, the indented code will run
                            print("INCOMING!\n")
                            time.sleep(2)
                            type("The Infinity has taken critical damage!\n")
                            print("")
                            time.sleep(1)
                            type("The ship is going down!\n")
                            print("")
                            time.sleep(2)
                            type("BRACE FOR IMPACT!\n")
                            print("")
                            time.sleep(3)
                            type("The Infinity crash landed in Lake Geneva... killing all on board...\n")
                            print("")
                            time.sleep(3)
                            type("War has begun...\n")
                            print("")
                            time.sleep(3)
                            type("Prepare...\n")
                            print("")
                            time.sleep(1)
                            type("Coming 2020...")
                            mixer.music.fadeout(3000)      #Any playing music is faded away for 3 seconds
                            dead = True                    #dead Boolean made True

                    else:
                        mixer.music.fadeout(3000)
                        dead = True                       #If the user loses the fight, the dead Boolean is made True

                else:
                    print("You don't have a " + fight_with + "\n")    #If the weapon is not in the list, it prints this
                there = True
        if not there:
            print("That person is not here")              #If the person the user has typed is not there, this code is run


    elif command == "Take":                               #If the user wants to take an item, the indented code is run
        if item is not None:
            print("You take the " +  item.get_name() + " along with you\n")
            on_hand.append(item.get_name())               #Adds the iitem to the on_hand list so that the user can use it in fights
            current_room.get_item().remove(item)          #Removes the item from the room

        else:
            print("There is nothing here to take!\n")     #If there is no item in the room, this code gets printed

    else:
        print("You can't do that!\n")                     #If the user types in something that isn't an option, this code gets printed
