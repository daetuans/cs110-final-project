import tkinter

class titleWindow:
    def __init__(self):
        self.__titleScreen = tkinter.Tk()
        self.__titleScreen.wm_title('Sample Title')
        self.__userName = None
        self.__titleScreen.minsize(width=750, height=550)
        self.__titleScreen.maxsize(width=750, height=550)
        self.__topFrame = tkinter.Frame(self.__titleScreen)
        self.__midFrame = tkinter.Frame(self.__titleScreen)
        self.__botFrame = tkinter.Frame(self.__titleScreen)

        self.__titleLabel = tkinter.Label(self.__topFrame, \
                                          text='Sample Title', \
                                           font=("Times New Roman", 32))
        self.__titleLabel.pack()

        self.__can = tkinter.Canvas(self.__midFrame, width=300, height=300, bg='white')
        self.__pic = tkinter.PhotoImage(file='testimage.gif')
        self.__programImage = self.__can.create_image(151, 150, image=self.__pic)
        self.__can.pack()

        self.__nameEntryLabel = tkinter.Label(self.__botFrame, text='Please enter' + \
                                    ' your name:', font=("Times New Roman", 17))

        self.__nameEntry = tkinter.Entry(self.__botFrame, width=50)
        self.__nameEntry.bind('<Return>', self.__userName)
        self.__nameEntryLabel.pack()
        self.__nameEntry.pack()









        self.__topFrame.pack()
        self.__midFrame.pack()
        self.__botFrame.pack()

        

        tkinter.mainloop()

titleWindow()
        
        
        
