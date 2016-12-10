import tkinter

class brothersRoomWindow:
    def __init__(self):
        self.__broRoomScreen = tkinter.Tk()
        self.__broRoomScreen.wm_title("Boy's Room")
        self.__broRoomScreen.minsize(width=750, height=550)
        self.__broRoomScreen.maxsize(width=750, height=550)
        self.__topFrame = tkinter.Frame(self.__broRoomScreen)
        self.__midFrame = tkinter.Frame(self.__broRoomScreen)
        self.__botFrame = tkinter.Frame(self.__broRoomScreen)

        self.__kitchenButton = tkinter.Button(self.__topFrame, text="Kitchen")
        self.__broRoomButton = tkinter.Button(self.__topFrame, text="Boy's Room")
        self.__livingRoomButton = tkinter.Button(self.__topFrame, text="Living Room")
        self.__secretRoomButton = tkinter.Button(self.__topFrame, text="Secret Room")

        self.__kitchenButton.pack(side="left")
        self.__broRoomButton.pack(side="left")
        self.__livingRoomButton.pack(side="left")
        self.__secretRoomButton.pack(side="left")

        self.__can = tkinter.Canvas(self.__midFrame, width=600, height=300, bg='white')
        self.__pic = tkinter.PhotoImage(file='boysroom.gif')
        self.__programImage = self.__can.create_image(301, 151, image=self.__pic)
        self.__can.pack()

        self.__storyText = tkinter.Label(self.__midFrame, height=5, \
                                        width=60, text="12345678901" +\
                                         "2345678901234567890\n" + \
                                "123456789012345678901234567890\n" + \
                                "123456789012345678901234567890\n" + \
                                "123456789012345678901234567890\n" + \
                                "123456789012345678901234567890")
        self.__storyText.pack()
                                


        self.__optionAButton = tkinter.Button(self.__botFrame, text="Option A")
        self.__optionAButton.grid(row=3,column=1,rowspan=2)

        self.__optionBButton = tkinter.Button(self.__botFrame, text="Option B")
        self.__optionBButton.grid(row=3,column=2,rowspan=2)

        self.__optionCButton = tkinter.Button(self.__botFrame, text="Option C")
        self.__optionCButton.grid(row=5,column=1,rowspan=2)

        self.__optionDButton = tkinter.Button(self.__botFrame, text="Option D")
        self.__optionDButton.grid(row=5,column=2,rowspan=2)
        

        

        self.__topFrame.pack()
        self.__midFrame.pack()
        self.__botFrame.pack()

        

        tkinter.mainloop()

brothersRoomWindow()
