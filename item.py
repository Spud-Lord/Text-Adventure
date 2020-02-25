class Item():                       #Defines the Item Class to be called and used in main program
  
  def __init__(self, item_name):    #Initializes the class with variables, names and descriptions
    self.name = item_name
    self.description = None 
    
  def set_name(self, item_name):    #Defines how the item name is set
    self.name = item_name
    
  def get_name(self):               #Defines how the program will retrieve the name of the item
    return self.name
    
  def set_description(self, item_description):      #Defines how the items description is set
    self.description = item_description
    
  def get_description(self):        #Defines how the program will retrieve the description
    return self.description

  def describe(self):               #Defines how the programs prints the item and its description
    print("The " + self.name + " is here - " + self.description)
