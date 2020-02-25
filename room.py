class Room():                       #Defines the Room Class to be called and used in the main program
  
  def __init__(self, room_name):    #Initializes the class with variables, names and descriptions
    self.name = room_name
    self.description = None
    self.linked_rooms = {}
    self.character = []
    self.item = []
    
  def set_character(self, new_character):     #Defines the new character and adds it to the list
    self.character.append(new_character)
    
  def get_character(self):                    #Defines how the program will retrieve the character
    return self.character 
  
  def set_description(self, room_description):    #Defines the description for the character
    self.description = room_description
    
  def get_description(self):                  #Defines how the program will retireve the description for the character
    return self.description
    
  def get_name(self):                         #Defines how the character will retrieve the character name
    return self.name
    
  def set_name(self, room_name):              #Defines how the name for the room is set
    self.name = room_name 
  
  def get_item(self):                         #Defines how the program will retrieve the items in the room
    return self.item
    
  def set_item(self, item_name):              #Defines the items in the room
    self.item.append(item_name)
  
  def describe(self):
    print(self.description)
    
  def link_room(self, room_to_link, direction):   #Defines how the rooms are links
    self.linked_rooms[direction] = room_to_link
    
  def get_details(self):                      #Defines how the program retrieves the details of the room and how it is printed on screen
    print(self.name)
    print("-----------------------------------------------------------")
    print(self.description)
    for direction in self.linked_rooms:
      room = self.linked_rooms[direction]
      print("The " + room.get_name() + " is " + direction)
      
  def move(self, direction):                  #Defines how the user will move between rooms
    if direction in self.linked_rooms:
      return self.linked_rooms[direction]
    else:
      print("You can't go that way")          #Runs the following code if the User types in something that isn't a room 
      return self
