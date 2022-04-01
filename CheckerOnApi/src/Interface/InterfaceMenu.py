import json
from tkinter import *


class InterfaceMenu:
    global listOfCgActivated

    def window(self):
        # Creating the window
        master = Tk()

        Cg3090 = StringVar()
        Cg3080Ti = StringVar()
        Cg3080 = StringVar()
        Cg3070Ti = StringVar()
        Cg3070 = StringVar()
        Cg3060Ti = StringVar()

        # Personalization of the window
        master.title("Lancement du Bot")
        master.geometry("480x260")
        master.minsize(480, 360)
        master.config(bg="#DFDFDF")

        # Creating the frames
        frameButtons = Frame(master, bg="#DFDFDF")

        # Add a send button
        Button(frameButtons, text="Lancer le Bot",
               command=lambda: self.lancement(
                   [Cg3090.get(), Cg3080Ti.get(), Cg3080.get(), Cg3070Ti.get(), Cg3070.get(), Cg3060Ti.get()], master),
               font=("Helvetica", 10)).pack(side=BOTTOM)

        # Adding Check button
        Checkbutton(frameButtons, text="RTX3090", font=("Helvetica", 10), variable=Cg3090, onvalue="RTX 3090+NVGFT090_",
                    offvalue="", bg="#DFDFDF").pack(side=BOTTOM)
        Checkbutton(frameButtons, text="RTX3080 Ti", font=("Helvetica", 10), variable=Cg3080Ti, onvalue="RTX 3080 Ti+NVGFT080T_",
                    offvalue="", bg="#DFDFDF").pack(side=BOTTOM)
        Checkbutton(frameButtons, text="RTX3080", font=("Helvetica", 10), variable=Cg3080, onvalue="RTX 3080+NVGFT080_",
                    offvalue="", bg="#DFDFDF").pack(side=BOTTOM)
        Checkbutton(frameButtons, text="RTX3070 Ti", font=("Helvetica", 10), variable=Cg3070Ti, onvalue="RTX 3070 Ti+NVGFT070T_",
                    offvalue="", bg="#DFDFDF").pack(side=BOTTOM)
        Checkbutton(frameButtons, text="RTX3070", font=("Helvetica", 10), variable=Cg3070, onvalue="RTX 3070+NVGFT070_",
                    offvalue="", bg="#DFDFDF").pack(side=BOTTOM)
        Checkbutton(frameButtons, text="RTX3060 Ti", font=("Helvetica", 10), variable=Cg3060Ti, onvalue="RTX 3060 Ti+NVGFT060T_",
                    offvalue="", bg="#DFDFDF").pack(side=BOTTOM)

        # Show the frame
        frameButtons.pack()

        # Show the window (master)
        master.mainloop()

    def lancement(self, listCgAvticated, frame):
        frame.destroy()
        self.listOfCgActivated = listCgAvticated
