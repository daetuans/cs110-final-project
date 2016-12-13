from tkinter import *
from classDialogue import Dialogue
from classStatus import Status
import pyglet
from classItem import *

class TitleWindow():

  def __init__(self, master):
    self.__master = master
    self.__master.geometry('750x575')
    self.__master.title(' ')
##    self.__master.wm_iconbitmap('bloodhfinal.ico')
    
    self.__userName = StringVar()
    self.__topFrame = Frame(self.__master)
    self.__midFrame = Frame(self.__master)
    self.__botFrame = Frame(self.__master)
    self.__titleLabel = Label(self.__topFrame,\
                              text='THE DOG',\
                              font=("Times New Roman", 32))
    self.__titleLabel.pack()
    self.__can = Canvas(self.__midFrame, width=300, height=300,\
                        bg='white')
    self.__pic = PhotoImage(file='doghousefinal.gif')
    self.__programImage = self.__can.create_image(150, 150,\
                                                  image=self.__pic)
    self.__can.pack()

    self.__nameEntryLabel = Label(self.__botFrame, text='Enter' + \
                                  ' your name:',\
                                  font=("Times New Roman", 17))

    self.__nameEntry = Entry(self.__botFrame, width=50)
    self.__nameEntry.bind('<Return>', self.setUserName)
    self.__nameEntryLabel.pack()
    self.__nameEntry.pack()

    self.__enterButton = Button(self.__botFrame, text="Enter", width=10,\
                                height=2, command=self.goToMainGUI)
    self.__enterButton.config(state=DISABLED)
    self.__enterButton.pack()

    self.__topFrame.pack()
    self.__midFrame.pack()
    self.__botFrame.pack()
   
  def setUserName(self, event):
    if (self.__nameEntry.get()).isalpha():
      self.__userName.set(self.__nameEntry.get())
      self.__nameEntry.config(state=DISABLED)
      self.__enterButton.config(state='normal')
    else:
      messagebox.showinfo('ERROR','1. INPUT NAME\n'+\
                          '2. PRESS  <ENTER>  TO PROCEED')
      
  def goToMainGUI(self):
    root2=Toplevel(self.__master)
    myGUI=MainGUI(root2)
    filename = self.__nameEntry.get() + str(".txt")
    file = open(filename, "a+")
    file.close()
    foo=pyglet.media.load("creepymusic.wav")
    foo.play()
    
##Main GUI--------------------------------------------------------------------
class MainGUI:
  def __init__(self, master):
    self.__master = master
    self.__master.geometry('750x575')
    #X AND Y WIDTH AND HEIGHT: 750-X, 575-Y    
    self.__master.title((' '*100)+'THE DOG')
##    self.__master.wm_iconbitmap('bloodhfinal.ico')
    
    self.__menu = Menu(self.__master)
    self.__master.config(menu=self.__menu)
    
    self.__subMenu = Menu(self.__menu)
    self.__menu.add_cascade(label='Think . . .', menu=self.__subMenu)

    self.__subMenu.add_command(label="Items", command=self.goToItemGUI)
    self.__subMenu.add_command(label="Status", command=self.goToStatusGUI)
    self.__subMenu.add_separator()
    self.__subMenu.add_command(label="Remember...", command=self.future)
    self.__dialogue = StringVar()
    self.__progress = StringVar()
    self.__classDialogue = Dialogue()
    self.__dialogue.set(self.__classDialogue.introduction())

##Living Room Picture---------------------------------------------------------
    self.__mainRoomCanvas = Canvas(self.__master, height=378, width=490)
    self.__mainRoomPic = PhotoImage(file='rsz_livingRoom2.gif')
    self.__mainRoomScreen =self.__mainRoomCanvas.create_image\
                            (247,189,image=self.__mainRoomPic)
    self.__mainRoomCanvas.place(x=130, y=10)
