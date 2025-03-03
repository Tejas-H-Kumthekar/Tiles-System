import pymysql # type: ignore
from tkinter import *
from tkinter import messagebox

class feedbackClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Feedback")
        self.root.geometry("1540x800+0+0")
        self.root.config(bg="white")

        self.icon_title = PhotoImage(file="C:\\Users\\tejas\\Downloads\\tiles app\\wp10701716 (1).png")
        title = Label(self.root, image=self.icon_title)
        title.place(x=0, y=0)

        #login frame
        Feed_Frame=Frame(self.root,bg="black")
        Feed_Frame.place(x=550,y=130,width=530,height=440,relwidth=0)

        title=Label(Feed_Frame,text="Feedback",font=("times new roman",20,"bold"),bg="black",fg="orange").place(x=210,y=30)
        #labels
        name=Label(Feed_Frame,text="Username:",font=("times new roman",20,"bold"),bg="black",fg="orange").place(x=60,y=110)
        self.txt_name=Entry(Feed_Frame,font=("times new roman",15),bg="white")
        self.txt_name.place(x=60,y=155,width=300)

        feedback=Label(Feed_Frame,text="Your Feedback:",font=("times new roman",20,"bold"),bg="black",fg="orange").place(x=60,y=190)
        self.txt_feedback=Entry(Feed_Frame,font=("times new roman",15),bg="white")
        self.txt_feedback.place(x=60,y=225,width=300)
        #button
        btn=Button(Feed_Frame,text="Submit",font=("times new roman",20,"bold"),bg="white",fg="orange",command=self.feedback)
        btn.place(x=210,y=310)
        
    def feedback(self):
        if self.txt_uname.get()=="" or self.txt_feedback.get()=="":
            messagebox.showerror("Error","All fields are required!!",parent=self.root)
        else:
                 try:
                      con=pymysql.connect(host="localhost",user="root",password="abc",database="ts")
                      cur=con.cursor()
                      cur.execute("insert into feed2 (username,feedback) values (%s,%s)",
                                (self.txt_name.get(),
                                self.txt_feedback.get()
                                    ) )
                      con.commit()
                      con.close()
                      messagebox.showinfo("Success","Feedback Submitted Successfully!",parent=self.root)
                      
                
                 except Exception as es:
                  messagebox.showerror("Error",f"Error due to: {str(es)} ",parent=self.root)
                 finally:
                        try:
                              if con.is_connected():
                                    cur.close()
                                    con.close()
                        except Exception as e:
                              print(f"Error closing connection: {str(e)}")

if __name__ == "__main__":
    root =Tk()
    obj=feedbackClass(root)
    root.mainloop()       
        