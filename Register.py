class Register:
  def __init__(self, name):
    self.name = str(name)
    self.used = False
  
  def getUsed(self):
    return self.used

  def setUsed(self, used):
    self.used = used

  def toString(self):
    return self.name

REGISTERS = [Register("A"), Register("B"), Register("C"), Register("D"), Register("E"), Register("F"), Register("G"), Register("H")]

def getFreeRegister():
  for register in REGISTERS:
    if not register.getUsed():
      return register

  return None