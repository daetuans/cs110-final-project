

class Dialogue:
  CHOICE_A = 'A'
  CHOICE_B = 'B'
  CHOICE_C = 'C'
  COUNTER_ONE = 0
  COUNTER_TWO = 1
  COUNTER_THREE = 2
  COUNTER_FOUR = 4
  COUNTER_FIVE = 5
  COUNTER_SIX = 6
  COUNTER_SEVEN = 7
  COUNTER_EIGHT = 8
  COUNTER_NINE = 9
  
  def __init__(self):
    self.__introDialogue = ['WELCOME', 'TO', 'THE DOG']

    self.__fatherIntroduction = ['LUKE', 'I AM...', 'YOUR FATHER',\
                                 'Do you want to:\nA. Bite him\n B. Run away'\
                                 + '\n C. Scream, "DADDY?!"']
    self.__fatherResponse = ['OW!', 'WAIT, COME BACK!', 'WTF?!']
   
    self.__motherIntroduction = ['a', 'b', 'c']
    self.__motherResponse = ['d', 'e', 'f']

    self.__brotherIntroduction = ['a', 'b', 'c']
    self.__brotherResponse = ['d', 'e', 'f']

    self.__remember = [] 
    self.__rememberStages = ['1','2','3', '4', '5', '6', '7', '8', '9']
    self.__introCounter = 0
    self.__fatherCounter = 0

    
 
##The introduction------------------------------------------------------------
  def introduction(self):
    #This automatically comes onto the screen when the game begins, every\
    #time player presses the forward button the counter increments and\
    #extracts the next item in the list. All other buttons are diabled until\
    #the list is empy (might have to create a flag here to do that)
    self.__intro = self.__introDialogue[self.__introCounter]
    self.__introCounter += 1
    return self.__intro

  def getIntroCounter(self):
    return self.__introCounter

  def getLengthOfIntro(self):
    return len(self.__introDialogue)

##Father----------------------------------------------------------------------
  def fatherIntroduction(self):
    #When the user presses the father button all other buttons are diabled\
    #his intro speech comes on the screen. 
    self.__fatherIntro = self.__fatherIntroduction[self.__fatherCounter]
    self.__fatherCounter += 1
    return self.__fatherIntro

  def getFatherCounter(self):
    return self.__fatherCounter

  def getLengthOfFatherIntro(self):
    return len(self.__fatherIntroduction)

  def resetFatherCounter(self):
    self.__fatherCounter = 0
  
  def fatherResponseButton(self, button):
  #At the end of list of the fathers intro will describe the three choices\
  #the user can choose from. The A, B, and C buttons will enable
    if button == Dialogue.CHOICE_A:
      self.__theFatherResponse = self.__fatherResponse[Dialogue.COUNTER_ONE]
      self.addMemory(self.__rememberStages[Dialogue.COUNTER_ONE])
    elif button == Dialogue.CHOICE_B:
      self.__theFatherResponse = self.__fatherResponse[Dialogue.COUNTER_TWO]
      self.addMemory(self.__rememberStages[Dialogue.COUNTER_TWO])
    elif button == Dialogue.CHOICE_C:
      self.__theFatherResponse = self.__fatherResponse[Dialogue.COUNTER_THREE]
      self.addMemory(self.__rememberStages[Dialogue.COUNTER_THREE])
    return self.__theFatherResponse

##Mother----------------------------------------------------------------------
  def motherDialogue(self, motherCounter):
    #same as father
    return self.__motherIntroduction[motherCounter]
  
  def motherResponseButton(self, button):
    if button == Dialogue.CHOICE_A:
      self.__theMotherResponse = self.__motherResponce[Dialogue.COUNTER_ONE]
      self.addMemory(self__rememberStages[COUNTER_FOUR])
    elif button == Dialogue.CHOICE_B:
      self.__theMotherResponse = self.__motherResponse[Dialogue.COUNTER_TWO]
      self.addMemory(self__rememberStages[COUNTER_FIVE])
    elif button == Dialogue.CHOICE_C:
      self.__theMotherResponse = self.__motherResponse[Dialogue.COUNTER_THREE]
      self.addMemory(self__rememberStages[COUNTER_SIX])
    return self.__theMotherResponse

##Brother---------------------------------------------------------------------
  def brotherDialogue(self, motherCounter):
    #same as father
    return self.__brotherIntroduction[brotherCounter]
  
  def brotherResponseButton(self, button):
    if button == Dialogue.CHOICE_A:
      self.__theBrotherResponse = self.__brotherResponse[Dialogue.COUNTER_ONE]
      self.addMemory(self__rememberStages[COUNTER_SEVEN])
    elif button == Dialogue.CHOICE_B:
      self.__theBrotherResponse = self.__brotherResponse[Dialogue.COUNTER_TWO]
      self.addMemory(self__rememberStages[COUNTER_EIGHT])
    elif button == Dialogue.CHOICE_C:
      self.__theBrotherResponse = self.__brotherResponse[Dialogue.COUNTER_THREE]
      self.addMemory(self__rememberStages[COUNTER_NINE])
    return self.__theBrotherResponse

##Remember--------------------------------------------------------------------
  def addMemory(self, memory):
  ##Add a memory to the memory list or add last memory gathered to the\
  ##    beginning of the list
    if memory in self.__remember:
      self.__remember.remove(memory)
      self.__remember.insert(0, memory)
    else:
      self.__remember.append(memory)

  def rememberMonologue(self, rememberCounter):
    #When the user goes to the dropdown menu and selects menu, the memory\
    #will appear in the dialogue box. Every time the user presses forward\
    #the next memory in the lest will appear
    return self.__remember[rememberCounter]


        
        
        