####Room buttons----------------------------------------------------------------
##    self.__livingRoomButton = Button(self.__master, text="Living Room")
##    self.__livingRoomButton.place(x=55, y=10, width=100, height=50)
##
##    self.__boysRoomButton = Button(self.__master, text="Boy's Room")
##    self.__boysRoomButton.place(x=190, y=10, width=100, height=50)
##
##    self.__kitchenButton = Button(self.__master, text="Kitchen")
##    self.__kitchenButton.place(x=325, y=10, width=100, height=50)
##    
##    self.__adultsRoomButton = Button(self.__master, text="Adults' Room")
##    self.__adultsRoomButton.place(x=460, y=10, width=100, height=50)  
##    
##    self.__secretRoomButton = Button(self.__master, text="?")
##    self.__secretRoomButton.place(x=595, y=10, width=100, height=50)
##
##Family member buttons-------------------------------------------------------
##    self.__fatherButton = Button(self.__master, text="Talk to\n Father",\
##                              command=self.fatherIntro)
##    self.__fatherButton.place(x=640, y=30, width=100, height=75)
    
    self.__fatherButton = Button(self.__master, text="Talk to\n Boy",\
                                 command=self.fatherIntro)
    self.__fatherButton.place(x=640, y=167.4, width=100, height=75)

##    self.__boyButton = Button(self.__master, text="Talk to\n Boy")
##    self.__boyButton.place(x=640, y=295, width=100, height=75)

##Exploration buttons . . . rename-------------------------------------------
    self.__exploreButtonOne = Button(self.__master, text="Explore\n Room",\
                                     command=self.goToRoomOneGUI)
    self.__exploreButtonOne.place(x=10, y=10, width=100, height=75)
    
    self.__exploreButtonTwo = Button(self.__master, text="Explore\n Room")
    self.__exploreButtonTwo.place(x=10, y=111.6, width=100, height=75)
    
    self.__exploreButtonThree = Button(self.__master, text="Explore\n Room")
    self.__exploreButtonThree.place(x=10, y=213.2, width=100, height=75)

##Secret Room-----------------------------------------------------------------        
    self.__secretRoomButton = Button(self.__master, text="?",\
                                     command=self.goToLabGUI)
    self.__secretRoomButton.place(x=10, y=315, width=100, height=75)
    self.__secretRoomButton.config(state=DISABLED)

##Choice buttons--------------------------------------------------------------  
    self.__choiceAButton = Button(self.__master, text='A',\
                                  command=lambda:self.fatherResponse('A'))
    self.__choiceAButton.place(x=20, y=500, height=40, width=60)

    self.__choiceBButton = Button(self.__master, text='B',\
                                  command=lambda:self.fatherResponse('B'))
    self.__choiceBButton.place(x=137.5, y=500, height=40, width=60)

    self.__choiceCButton = Button(self.__master, text='C',\
                                  command=lambda:self.fatherResponse('C'))
    self.__choiceCButton.place(x=245, y=500, height=40, width=60)
    
##Entry Box-------------------------------------------------------------------
    self.__entryBox = Entry(self.__master, width=52)
    self.__entryBox.bind('<Return>')
    self.__entryBox.place(x=353.5, y=502, height=35)
    self.__entryBox.config(state=DISABLED)

##Enter Button----------------------------------------------------------------
    self.__enterButton = Button(self.__master, text='Enter')
    self.__enterButton.place(x=670, y=502, height=35, width=60)
    
##Text Box--------------------------------------------------------------------
    self.__textBox = Label(self.__master, anchor=NW,\
                           bg='white', textvariable = self.__dialogue)
    self.__textBox.place(x=10, y=400, height=87, width=655)

##Progression Button Base-----------------------------------------------------
    self.__forwardButton = Button(self.__master, text='Forward',\
                                        command=self.intro)
    self.__forwardButton.place(x=665, y=400, width=75, height=88)

    self.disableAllButtonsInfinite()


