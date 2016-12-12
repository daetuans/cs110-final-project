from tkinter import *



class TitleWindow:

    def __init__(self):
        self.__titleScreen = Tk()
        self.__titleScreen.wm_title('')
        self.__userName = None
        self.__titleScreen.minsize(width=750, height=550)
        self.__titleScreen.maxsize(width=750, height=550)
        self.__topFrame = Frame(self.__titleScreen)
        self.__midFrame = Frame(self.__titleScreen)
        self.__botFrame = Frame(self.__titleScreen)
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

        self.__nameEntryLabel = Label(self.__botFrame, text='Please enter' + \
                                      ' your name:',\
                                      font=("Times New Roman", 17))

        self.__nameEntry = Entry(self.__botFrame, width=50)
        self.__nameEntry.bind('<Return>', self.setUserName)
        self.__nameEntryLabel.pack()
        self.__nameEntry.pack()

        self.__enterButton = Button(self.__botFrame, text="Enter", width=10,\
                                    height=2, state=DISABLED)
        self.__enterButton.pack()

        self.__topFrame.pack()
        self.__midFrame.pack()
        self.__botFrame.pack()
        
        mainloop()
    def setUserName(self, event):
        self.__userName = self.__nameEntry.get()
        self.__nameEntry.config(state=DISABLED)
        self.__enterButton.config(state='normal')
        


TitleWindow()
