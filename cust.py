from tkinter import *
from tkinter import messagebox
from PIL import ImageTk # type: ignore
import pymysql # type: ignore
from dashboard import IMSClass
from forpass import forg

class customerClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1540x800+0+0")
        self.root.title("Admin SYSTEM")
        self.root.config(bg="white")

        #image bg    
        self.icon_title = ImageTk.PhotoImage(file="C:\\Users\\tejas\\Downloads\\tiles app\\wp10701716 (1).png")
        title = Label(self.root, image=self.icon_title)
        title.place(x=0, y=0, height=800, width=1530)

        ##login frame
        Login_Frame = Frame(self.root, bg="black", bd=10)
        Login_Frame.place(x=500, y=150, width=530, height=440)

        title = Label(Login_Frame, text="Customer Login", font=("times new roman", 20, "bold"), bg="black", fg="white", bd=10)
        title.place(x=0, y=30, relwidth=1)

        ###labels
        u_name = Label(Login_Frame, text="Username:", font=("times new roman", 20, "bold"), bg="black", fg="white")
        u_name.place(x=60, y=110)
        self.txt_uname = Entry(Login_Frame, font=("times new roman", 15), bg="white")
        self.txt_uname.place(x=60, y=155, width=300)

        password = Label(Login_Frame, text="Password:", font=("times new roman", 20, "bold"), bg="black", fg="white")
        password.place(x=60, y=190)
        self.txt_password = Entry(Login_Frame, font=("times new roman", 15), bg="white",show="*")
        self.txt_password.place(x=60, y=225, width=300)

        btn_login = Button(Login_Frame, text="Login", command=self.login, font=("times new roman", 20, "bold"), bg="skyblue", fg="black")
        btn_login.place(x=155, y=300, height=35, width=140)

        btn2 = Button(Login_Frame, text='Forgot Password?', font=("times new roman", 15, "bold"), bg="skyblue", fg="black",command=self.open_for)
        btn2.place(x=350, y=370, height=30, width=160)
        
    def login(self):

        username = self.txt_uname.get()
        password = self.txt_password.get()
        if username == "" or password == "":
            messagebox.showerror("Error", "All Fields Are Required!", parent=self.root)
        else:
            if self.validate_password(password):
                if self.validate_credentials(username, password):
                    messagebox.showinfo("Success", "Login Successful", parent=self.root)
                    self.open_dashboard()
                else:
                    messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
            else:
                messagebox.showerror("Error", "Password should be at least 8 characters long", parent=self.root)


    def validate_password(self, password):
        # Check if password length is at least 8 characters
        if len(password) < 8:
            return False
        return True
   
    def validate_credentials(self, username, password):
        try:
            con = pymysql.connect(host="localhost", user="root", password="abc", database="ts")
            cur = con.cursor()
            # Fetch the user from the data table based on username and password
            cur.execute("SELECT * FROM data2 WHERE name = %s AND password = %s", (username, password))
            user = cur.fetchone()
            
            if user:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error validating credentials: {str(e)}")
            return False
        finally:
            cur.close()
            con.close()

    def open_for(self):
        try:
            # Close the current registration window
            self.root.destroy()
            # Create a new Tkinter instance for the login window
            root = Tk()
            for_window = forg(root)
            # Start the main loop for the login window
            root.mainloop()
        except Exception as e:
            # Show error message if there's an issue opening the login window
            print(f"Error: {str(e)}")

    def open_dashboard(self):
        # Hide the current login window
        self.root.withdraw()
        # Create and open the dashboard window
        dashboard_window = Toplevel(self.root)
        dashboard = IMSClass(dashboard_window)

if __name__ == "__main__":
    root = Tk()
    obj = customerClass(root)
    root.mainloop()