##Functions-------------------------------------------------------------------
  def intro(self):
    if self.__classDialogue.getIntroCounter() <\
       self.__classDialogue.getLengthOfIntro():
      self.__dialogue.set(self.__classDialogue.introduction())
    else:
      self.__dialogue.set(' ')
      self.__fatherButton.config(state='normal')
      self.__forwardButton.destroy()
      self.createForwardButton(self.fatherIntro)

  def createForwardButton(self, theCommand):
    self.__forwardButton = Button(self.__master, text='Forward',\
                                        command=theCommand)
    self.__forwardButton.place(x=665, y=400, width=75, height=88)
    self.__forwardButton.config(state=DISABLED)

  def enableForwardButton(self):
    self.__forwardButton.config(state='normal')

  def disableForwardButton(self):
    self.__forwardButton.config(state=DISABLED)

  def fatherIntro(self):
    self.__fatherButton.config(state=DISABLED)
    self.__forwardButton.config(state='normal')
    if self.__classDialogue.getFatherCounter() <\
       self.__classDialogue.getLengthOfFatherIntro():
      self.__dialogue.set(self.__classDialogue.fatherIntroduction())
    else:
##      self.__dialogue.set(' ')
      self.__forwardButton.destroy()
      self.createForwardButton(self.reset)
      self.enableChoiceButtons()

  def fatherResponse(self, button):
    self.__dialogue.set(self.__classDialogue.fatherResponseButton(button))
    self.disableChoiceButtons()
    self.enableForwardButton()
##    if self.__dialogue.set(' ')==False:
##      self.disableForwardButton()
##    
      
  def reset(self):
    self.__resetCounter=0
    self.__dialogue.set(' ')
    self.__resetCounter+=1
    if self.__resetCounter == 1:
      self.__forwardButton.destroy()
      self.createForwardButton(self.fatherIntro)
      self.__classDialogue.resetFatherCounter()
      self.__fatherButton.config(state='normal')
    
    

  def disableAllButtonsInfinite(self):
    self.__fatherButton.config(state=DISABLED)
##    self.__exploreButtonOne.config(state=DISABLED)
    self.__exploreButtonTwo.config(state=DISABLED)
    self.__exploreButtonThree.config(state=DISABLED)
    self.__choiceAButton.config(state=DISABLED)
    self.__choiceBButton.config(state=DISABLED)
    self.__choiceCButton.config(state=DISABLED)
    self.__enterButton.config(state=DISABLED)

  def enableChoiceButtons(self):
    self.__choiceAButton.config(state='normal')
    self.__choiceBButton.config(state='normal')
    self.__choiceCButton.config(state='normal')

  def disableChoiceButtons(self):
    self.__choiceAButton.config(state=DISABLED)
    self.__choiceBButton.config(state=DISABLED)
    self.__choiceCButton.config(state=DISABLED)    
    
  def future(self):
      self.__dialogue.set('New content coming soon...')
    

##  def displayDialogue(self):
##    return self.__dialogue.set('stuff')
    
  def goToStatusGUI(self):
    root2=Toplevel(self.__master)
    myGUI=StatusGUI(root2)
    

  def goToItemGUI(self):
    root2=Toplevel(self.__master)
    myGUI=ItemsGUI(root2)

  def goToLabGUI(self):
    root2=Toplevel(self.__master)
    myGUI=LabGUI(root2)

  def goToRoomOneGUI(self):
    root2=Toplevel(self.__master)
    myGUI=RoomOneGUI(root2)

  def goToRoomTwoGUI(self):
    root2=Toplevel(self.__master)
    myGUI=RoomTwoGUI(root2)

  def goToRoomThreeGUI(self):
    root2=Toplevel(self.__master)
    myGUI=RoomThreeGUI(root2)
    
##RoomOne---------------------------------------------------------------------
class RoomOneGUI():
  def __init__(self, master):
    self.__master = master
    self.__master.geometry('750x575')
    #X AND Y WIDTH AND HEIGHT: 750-X, 575-Y    
    self.__master.title(' ')
##    self.__master.wm_iconbitmap('bloodhfinal.ico')
    self.__description = StringVar()
    self.__classItem = Item()
    self.__userAnswer = " "
    self.__item = " "

##Living Room Picture---------------------------------------------------------
##    self.__roomOneCanvas = Canvas(self.__master, height=378, width=490)
####    self.__roomOnePic = PhotoImage(file='roomOneFinal.gif')
##    self.__roomOneScreen =self.__roomOneCanvas.create_image\
##                            (247,189,image=self.__roomOnePic)
##    self.__roomOneCanvas.place(x=130, y=10)

