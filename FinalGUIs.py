from tkinter import *
from classDialogue import Dialogue


class TitleWindow():

  def __init__(self, master):
    self.__master = master
    self.__master.geometry('750x550')
    self.__master.title(' ')
    
    self.__userName = None
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
      self.__userName = self.__nameEntry.get()
      self.__nameEntry.config(state=DISABLED)
      self.__enterButton.config(state='normal')
    else:
      messagebox.showinfo('ERROR','1. INPUT NAME\n'+\
                          '2. PRESS  <ENTER>  TO PROCEED')
      


  def goToMainGUI(self):
    root2=Toplevel(self.__master)
    myGUI=MainGUI(root2)
    


class MainGUI:
  def __init__(self, master):
    self.__master = master
    self.__master.geometry('750x550')
    #X AND Y LENGTHS AND HEIGHT: 750-X, 550-Y    
    self.__master.title((' '*100)+'THE DOG')
    self.__menu = Menu(self.__master)
    self.__master.config(menu=self.__menu)
    self.__dialogue = StringVar()
    
   

    self.__subMenu = Menu(self.__menu)
    self.__menu.add_cascade(label='Think . . .', menu=self.__subMenu)

    self.__subMenu.add_command(label="Items", command=self.goToItemGUI)
    self.__subMenu.add_command(label="Status", command=self.goToStatusGUI)
    self.__subMenu.add_separator()
    self.__subMenu.add_command(label="Remember...", command=self.future)

##Living Room Picture---------------------------------------------------------
    self.__mainRoomCanvas = Canvas(self.__master, height=378, width=490,\
                                     bg='white')
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
    self.__boyButton = Button(self.__master, text="Talk to\n Boy")
    self.__boyButton.place(x=640, y=30, width=100, height=75)
    
    self.__motherButton = Button(self.__master, text="Talk to\n Mother")
    self.__motherButton.place(x=640, y=167.4, width=100, height=75)

    self.__fatherButton = Button(self.__master, text="Talk to\n Father")
    self.__fatherButton.place(x=640, y=295, width=100, height=75)

##Exploration buttons . . . rename-------------------------------------------
    self.__exploreButtonOne = Button(self.__master, text="Explore\n Room",\
                                     command=self.future)
    self.__exploreButtonOne.place(x=10, y=10, width=100, height=75)
    
    self.__exploreButtonTwo = Button(self.__master, text="Explore\n Room")
    self.__exploreButtonTwo.place(x=10, y=111.6, width=100, height=75)
    
    self.__exploreButtonThree = Button(self.__master, text="Explore\n Room")
    self.__exploreButtonThree.place(x=10, y=213.2, width=100, height=75)

##Secret Room-----------------------------------------------------------------        
    self.__secretRoomButton = Button(self.__master, text="?")
    self.__secretRoomButton.place(x=10, y=315, width=100, height=75)

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
    self.__textBox.place(x=10, y=400, height=87, width=655)

##Progression Button----------------------------------------------------------
    self.__forwardButton = Button(self.__master, text="Forward",\
                                  command=self.displayDialogue)
    self.__forwardButton.place(x=665, y=400, width=75, height=88)

##Sample Function-------------------------------------------------------------
  def future(self):
    print("New content coming soon...")

  def displayDialogue(self):
    return self.__dialogue.set('booty')
    
  def goToStatusGUI(self):
    root2=Toplevel(self.__master)
    myGUI=StatusGUI(root2)
    

  def goToItemGUI(self):
    root2=Toplevel(self.__master)
    myGUI=ItemsGUI(root2)
    
##Status Page-----------------------------------------------------------------
class StatusGUI():
  def __init__(self, master):
    self.__master = master
    self.__master.geometry('750x550')
    self.__master.title((' '*100) +'STATUS')

    self.__menu = Menu(self.__master)
    self.__master.config(menu=self.__menu)

    self.__subMenu = Menu(self.__menu)
    self.__menu.add_cascade(label='Exit mind . . .', menu=self.__subMenu)

    self.__subMenu.add_command(label="Living Room",\
                               command=self.goBack)
##Father Status---------------------------------------------------------------
    self.__fatherCanvasOne = Canvas(self.__master, height=170, width=245,\
                                    bg='white')
    self.__fatherCanvasOne.place(x=5, y=7.5)

    self.__fatherCanvasTwo = Canvas(self.__master, height=170, width=245,\
                                    bg='white')
    self.__fatherCanvasTwo.place(x=5, y=185)
    

    self.__fatherCanvasThree = Canvas(self.__master, height=170, width=245,\
                                      bg='white')
    self.__fatherCanvasThree.place(x=5, y=362.5)

##Mother Status---------------------------------------------------------------
    self.__motherStatusOne = Canvas(self.__master, height=170, width=240,\
                                    bg='white')
    self.__motherStatusOne.place(x=255, y=7.5)

    self.__motherStatusTwo = Canvas(self.__master, height=170, width=240,\
                                    bg='white')
    self.__motherStatusTwo.place(x=255, y=185)

    self.__motherStatusThree = Canvas(self.__master, height=170, width=240,\
                                      bg='white')
    self.__motherStatusThree.place(x=255, y=362.5)

##Brother Status--------------------------------------------------------------
    self.__brotherStatusOne = Canvas(self.__master, height=170, width=240,\
                                     bg='white')
    self.__brotherStatusOne.place(x=500, y=7.5)

    self.__brotherStatusTwo = Canvas(self.__master, height=170, width=240,\
                                     bg='white')
    self.__brotherStatusTwo.place(x=500, y=185)

    self.__brotherStatusThree = Canvas(self.__master, height=170, width=240,\
                                       bg='white')
    self.__brotherStatusThree.place(x=500, y=362.5)

##Go Back Button--------------------------------------------------------------
  def goBack(self):
    self.__master.destroy()
##Item Page-------------------------------------------------------------------
class ItemsGUI():
  def __init__(self, master):
    self.__master = master
    self.__master.geometry('750x550')
    self.__master.title((' '*100) +'ITEMS')

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
  pass
    


def main():
  root = Tk()
  GUIStart = TitleWindow(root)
  root.mainloop()

if __name__ == '__main__':
  main()
