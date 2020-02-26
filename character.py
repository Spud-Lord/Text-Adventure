class Character():                                      #Defines the Character Class to be called and used in main program

    def __init__(self, char_name, char_description):    #Initializes the class with variables, names and descriptions
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def get_name(self):                                 #Defines how the program will retrieve the name of the Character
        return self.name

    def describe(self):                                 #Defines how the program will tell the user who is in the room and how to give the description of the Character
        print(self.name + " is here!")
        print(self.description)

    def set_conversation(self, conversation):           #Gives the conversation a variable name and tells the program how to set the pre-keyed in conversation speech
        self.conversation = conversation

    def talk(self):                                     #Defines how the user will interact with the Character
        if self.conversation is not None:
            print(self.name + " says: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    def fight(self, combat_item):                       #Defines what will happen if the user tries to fight with a friendly
        print(self.name + " doesn't want to fight with you")
        return False

class Enemy(Character):                                 #Defines the Enemy Class as a derivitive of the Character Class to be called and used in the main program

  enemies_defeated = 0                                  #Sets Variable as 0

  def __init__(self, char_name, char_description):      #Initializes the Class with variables, names and descriptions

    super().__init__(char_name, char_description)       #Initializes the Class with the Super Element
    self.weakness = None                                #Sets the weakness of all characters to be nothing

  def fight(self, combat_item):                         #Defines how the program will run if a user wants to fight with a character
    if combat_item == self.weakness:                    #If the item the user has chosen is the same as the weakness of the Enemy, the indented code runs
      print("You fend " + self.name + " off with the " + combat_item)
      Enemy.enemies_defeated += 1                       #Adds 1 to the Enemies Defeated variable
      return True
    else:                                               #If the user loses the fight, the indented code runs
      print(self.name + " has defeated you! Hopefully a new Captain can win the battle and the war...")
      return False

  def set_weakness(self, item_weakness):                #Defines how the program will set the weakness of the Enemies
    self.weakness = item_weakness

  def get_weakness(self):                               #Defines how the program will retrieve the weakness of the Enemies
    return self.weakness

  def get_defeated(self):                               #Defines how the program will retrieve the defeated code for the Enemy
    return Enemy.enemies_defeated

  def set_defeated(self, number_defeated):              #Defines how the program will set the Enemy state to be defeated
    Enemy.enemies_defeated = number_defeated
