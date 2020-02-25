class Character():

    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
    def get_name(self):
        return self.name

    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return False

class Enemy(Character):

  enemies_defeated = 0

  def __init__(self, char_name, char_description):

    super().__init__(char_name, char_description)
    self.weakness = None

  def fight(self, combat_item):
    if combat_item == self.weakness:
      print("You fend " + self.name + " off with the " + combat_item)
      Enemy.enemies_defeated += 1
      return True
    else:
      print(self.name + " has defeated you! Hopefully a new Captain can win the battle and the war...")
      return False

  def set_weakness(self, item_weakness):
    self.weakness = item_weakness

  def get_weakness(self):
    return self.weakness

  def get_defeated(self):
    return Enemy.enemies_defeated

  def set_defeated(self, number_defeated):
    Enemy.enemies_defeated = number_defeated

class Friend(Character):

  def __init__(self, char_name, char_description):

    super().__init__(char_name, char_description)
    self.feeling = None
