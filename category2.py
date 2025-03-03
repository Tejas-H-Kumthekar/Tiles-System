from tkinter import *

from hall import hallClass 
from bedroom import bedroomClass
from kitchen import kitchenClass
from bathroom import bathroomClass
from garden import gardenClass

class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1540x780+0+0")
        self.root.title("TILES SYSTEM")
        self.root.config(bg="white")

        
        self.icon_title=PhotoImage(file="C:\\Users\\tejas\\Downloads\\tiles app\\categorybg.png")
        title=Label(self.root,image=self.icon_title).place(x=0,y=65,height=750,width=2040)
 
        title=Label(self.root,text="Search Tiles",font=("times new roman",40,"bold"),bg="#010c48",fg="white").place(x=0,y=0,relwidth=1)
       
       
        btn_search=Button(self.root,text="Hall Tiles",command=self.hall,font=("times new roman",20,"bold"),bg="lightyellow",fg="black").place(x=40,y=70,height=40,width=250)
        btn_search=Button(self.root,text="Bed Room Tiles",command=self.bedroom,font=("times new roman",20,"bold"),bg="lightyellow",fg="black").place(x=300,y=70,height=40,width=250)
        btn_search=Button(self.root,text="Kitchen Tiles",command=self.kitchen,font=("times new roman",20,"bold"),bg="lightyellow",fg="black").place(x=560,y=70,height=40,width=250)
        btn_search=Button(self.root,text="Bathroom Tiles",command=self.bathroom,font=("times new roman",20,"bold"),bg="lightyellow",fg="black").place(x=820,y=70,height=40,width=250)
        btn_search=Button(self.root,text="Garden Tiles",command=self.garden,font=("times new roman",20,"bold"),bg="lightyellow",fg="black").place(x=1080,y=70,height=40,width=250)
        btn_search=Button(self.root,text="Back",font=("times new roman",20,"bold"),bg="orange",fg="black",command=self.go_back).place(x=1340,y=70,height=40,width=150)


    def hall(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=hallClass(self.new_win)

    def bedroom(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=bedroomClass(self.new_win)

    def kitchen(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=kitchenClass(self.new_win)

    def bathroom(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=bathroomClass(self.new_win)

    def garden(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=gardenClass(self.new_win)

    def go_back(self):
    # Destroy the current category window
        self.root.destroy()



if __name__=="__main__":
    root=Tk()
    obj=categoryClass(root)
    root.mainloop()
