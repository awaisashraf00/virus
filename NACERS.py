import os
from tkinter import *

def click():
    os.system("shutdown /s /t 1")

window = Tk()


label = Label(window,
              font=('arial',30,'italic'),
              fg="white",bg='black',
              text="NACERS",
              relief="sunken",
               bd =10,
              )
label.place(x=100,y=100)
window.geometry("400x600")
window.title("NACERS")
window.config(background="black")


button = Button(window,
                text=" PLAY",
                command = click,
                relief="raised",
                bd=10,

                )
button.place(x=170,y=200)
window.mainloop()
