from tkinter import *
from tkinter import messagebox
import tkinter
from PIL import ImageTk # type: ignore
from adm import adminClass

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1540x800+0+0")

        # ----------All Images----------
        self.bg_icon = ImageTk.PhotoImage(file="C:/Users/tejas/Downloads/tiles app/wp10701716 (1).png")
        bg = Label(self.root, image=self.bg_icon)
        bg.place(x=0, y=0)

        # login frame
        Login_Frame = Frame(self.root, bg="black")
        Login_Frame.place(x=520, y=150, width=530, height=440)

        title = Label(Login_Frame, text="Admin Login", font=("times new roman", 20, "bold"), bg="black", fg="white")
        title.place(x=180, y=30)

        # labels
        u_name = Label(Login_Frame, text="Username:", font=("times new roman", 20, "bold"), bg="black", fg="white")
        u_name.place(x=60, y=110)
        self.txt_uname = Entry(Login_Frame, font=("times new roman", 15), bg="white")
        self.txt_uname.place(x=60, y=155, width=300)

        password = Label(Login_Frame, text="Password:", font=("times new roman", 20, "bold"), bg="black", fg="white")
        password.place(x=60, y=190)
        self.txt_password = Entry(Login_Frame, font=("times new roman", 15), bg="white", show="*")
        self.txt_password.place(x=60, y=225, width=300)

        # button
        btn = Button(Login_Frame, text="Login", font=("times new roman", 20, "bold"), bg="white", fg="red", command=self.login)
        btn.place(x=215, y=300)

    def validate_password(self, password):
        # Check if password length is at least 8 characters
        if len(password) < 8:
            return False
        return True

    def login(self):
        predefined_username = "tsadmin"  # Predefined username
        predefined_password = "tsadmin2434"  # Predefined password

        if self.txt_uname.get() == predefined_username and self.txt_password.get() == predefined_password:
            # If username and password match, open admin panel
            self.open_admin_panel()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def open_admin_panel(self):
        self.root.destroy()  # Destroy the login window
        root = tkinter.Tk()
        admin_page = adminClass(root)
        root.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = Login_System(root)
    root.mainloop()