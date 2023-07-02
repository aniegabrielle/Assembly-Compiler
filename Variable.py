VARIABLES = []

class Variable:
  def __init__(self, name):
    self.name = str(name)
  
  def toString(self):
    return self.name