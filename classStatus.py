from tkinter import *
from classDialogue import *

class Status:
  def __init__(self):
    self.__colorBlank = 'white'
    self.__colorFill = 'gray'

  def getDefaultColor(self):
    return self.__colorBlank

  def getFillColor(self):
    return self.__colorFill

##def main():
##  s = Status()
##  print(s.getDefaultColor())
##
##main()
    
        
