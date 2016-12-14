from tkinter import *
class Item:
  def __init__(self):
      self.__itemDictionary = {}
      self.__roomOneDialogue = None
      self.__roomTwoDialogue = None
      self.__roomThreeDialogue = None
      self.__numTries = 0
      self.__roomOneAnswer = "dog"
      self.__itemOne = "Random"
      self.__itemTwo = "Picture Frame"
      self.__itemThree = "Toy Car"
      self.__itemFour = "Beaker"
      

  def roomOneDialogue(self):
    self.__roomOneDialogue = "Hello World! You have three tries."
    return self.__roomOneDialogue

  def roomTwoDialogue(self):
    self.__roomTwoDialogue = "Bye World!"
    return self.__roomTwoDialogue

  def roomThreeDialogue(self):
    self.__roomThreeDialogue = "I ran out of ideas"
    return self.__roomThreeDialogue

  def checkAnswer(self, userAnswer):
      self.__numTries = self.__numTries + 1
      if self.__numTries <= 3:
        itemGained=self.guessTheAnswer(userAnswer)
      else:
        messagebox.showwarning(
         'NO MORE TRIES', 
         "You have no more attempts")
        itemGained=False
      if itemGained == True:
          messagebox.showinfo(
           'Item Found',
           "You've found an item")
      elif itemGained == False:
        messagebox.showwarning(
         'NO ITEM GAINED', 
         "You did not find the item")

  def guessTheAnswer(self, entryData):
     while entryData != self.__roomOneAnswer:
       messagebox.showwarning(
         'INCORRECT', 
         "That is not the correct answer, try again")
       itemGained = False
       return itemGained
     if entryData == self.__roomOneAnswer:
         itemGained = True
         return itemGained

class RoomTwo(Item):
  def __init__(self):
    self.__roomTwoAnswer = "human"

  def guessTheAnswer(self, entryData):
     while entryData != self.__roomTwoAnswer:
       messagebox.showwarning(
         'INCORRECT', 
         "That is not the correct answer, try again")
       itemGained = False
       return itemGained
     if entryData == self.__roomTwoAnswer:
         itemGained = True
         return itemGained

class RoomThree(Item):
  def __init__(self):
    self.__roomThreeAnswer = "mind

  def guessTheAnswer(self, entryData):
     while entryData != self.__roomThreeAnswer:
       messagebox.showwarning(
         'INCORRECT', 
         "That is not the correct answer, try again")
       itemGained = False
       return itemGained
     if entryData == self.__roomThreeAnswer:
         itemGained = True
         return itemGained