##Text Box--------------------------------------------------------------------
    self.__textBox = Label(self.__master, anchor=NW,\
                           bg='white',text=self.__classItem.roomOneDialogue())
    self.__textBox.place(x=47.5, y=400, height=87, width=655)

##Entry Box-------------------------------------------------------------------
    self.__entryBox = Entry(self.__master, width=52)
    self.__entryBox.bind('<Return>', self.setUserAnswer)
    self.__entryBox.place(x=200, y=502, height=35)

##Enter Button----------------------------------------------------------------
    self.__enterButton = Button(self.__master, text='Enter', state=DISABLED, \
                                command=self.checkUserAnswer)
    self.__enterButton.place(x=506.5, y=502, height=35, width=60)

  def setUserAnswer(self, event):
      self.__userAnswer = self.__entryBox.get().lower()
      self.__enterButton['state']="normal"
      self.__entryBox['state']="disabled"

  def checkUserAnswer(self):
    self.__enterButton['state']="disabled"
    self.__entryBox['state']="normal"
    return self.__classItem.checkAnswer(self.__userAnswer)
          
          

##Room Two--------------------------------------------------------------------
class RoomTwoGUI():
  def __init__(self, master):
    self.__master = master
    self.__master.geometry('750x575')
    #X AND Y WIDTH AND HEIGHT: 750-X, 575-Y    
    self.__master.title(' ')
##    self.__master.wm_iconbitmap('bloodhfinal.ico')
    self.__description = StringVar()
    self.__classItem = RoomTwo()
    self.__userAnswer = " "
    self.__item = " "
    

####Living Room Picture---------------------------------------------------------
##    self.__mainRoomCanvas = Canvas(self.__master, height=378, width=490)
####    self.__mainRoomPic = PhotoImage(file='rsz_livingRoom2.gif')
##    self.__mainRoomScreen =self.__mainRoomCanvas.create_image\
##                            (247,189,image=self.__mainRoomPic)
##    self.__mainRoomCanvas.place(x=130, y=10)

##Text Box--------------------------------------------------------------------
    self.__textBox = Label(self.__master, anchor=NW,\
                           bg='white',text=self.__classItem.roomTwoDialogue())
    self.__textBox.place(x=47.5, y=400, height=87, width=655)

##Entry Box-------------------------------------------------------------------
    self.__entryBox = Entry(self.__master, width=52)
    self.__entryBox.bind('<Return>', self.setUserAnswer)
    self.__entryBox.place(x=200, y=502, height=35)

##Enter Button----------------------------------------------------------------
    self.__enterButton = Button(self.__master, text='Enter', state=DISABLED, \
                                command=self.checkUserAnswer)
    self.__enterButton.place(x=506.5, y=502, height=35, width=60)

  def setUserAnswer(self, event):
      self.__userAnswer = self.__entryBox.get().lower()
      self.__enterButton['state']="normal"
      self.__entryBox['state']="disabled"

  def checkUserAnswer(self):
    self.__enterButton['state']="disabled"
    self.__entryBox['state']="normal"
    return self.__classItem.checkAnswer(self.__userAnswer)


##Room Three------------------------------------------------------------------
class RoomThreeGUI():
  def __init__(self, master):
    self.__master = master
    self.__master.geometry('750x575')
    #X AND Y WIDTH AND HEIGHT: 750-X, 575-Y    
    self.__master.title(' ')
##    self.__master.wm_iconbitmap('bloodhfinal.ico')
    self.__description = StringVar()
    self.__classItem = RoomThree()
    self.__userAnswer = " "
    self.__item = " "

####Living Room Picture---------------------------------------------------------
##    self.__mainRoomCanvas = Canvas(self.__master, height=378, width=490)
####    self.__mainRoomPic = PhotoImage(file='rsz_livingRoom2.gif')
##    self.__mainRoomScreen =self.__mainRoomCanvas.create_image\
##                            (247,189,image=self.__mainRoomPic)
##    self.__mainRoomCanvas.place(x=130, y=10)

