from tkinter import *
import classDialogue
brotherCounter = 0
motherCounter = 0
fatherCounter = 0
introCounter = 0
class MainGUI():
  def __init__(self):
    self.__root = Tk()
    self.__root.geometry('750x550')
    #X AND Y LENGTHS AND HEIGHT: 750-X, 550-Y
    
    self.__root.title('THE DOG')
    self.__menu = Menu(self.__root)
    self.__root.config(menu=self.__menu)
    self.__subMenu = Menu(self.__menu)
    self.__menu.add_cascade(label='Menu', menu=self.__subMenu)
    self.__subMenu.add_command(label="Items", command=self.future)
    self.__subMenu.add_command(label="Status", command=self.future)
    self.__subMenu.add_separator()
    self.__subMenu.add_command(label="Remember...", command=self.future)

##    self.__label = Label(self.__root, bg="gray")
##    self.__label.place(x=0, y=0, height=550, width=750)

##Room buttons----------------------------------------------------------------
    self.__livingRoomButton = Button(self.__root, text="Living Room")
    self.__livingRoomButton.place(x=55, y=10, width=100, height=50)
    self.__boysRoomButton = Button(self.__root, text="Boy's Room")
    self.__boysRoomButton.place(x=190, y=10, width=100, height=50)
    self.__kitchenButton = Button(self.__root, text="Kitchen")
    self.__kitchenButton.place(x=325, y=10, width=100, height=50)
    
    self.__adultsRoomButton = Button(self.__root, text="Adults' Room")
    self.__adultsRoomButton.place(x=460, y=10, width=100, height=50)  
    
    self.__secretRoomButton = Button(self.__root, text="?")
    self.__secretRoomButton.place(x=595, y=10, width=100, height=50)
##Family member buttons-------------------------------------------------------
    self.__boyButton = Button(self.__root, text="Talk to\n Boy")
    self.__boyButton.place(x=660, y=80, width=80, height=50)
    self.__boyButton.bind("<Button-1>", self.getBrotherResponse)
    self.__motherButton = Button(self.__root, text="Talk to\n Mother")
    self.__motherButton.place(x=660, y=205, width=80, height=50)
    self.__motherButton.bind("<Button-1>", self.getMotherResponse)
    self.__fatherButton = Button(self.__root, text="Talk to\n Father")
    self.__fatherButton.place(x=660, y=330, width=80, height=50)
    self.__fatherButton.bind("<Button-1>", self.getFatherResponse)
##Exploration buttons . . . rename-------------------------------------------
    self.__exploreButtonOne = Button(self.__root, text="Explore\n Room")
    self.__exploreButtonOne.place(x=10, y=80, width=80, height=50)
    
    self.__exploreButtonTwo = Button(self.__root, text="Explore\n Room")
    self.__exploreButtonTwo.place(x=10, y=205, width=80, height=50)
    
    self.__exploreButtonThree = Button(self.__root, text="Explore\n Room")
    self.__exploreButtonThree.place(x=10, y=330, width=80, height=50)
##
##Choice buttons--------------------------------------------------------------
        
    self.__choiceAButton = Button(self.__root, text='A', command=self.choiceA)
    self.__choiceAButton.place(x=443.5, y=430, height=40, width=60)
    self.__choiceBButton = Button(self.__root, text='B')
    self.__choiceBButton.place(x=551, y=430, height=40, width=60)
    self.__choiceCButton = Button(self.__root, text='C')
    self.__choiceCButton.place(x=658.5, y=430, height=40, width=60)
    
 
##Entry Box-------------------------------------------------------------------
    self.__entryBox = Entry(self.__root, width=52)
    self.__entryBox.bind('<Return>')
    self.__entryBox.place(x=423.5, y=480, height=35)
##Text Box--------------------------------------------------------------------
    self.__textToDisplay = ""
    self.__textBox = Label(self.__root, bg='white', text=self.__textToDisplay)
    self.__textBox.place(x=10, y=430, height=87, width=320)
