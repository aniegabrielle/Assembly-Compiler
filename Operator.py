from Register import *

OPERATORS = ['/','*','-','+','=','==', '<', '>', '&&', '||']

class Operator:
  def __init__(self, operator):
    self.operator = operator
    self.leftRegister = None

  def hasHighestPrecedence(self, otherOperator):
    posThis = OPERATORS.index(self.operator)
    posOther = OPERATORS.index(otherOperator.operator)
    return posThis < posOther

  def getLeftRegister(self):
    return self.leftRegister

  def write(self, leftToken, rightToken):
    lines = ""
    rightRegister = None

    match self.operator:
      case '+':
        if not isinstance(leftToken, Register):
          self.leftRegister = getFreeRegister()
          self.leftRegister.setUsed(True)
          lines  = "MOVE " + self.leftRegister.toString() + ", " + leftToken.toString() + "\n"
        else:
          self.leftRegister = leftToken
        if not isinstance(rightToken, Register):
          rightRegister = getFreeRegister()
          rightRegister.setUsed(True)
          lines += "MOVE " + rightRegister.toString() + ", " + rightToken.toString() + "\n"
        else:
          rightRegister = rightToken
        lines += "ADD " + self.leftRegister.toString() + ", " + rightRegister.toString()
      case '-':
        if not isinstance(leftToken, Register):
          self.leftRegister = getFreeRegister()
          self.leftRegister.setUsed(True)
          lines  = "MOVE " + self.leftRegister.toString() + ", " + leftToken.toString() + "\n"
        else:
          self.leftRegister = leftToken
        if not isinstance(rightToken, Register):
          rightRegister = getFreeRegister()
          rightRegister.setUsed(True)
          lines += "MOVE " + rightRegister.toString() + ", " + rightToken.toString() + "\n"
        else:
          rightRegister = rightToken
        lines += "SUBT " + self.leftRegister.toString() + ", " + rightRegister.toString()
      case '*':
        if not isinstance(leftToken, Register):
          self.leftRegister = getFreeRegister()
          self.leftRegister.setUsed(True)
          lines  = "MOVE " + self.leftRegister.toString() + ", " + leftToken.toString() + "\n"
        else:
          self.leftRegister = leftToken
        if not isinstance(rightToken, Register):
          rightRegister = getFreeRegister()
          rightRegister.setUsed(True)
          lines += "MOVE " + rightRegister.toString() + ", " + rightToken.toString() + "\n"
        else:
          rightRegister = rightToken
        lines += "MULT " + self.leftRegister.toString() + ", " + rightRegister.toString()
      case '/':
        if not isinstance(leftToken, Register):
          self.leftRegister = getFreeRegister()
          self.leftRegister.setUsed(True)
          lines  = "MOVE " + self.leftRegister.toString() + ", " + leftToken.toString() + "\n"
        else:
          self.leftRegister = leftToken
        if not isinstance(rightToken, Register):
          rightRegister = getFreeRegister()
          rightRegister.setUsed(True)
          lines += "MOVE " + rightRegister.toString() + ", " + rightToken.toString() + "\n"
        else:
          rightRegister = rightToken
        lines += "DIV " + self.leftRegister.toString() + ", " + rightRegister.toString()
      case '=':
        if isinstance(rightToken, str):
          lines = "MOVE " + leftToken.toString() + ", " + rightToken
        else:
          lines = "MOVE " + leftToken.toString() + ", " + rightToken.toString()

    return lines