##Text Box--------------------------------------------------------------------
    self.__textBox = Label(self.__master, anchor=NW,\
                        bg='white',text=self.__classItem.roomThreeDialogue())
    self.__textBox.place(x=47.5, y=400, height=87, width=655)

##Entry Box-------------------------------------------------------------------
    self.__entryBox = Entry(self.__master, width=52)
    self.__entryBox.bind('<Return>')
    self.__entryBox.place(x=200, y=502, height=35)

##Enter Button----------------------------------------------------------------
    self.__enterButton = Button(self.__master, text='Enter')
    self.__enterButton.place(x=506.5, y=502, height=35, width=60)

  def setUserAnswer(self, event):
    self.__userAnswer = self.__entryBox.get().lower()
    self.__enterButton['state']="normal"
    self.__entryBox['state']="disabled"

  def checkUserAnswer(self):
    self.__enterButton['state']="disabled"
    self.__entryBox['state']="normal"
    return self.__classItem.checkAnswer(self.__userAnswer)
  
##Status Page-----------------------------------------------------------------
class StatusGUI():
  def __init__(self, master):
    self.__master = master
    self.__master.protocol('WM_DELETE_WINDOW', self.future)
    self.__master.geometry('750x575')
    self.__master.title((' '*100) +'STATUS')
##    self.__master.wm_iconbitmap('bloodhfinal.ico')

    self.__status = Status()

    self.__menu = Menu(self.__master)
    self.__master.config(menu=self.__menu)

    self.__subMenu = Menu(self.__menu)
    self.__menu.add_cascade(label='Exit mind . . .', menu=self.__subMenu)

    self.__subMenu.add_command(label="Living Room",\
                               command=self.goBack)
##Father Status---------------------------------------------------------------
##    self.__fatherCanvasOne = Canvas(self.__master, height=170, width=245,\
##                                    bg='white')
##    self.__fatherCanvasOne.place(x=5, y=7.5)

    self.__fatherCanvasTwo = Canvas(self.__master, height=170, width=245,\
                                    bg='white')
    self.__fatherCanvasTwo.place(x=5, y=185)
    

##    self.__fatherCanvasThree = Canvas(self.__master, height=170, width=245,\
##                                      bg='white')
##    self.__fatherCanvasThree.place(x=5, y=362.5)

##Mother Status---------------------------------------------------------------
##    self.__motherStatusOne = Canvas(self.__master, height=170, width=240,\
##                                    bg='white')
##    self.__motherStatusOne.place(x=255, y=7.5)

    self.__motherStatusTwo = Canvas(self.__master, height=170, width=240,\
                                    bg='white')
    self.__motherStatusTwo.place(x=255, y=185)

##    self.__motherStatusThree = Canvas(self.__master, height=170, width=240,\
##                                      bg='white')
##    self.__motherStatusThree.place(x=255, y=362.5)
##
##Brother Status--------------------------------------------------------------
##    self.__brotherStatusOne = Canvas(self.__master, height=170, width=240,\
##                                     bg='white')
##    self.__brotherStatusOne.place(x=500, y=7.5)

    self.__brotherStatusTwo = Canvas(self.__master, height=170, width=240,\
                                     bg='white')
    self.__brotherStatusTwo.place(x=500, y=185)

##    self.__brotherStatusThree = Canvas(self.__master, height=170, width=240,\
##                                       bg='white')
##    self.__brotherStatusThree.place(x=500, y=362.5)
##
##Go Back Button--------------------------------------------------------------
  def goBack(self):
    self.__master.destroy()

  def future(self):
    print("New content coming soon...")

##Item Page-------------------------------------------------------------------
class ItemsGUI():
  def __init__(self, master):
    self.__master = master
    self.__master.geometry('750x575')
    self.__master.title((' '*100) +'ITEMS')
##    self.__master.wm_iconbitmap('bloodhfinal.ico')

    self.__menu = Menu(self.__master)
    self.__master.config(menu=self.__menu)

    self.__subMenu = Menu(self.__menu)
    self.__menu.add_cascade(label='Exit mind . . .', menu=self.__subMenu)

    self.__subMenu.add_command(label="Living Room",\
                               command=self.goBack)

