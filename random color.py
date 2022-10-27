from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
root=Tk()
root.geometry("600x500")
root.title("🥳😰color game wow🥰😱")
label2=Label(root, text="hiing", fg="grey", font=("times",32))
label2.place(relx=0.5, rely=0.1, anchor=CENTER)


class Game():
    def __init__(self):
        self.__score=0
    def updategame(self):
        self.color=["red","orange","yellow","green","blue","purple","pink"]
        self.colortext=["red","orange","yellow","green","blue","purple","pink"]
        self.randomcolor=random.randint(0,6)
        self.randomcolortext=random.randint(0,6)
        label2["text"]=self.colortext[self.randomcolortext]
        label2["fg"]=self.color[self.randomcolor] 
object1=Game() 
button1=Button(root,text="start",command=object1.updategame)
button1.place(relx=0.8, rely=0.5, anchor=CENTER)       

        
        



root.mainloop()