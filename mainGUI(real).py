from tkinter import *

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
    
    self.__motherButton = Button(self.__root, text="Talk to\n Mother")
    self.__motherButton.place(x=660, y=205, width=80, height=50)

    self.__fatherButton = Button(self.__root, text="Talk to\n Father")
    self.__fatherButton.place(x=660, y=330, width=80, height=50)

##Exploration buttons . . . rename-------------------------------------------
    self.__exploreButtonOne = Button(self.__root, text="Explore\n Room")
    self.__exploreButtonOne.place(x=10, y=80, width=80, height=50)
    
    self.__exploreButtonTwo = Button(self.__root, text="Explore\n Room")
    self.__exploreButtonTwo.place(x=10, y=205, width=80, height=50)
    
    self.__exploreButtonThree = Button(self.__root, text="Explore\n Room")
    self.__exploreButtonThree.place(x=10, y=330, width=80, height=50)

##Choice buttons--------------------------------------------------------------
        
    self.__choiceAButton = Button(self.__root, text='A')
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
    self.__textBox = Label(self.__root, bg='white', text="Insert dialogue here. . .")
    self.__textBox.place(x=10, y=430, height=87, width=320)

##Progression Button----------------------------------------------------------
    self.__forwardButton = Button(self.__root, text="Forward")
    self.__forwardButton.place(x=330, y=430, width=75, height=87)

    self.__root.mainloop()

class StatusGUI():
  pass

class ItemGUI():
  pass

class StartPageGUI():
  pass

class LabGUI():
  pass
    

    




    self.__root.mainloop()
  def future(self):
    print("New content coming soon...")


MainGUI()