##First Item------------------------------------------------------------------
    self.__itemOneName = Label(self.__master, text="name1", bg='white')
    self.__itemOneName.place(x=20, y=45, height=75, width=175)

    self.__itemOneDescription = Label(self.__master, text="description1",\
                                      bg='white', anchor=NW)
    self.__itemOneDescription.place(x=215, y=45, height=125, width=515)

##Second Item-----------------------------------------------------------------
    self.__itemTwoName = Label(self.__master, text='name2', bg='white')
    self.__itemTwoName.place(x=20, y=210, height=75, width=175)

    self.__itemTwoDescription = Label(self.__master, text="description2",\
                                      bg='white', anchor=NW)
    self.__itemTwoDescription.place(x=215, y=210, height=125, width=515)

##Third Item------------------------------------------------------------------
    self.__itemThreeName = Label(self.__master, text='name3', bg='white')
    self.__itemThreeName.place(x=20, y=380, height=75, width=175)

    self.__itemThreeDescription = Label(self.__master, text="description3",\
                                      bg='white', anchor=NW)
    self.__itemThreeDescription.place(x=215, y=380, height=125, width=515)

##Go Back---------------------------------------------------------------------
  def goBack(self):
    self.__master.destroy()

##Lab Page--------------------------------------------------------------------
class LabGUI():
  def __init__(self, master):
    self.__master = master
    self.__master.geometry('750x575')
    self.__master.title((' '*100)+'THE LAB')
##    self.__master.wm_iconbitmap('bloodhfinal.ico')
    self.__master.protocol('WM_DELETE_WINDOW', self.doNothing)
    self.__dialogue = StringVar()

##Menu------------------------------------------------------------------------
    self.__menu = Menu(self.__master)
    self.__master.config(menu=self.__menu)

    self.__subMenu = Menu(self.__menu)
    self.__menu.add_cascade(label='Exit your lab', menu=self.__subMenu)

    self.__subMenu.add_command(label="Living Room",\
                               command=self.youCant)

##Lab Background--------------------------------------------------------------
    self.__labCanvas = Canvas(self.__master, height=575, width=750)
    self.__labPic = PhotoImage(file='evilLabFinal.gif')
    self.__labScreen =self.__labCanvas.create_image\
                            (375,287.5,image=self.__labPic)
    self.__labCanvas.place(x=0, y=0)

##Choice buttons--------------------------------------------------------------  
    self.__choiceAButton = Button(self.__master, text='A')
    self.__choiceAButton.place(x=20, y=500, height=40, width=60)

    self.__choiceBButton = Button(self.__master, text='B')
    self.__choiceBButton.place(x=137.5, y=500, height=40, width=60)

    self.__choiceCButton = Button(self.__master, text='C')
    self.__choiceCButton.place(x=245, y=500, height=40, width=60)
    
##Entry Box-------------------------------------------------------------------
    self.__entryBox = Entry(self.__master, width=52)
    self.__entryBox.bind('<Return>')
    self.__entryBox.place(x=353.5, y=502, height=35)

##Enter Button----------------------------------------------------------------
    self.__enterButton = Button(self.__master, text='Enter')
    self.__enterButton.place(x=670, y=502, height=35, width=60)
    
##Text Box--------------------------------------------------------------------
    self.__textBox = Label(self.__master, anchor=NW,\
                           bg='white', textvariable = self.__dialogue)
    self.__textBox.place(x=10, y=425, height=70, width=655)

##Progression Button----------------------------------------------------------
    self.__forwardButton = Button(self.__master, text="Forward",\
                                  command=self.displayDialogue)
    self.__forwardButton.place(x=665, y=425, width=75, height=70)    

##Sample Functions------------------------------------------------------------
  def youCant(self):
    messagebox.showinfo("It's too late to go back.",\
                        "Finish what you started.")

  def doNothing(self):
    pass

  def displayDialogue(self):
    return self.__dialogue.set('stuff')

 
    


def main():
  root = Tk()
  GUIStart = TitleWindow(root)
  root.mainloop()

if __name__ == '__main__':
  main()
