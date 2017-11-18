# think of classes like a template-thing
# instructions for the computer
# to set, arrange and modify some data 
# you have set for this super-container-thing
class Dragon:
  
  # this is the "constructor"
  # this function is called automatically
  # when you create a class
  def __init__(self, hp,atk):
    self.health = hp
    self.attack = atk
  
  # functions inside a class
  def is_alive(self):
    if (self.health > 0):
      return True
    else:
      return False

########################################
# to construct your own Dragon object
my_cute_dragon = Dragon(50, 10) 

# to check status on my cute dragon
# we call functions inside the class
if (my_cute_dragon.is_alive()):
  print("my cute dragon is alive yay")
else:
  print("RIP in pieces  ;w;")

########################################
# WHY USE CLASSES 
# abstraction !!
# Like cars. we only need to know you can press the accel pedal and it will move \o/ 
# skips da 4-year degree to learn stuff from petrol refining techniques. make the car super accessible and easy to use for everyone. 

