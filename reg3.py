import re
from tkinter import *
from tkinter import messagebox
import pymysql # type: ignore
from PIL import ImageTk # type: ignore
from cust import customerClass 

class reg:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1540x800+0+0")
        self.root.config(bg="white")

        self.bg_icon = ImageTk.PhotoImage(file="C:\\Users\\tejas\\Downloads\\tiles app\\wp10701716 (1).png")
        bg = Label(self.root, image=self.bg_icon).place(x=0, y=0)

        # Register frame
        frame1 = Frame(self.root, bg="black")
        frame1.place(x=450, y=120, width=700, height=500)

        title = Label(frame1, text="Register Here", font=("times new roman", 20, "bold"), bg="black", fg="orange").place(x=250, y=30)
        # 1st row
        c_name = Label(frame1, text="Name:", font=("times new roman", 20, "bold"), bg="black", fg="orange").place(x=50, y=100)
        self.txt_cname = Entry(frame1, font=("times new roman", 15), bg="white")
        self.txt_cname.place(x=50, y=145, width=250)

        p_no = Label(frame1, text="Phone Number:", font=("times new roman", 20, "bold"), bg="black", fg="orange").place(x=370, y=100)
        self.txt_pno = Entry(frame1, font=("times new roman", 15), bg="white")
        self.txt_pno.place(x=370, y=145, width=250)
        # 2nd row
        e_mail = Label(frame1, text="Email Id:", font=("times new roman", 20, "bold"), bg="black", fg="orange").place(x=50, y=170)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="white")
        self.txt_email.place(x=50, y=215, width=250)

        address = Label(frame1, text="Address:", font=("times new roman", 20, "bold"), bg="black", fg="orange").place(x=370, y=170)
        self.txt_address = Entry(frame1, font=("times new roman", 15), bg="white")
        self.txt_address.place(x=370, y=215, width=250)
        # 3rd row
        password = Label(frame1, text="Password:", font=("times new roman", 20, "bold"), bg="black", fg="orange").place(x=50, y=240)
        self.txt_password = Entry(frame1, font=("times new roman", 15), bg="white", show="*")
        self.txt_password.place(x=50, y=285, width=250)

        c_password = Label(frame1, text="Confirm Password:", font=("times new roman", 20, "bold"), bg="black", fg="orange").place(x=370, y=240)
        self.txt_cpassword = Entry(frame1, font=("times new roman", 15), bg="white", show="*")
        self.txt_cpassword.place(x=370, y=285, width=250)

        btn = Button(frame1, text="Register", font=("times new roman", 20, "bold"), bg="black", fg="orange", command=self.registration)
        btn.place(x=270, y=360)

    
    def validate_email(self, email):
        # Regular expression for email validation
        regex = '^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w+$'
        if re.search(regex, email):
            return True
        else:
            return False

    def validate_phone_number(self, phone_number):
        # Check if the phone number consists only of digits and has 10 digits
        if phone_number.isdigit() and len(phone_number) == 10:
            return True
        else:
            return False

    def validate_password(self, password):
        # Check if password length is at least 6 characters
        if len(password) < 8:
            return False
        return True

    def registration(self):
        if self.txt_cname.get()=="" or self.txt_pno.get()=="" or self.txt_email.get()=="" or self.txt_address.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All Fields Are Required!",parent=self.root)
        elif not self.validate_email(self.txt_email.get()):
            messagebox.showerror("Error", "Invalid Email Address!", parent=self.root)
        elif not self.validate_phone_number(self.txt_pno.get()):
            messagebox.showerror("Error", "Invalid Phone Number!", parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Password & Confirm Password Should be same",parent=self.root)
        elif not self.validate_password(self.txt_password.get()):
            messagebox.showerror("Error", "Password should be at least 8 characters long", parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="abc",database="ts")
                cur=con.cursor()
                cur.execute("select * from data2 where email=%s",self.txt_email.get())
                row=cur.fetchone()

                if row!=None:
                    messagebox.showerror("Error","User already Exist,Please try with another email ",parent=self.root)
                else:
                    cur.execute("INSERT INTO data2 (name, phoneno, email, address, password) VALUES (%s, %s, %s, %s, %s)",
            (self.txt_cname.get(), self.txt_pno.get(), self.txt_email.get(), self.txt_address.get(), self.txt_password.get()))

                    con.commit()
                    con.close()
                    messagebox.showinfo("Success!","Register Successful",parent=self.root)
                    self.open_login_window()  # Open the login window after successful registration
                      # Close the registration window after successful registration
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

    def open_login_window(self):
        try:
            # Close the current registration window
            self.root.destroy()
            # Create a new Tkinter instance for the login window
            root = Tk()
            login_window = customerClass(root)
            # Start the main loop for the login window
            root.mainloop()
        except Exception as e:
            # Show error message if there's an issue opening the login window
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    obj = reg(root)
    root.mainloop()