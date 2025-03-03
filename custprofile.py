from tkinter import *
import pymysql # type: ignore

class profileClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x460+380+150")
        self.root.title("TILES SYSTEM")
        self.root.config(bg="white") 
        
        # Connect to MySQL database
        self.connection = pymysql.connect(host="localhost", user="root", password="abc", database="ts")
        self.cursor = self.connection.cursor()

        self.icon_title = PhotoImage(file="C:\\Users\\tejas\\Downloads\\tiles app\\wp10701716 (1).png")
        title = Label(self.root, image=self.icon_title).place(x=0, y=0)

        title = Label(self.root, text="Customer Profile", font=("times new roman", 40, "bold"), bg="#010c48", fg="white").place(x=0, y=0, relwidth=1)
       
        login_frame = Frame(self.root, bg="black", bd=10, relief=GROOVE)
        login_frame.place(x=30, y=70, width=530, height=420, relwidth=0)
        
        # Fetch all users' information from database
        user_info_list = self.fetch_all_user_info()
        self.display_all_user_info(login_frame, user_info_list)

    def fetch_all_user_info(self):
        # Execute SQL query to fetch all users' information
        sql = "SELECT name, phoneno, email FROM data2"
        self.cursor.execute(sql)
        user_info_list = self.cursor.fetchall()
        return user_info_list

    def display_all_user_info(self, frame, user_info_list):
        y_coordinate = 0
        for user_info in user_info_list:
            name_label = Label(frame, text="Name: " + user_info[0], font=("times new roman", 20, "bold"), bg="black", fg="white").place(x=0, y=y_coordinate)
            contact_label = Label(frame, text="Contact: " + user_info[1], font=("times new roman", 20, "bold"), bg="black", fg="white").place(x=0, y=y_coordinate + 60)
            email_label = Label(frame, text="Email: " + user_info[2], font=("times new roman", 20, "bold"), bg="black", fg="white").place(x=0, y=y_coordinate + 120)
            y_coordinate += 180

if __name__ == "__main__":
    root = Tk()
    obj = profileClass(root)
    root.mainloop()
