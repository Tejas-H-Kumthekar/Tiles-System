from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image # type: ignore
import pymysql # type: ignore
import re

class forg:
    def __init__(self,root):
        self.root=root
        self.root.title("Forgot Password")
        self.root.geometry("1540x800+0+0")
        self.root.config(bg="white")

        self.bg=ImageTk.PhotoImage(file="C:/Users/tejas/Downloads/tiles app/wp10701716 (1).png")
        bg=Label(self.root,image=self.bg).place(x=0,y=0)

        #forgotpass frame
        Forgotpass_frame=Frame(self.root,bg="black")
        Forgotpass_frame.place(x=550,y=150,width=530,height=440,relwidth=0)

        title=Label(Forgotpass_frame,text="Forgot  Password?",font=("times new roman",20,"bold"),bg="black",fg="blue").place(x=0,y=30,relwidth=1)
        #labels
        email=Label(Forgotpass_frame,text="Email:",font=("times new roman",20,"bold"),fg="blue",bg="black").place(x=60,y=110)
        self.txt_email=Entry(Forgotpass_frame,font=("times new roman",15),bg="white")
        self.txt_email.place(x=60,y=147,width=300)

        password=Label(Forgotpass_frame,text="New Password:",font=("times new roman",20,"bold"),bg="black",fg="blue").place(x=60,y=175)
        self.txt_password=Entry(Forgotpass_frame,font=("times new roman",15),bg="white",show="*")
        self.txt_password.place(x=60,y=215,width=300)
        
        c_password=Label(Forgotpass_frame,text="Confirm Password:",font=("times new roman",20,"bold"),bg="black",fg="blue").place(x=60,y=245)
        self.txt_cpassword=Entry(Forgotpass_frame,font=("times new roman",15),bg="white",show="*")
        self.txt_cpassword.place(x=60,y=285,width=300)
        #button
        button = Button(Forgotpass_frame,text="Submit",font=("times new roman",20,"bold"),bg="black",fg="blue",command=self.newp)
        button.place(x=210,y=340)

    def validate_email(self, email):
        # Regular expression for email validation
        regex = '^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w+$'
        if re.search(regex, email):
            return True
        else:
            return False
        
    def validate_password(self, password):
        # Check if password length is at least 6 characters
        if len(password) < 8:
            return False
        return True
    
    def newp(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error","All fields are required!!")
        elif not self.validate_password(self.txt_password.get()):
            messagebox.showerror("Error", "Password should be at least 8 characters long", parent=self.root)
        else:
            try:
                      con=pymysql.connect(host="localhost",user="root",password="abc",database="ts")
                      cur=con.cursor()
                      cur.execute("insert into forget2 (email,newpass) values (%s,%s)",
                                (self.txt_email.get(),
                                self.txt_password.get()
                                    ) )
                      con.commit()
                      con.close()
                      messagebox.showinfo("Success","Password Reset Successfull!",parent=self.root)
                      
                
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
    obj=forg(root)
    root.mainloop() 