##Progression Button----------------------------------------------------------
    self.__forwardButton = Button(self.__root, text="Forward")
    self.__forwardButton.bind("<Button-1>", self.getIntroduction)
    self.__forwardButton.place(x=330, y=430, width=75, height=87)

  
    
    
    

      
      
   
   


    self.__root.mainloop()
  ##Controller Functions--------------------------------------------------------
  def getIntroduction(self, event):
    global introCounter
    if introCounter >= 3:
      self.__textToDisplay = Dialogue.introduction(introCounter)
      introCounter = introCounter + 1
    else:
      introCounter = 0

  
  def getFatherResponse(self, event):
    self.getConversationStatus("Father")
    self.__boyButton['state'] = "disabled"
    self.__motherButton['state'] = "disabled"
    global fatherCounter
    if fatherCounter >= 3:
      self.__textToDisplay = Dialogue.fatherDialogue(fatherCounter)
      fatherCounter = fatherCounter + 1
    else:
      fatherCounter = 0
      self.__boyButton['state'] = "normal"
      self.__motherButton['state'] = "normal"

  
  def getMotherResponse(self, event):
    self.getConversationStatus("Mother")
    self.__boyButton['state'] = "disabled"
    self.__fatherButton['state'] = "disabled"
    global motherCounter
    if motherCounter >= 3:
      self.__textToDisplay = Dialogue.motherDialogue(motherCounter)
      motherCounter = motherCounter + 1
    else:
      motherCounter = 0
      self.__boyButton['state'] = "normal"
      self.__fatherButton['state'] = "normal"

  
  def getBrotherResponse(self, event):
    self.getConversationStatus("Brother")
    self.__fatherButton['state'] = "disabled"
    self.__motherButton['state'] = "disabled"
    global brotherCounter
    if brotherCounter >= 3:
      self.__textToDisplay = Dialogue.brotherDialogue(brotherCounter)
      brotherCounter = brotherCounter + 1
    else:
      brotherCounter = 0
      self.__fatherButton['state'] = "normal"
      self.__motherButton['state'] = "normal"

  def setConversationStatus(self, status):
    if status == "Father":
      conversationStatus = "Father"
    if status == "Brother":
     conversationStatus = "Brother"
    if status == "Mother":
      conversationStatus = "Mother"
    return conversationStatus

  def getConversationStatus(self, status):
    return self.setConversationStatus(status)
    

  def choiceA(self, event):
    choice = 'A'
    if self.getConversationStatus("Father") == "Father":
      self.__textToDisplay = Dialogue.fatherResponseButton(choice)
    if self.getConversationStatus("Mother") == "Mother":
      self.__textToDisplay = Dialogue.motherResponseButton(choice)
    if self.getConversationStatus("Brother") == "Mother":
      self.__textToDisplay = Dialogue.motherResponseButton(choice)
    
  def choiceB(self, event):
    choice = 'B'
    if self.getConversationStatus("Father") == "Father":
      self.__textToDisplay = Dialogue.fatherResponseButton(choice)
    if self.getConversationStatus("Mother") == "Mother":
      self.__textToDisplay = Dialogue.motherResponseButton(choice)
    if self.getConversationStatus("Brother") == "Mother":
      self.__textToDisplay = Dialogue.motherResponseButton(choice)

  def choiceC(self, event):
    choice = 'C'
    if self.getConversationStatus("Father") == "Father":
      self.__textToDisplay = Dialogue.fatherResponseButton(choice)
    if self.getConversationStatus("Mother") == "Mother":
      self.__textToDisplay = Dialogue.motherResponseButton(choice)
    if self.getConversationStatus("Brother") == "Mother":
      self.__textToDisplay = Dialogue.motherResponseButton(choice)

  def future(self):
    print("New content coming soon...")

MainGUI()
