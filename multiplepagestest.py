import tkinter as tk

class Page(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
    def show(self):
        self.lift()

class Page1(Page):
    def __init__(self):
##        self.__broRoomScreen = tk.Tk()
##        self.__broRoomScreen.wm_title("Boy's Room")
##        self.__broRoomScreen.minsize(width=750, height=550)
##        self.__broRoomScreen.maxsize(width=750, height=550)
##        self.__topFrame = tk.Frame(self.__broRoomScreen)
##        self.__midFrame = tk.Frame(self.__broRoomScreen)
##        self.__botFrame = tk.Frame(self.__broRoomScreen)
        Page.__init__(self)
        
        self.__can = tk.Canvas(self, width=600, height=300, bg='white')
        self.__pic = tk.PhotoImage(file='boysroom.gif')
        self.__programImage = self.__can.create_image(301, 151, image=self.__pic)
        self.__can.pack()

        self.__storyText = tk.Label(self, height=5, \
                                        width=60, text="12345678901" +\
                                         "2345678901234567890\n" + \
                                "123456789012345678901234567890\n" + \
                                "123456789012345678901234567890\n" + \
                                "123456789012345678901234567890\n" + \
                                "123456789012345678901234567890")
        self.__storyText.pack()
                                


        self.__optionAButton = tk.Button(self, text="Option A")
        self.__optionBButton = tk.Button(self, text="Option B")
        self.__optionCButton = tk.Button(self, text="Option C")
        self.__optionDButton = tk.Button(self, text="Option D")

        self.__optionAButton.pack(side="left")
        self.__optionBButton.pack(side="left")
        self.__optionCButton.pack(side="left")
        self.__optionDButton.pack(side="left")
        

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

       self.__storyText = tk.Label(self, height=5, \
                                        width=60, text="12345678901" +\
                                         "2345678901234567890\n" + \
                                "123456789012345678901234567890\n" + \
                                "123456789012345678901234567890\n" + \
                                "123456789012345678901234567890\n" + \
                                "123456789012345678901234567890")
       self.__storyText.pack()

       self.__optionAButton = tk.Button(self, text="Option A")
       self.__optionBButton = tk.Button(self, text="Option B")
       self.__optionCButton = tk.Button(self, text="Option C")
       self.__optionDButton = tk.Button(self, text="Option D")

       self.__optionAButton.pack(side="left")
       self.__optionBButton.pack(side="left")
       self.__optionCButton.pack(side="left")
       self.__optionDButton.pack(side="left")                         
       

class Page3(Page):
   def __init__(self):
       Page.__init__(self)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        p1 = Page1()
        p2 = Page2()
        p3 = Page3()

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

##        self.__kitchenButton = tk.Button(self.__topFrame, text="Kitchen")
##        self.__broRoomButton = tk.Button(self.__topFrame, text="Boy's Room")
##        self.__livingRoomButton = tk.Button(self.__topFrame, text="Living Room")
##        self.__secretRoomButton = tk.Button(self.__topFrame, text="Secret Room")
##
##        self.__kitchenButton.pack(side="left")
##        self.__broRoomButton.pack(side="left")
##        self.__livingRoomButton.pack(side="left")
##        self.__secretRoomButton.pack(side="left")

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Boy's Room", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Kitchen", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()
        

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView()
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("750x550")
    root.mainloop()
