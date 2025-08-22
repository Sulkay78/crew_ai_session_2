# Chess game to learn inheritence, polymorphism and encapsulation
class chess_peace:
  """Chess game to learn inheritence, polymorphism and encapsulation"""
  def __init__(self, loc, color):
    self.loc = loc
    self.color = color 
    # to make the variable private so no one can access it self.__color = color 
  def move(self):
    # pass 
    print('peace move')
  def eat(self):
    print("eat peace")
  def check_available_loc(self):
    pass

ch = chess_peace(3, 'w')
print(ch.color)