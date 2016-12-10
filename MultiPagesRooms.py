import tkinter as tk

class Page(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
    def show(self):
        self.lift()

class Page1(Page):
    def __init__(self):
        Page.__init__(self)
        p2 = Page2()

        self.__titleLabel = tk.Label(self, \
                                          text='The Dog', \
                                           font=("Times New Roman", 32))
        self.__titleLabel.pack()

        self.__can = tk.Canvas(self, width=300, height=300, bg='white')
        self.__pic = tk.PhotoImage(file='testimage.gif')
        self.__programImage = self.__can.create_image(151, 150, image=self.__pic)
        self.__can.pack()

        self.__nameEntryLabel = tk.Label(self, text='Press the button ' + \
                                    'to enter the game', \
                                         font=("Times New Roman", 17))

        self.__startButton = tk.Button(self, text="Start Game", command=p2.lift)
        self.__nameEntryLabel.pack()
        self.__startButton.pack()
    
class Page2(Page):
   def __init__(self):
##       self.__kitchenScreen = tk.Tk()
##       self.__kitchenScreen.wm_title("Boy's Room")
##       self.__kitchenScreen.minsize(width=750, height=550)
##       self.__kitchenScreen.maxsize(width=750, height=550)
##       self.__topFrame = tk.Frame(self.__kitchenScreen)
##       self.__midFrame = tk.Frame(self.__kitchenScreen)
##       self.__botFrame = tk.Frame(self.__kitchenScreen)
       Page.__init__(self)

       self.__can = tk.Canvas(self, width=600, height=300, bg='white')
       self.__pic = tk.PhotoImage(file='kitchen.gif')
       self.__programImage = self.__can.create_image(301, 151, image=self.__pic)
       self.__can.pack()                  
       

class Page3(Page):
   def __init__(self):
       Page.__init__(self)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    


class GameView(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        p1 = Page1()
        p2 = Page2()
        p3 = Page3()
        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        
        ##Room buttons----------------------------------------------------------------
        self.__livingRoomButton = tk.Button(self, text="Living Room")
        self.__livingRoomButton.place(x=55, y=10, width=100, height=50)
        self.__boysRoomButton = tk.Button(buttonframe, text="Boy's Room", command=p3.lift)
        self.__boysRoomButton.place(x=190, y=10, width=100, height=50)
        self.__kitchenButton = tk.Button(buttonframe, text="Kitchen", command=p2.lift)
        self.__kitchenButton.place(x=325, y=10, width=100, height=50)
        
        self.__adultsRoomButton = tk.Button(self, text="Adults' Room")
        self.__adultsRoomButton.place(x=460, y=10, width=100, height=50)  
        
        self.__secretRoomButton = tk.Button(self, text="?")
        self.__secretRoomButton.place(x=595, y=10, width=100, height=50)
    ##Family member buttons-------------------------------------------------------
        self.__boyButton = tk.Button(self, text="Talk to\n Boy")
        self.__boyButton.place(x=660, y=80, width=80, height=50)
        
        self.__motherButton = tk.Button(self, text="Talk to\n Mother")
        self.__motherButton.place(x=660, y=205, width=80, height=50)
        self.__fatherButton = tk.Button(self, text="Talk to\n Father")
        self.__fatherButton.place(x=660, y=330, width=80, height=50)
    ##Exploration buttons . . . rename-------------------------------------------
        self.__exploreButtonOne = tk.Button(self, text="Explore\n Room")
        self.__exploreButtonOne.place(x=10, y=80, width=80, height=50)
        
        self.__exploreButtonTwo = tk.Button(self, text="Explore\n Room")
        self.__exploreButtonTwo.place(x=10, y=205, width=80, height=50)
        
        self.__exploreButtonThree = tk.Button(self, text="Explore\n Room")
        self.__exploreButtonThree.place(x=10, y=330, width=80, height=50)
    ##Choice buttons--------------------------------------------------------------

        self.__choiceAButton = tk.Button(self, text='A')
        self.__choiceAButton.place(x=443.5, y=430, height=40, width=60)
        self.__choiceBButton = tk.Button(self, text='B')
        self.__choiceBButton.place(x=551, y=430, height=40, width=60)
        self.__choiceCButton = tk.Button(self, text='C')
        self.__choiceCButton.place(x=658.5, y=430, height=40, width=60)
        
     
    ##Entry Box-------------------------------------------------------------------
        self.__entryBox = tk.Entry(self, width=52)
        self.__entryBox.bind('<Return>')
        self.__entryBox.place(x=423.5, y=480, height=35)
    ##Text Box--------------------------------------------------------------------
        self.__textBox = tk.Label(self, bg='white', text="Insert dialogue here. . .")
        self.__textBox.place(x=10, y=430, height=87, width=320)
    ##Progression Button----------------------------------------------------------
        self.__forwardButton = tk.Button(self, text="Forward")
        self.__forwardButton.place(x=330, y=430, width=75, height=87)

        p1.show()
        
        

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView()
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("750x550")
    root.mainloop()

