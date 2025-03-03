from tkinter import *
from PIL import Image, ImageTk # type: ignore
from adminlog import Login_System
from homee import homeClass
from category2 import categoryClass
from aboutos import AboutPage
from feed import feedbackClass
from cart import ViewCart
from custprofile import profileClass
import time

class IMSClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1540x780+0+0")
        self.root.title("TILES SYSTEM")
        self.root.config(bg="white")
        self.current_page = None 
        self.admin_window = None
        self.home_instance = None
        self.category_instance = None
        self.about_instance = None
        self.profile_instance = None
        self.viewcart_instance = None
        self.feedback_instance = None
        self.home_window = None
        # Initialize logged_in status
        self.logged_in = True  # Set to True initially or based on login status
        #self.current_user = None  # Track current user
        self.cart_items = []  # List to store items in the cart
        self.current_page = None  # Attribute to track the current page
        self.initialize_ui()  
        # Check if user is already logged in
        #self.check_login_status()
    
    def on_closing(self):
        # Exit the home window only if the user confirms
            """ if messagebox.askokcancel("Quit", "Do you want to quit?", parent=self.root):
                # Destroy the home window"""
            self.root.destroy()

    def open_page(self, page_instance):
        # Check if there are any open pages
        if self.current_page:
            # If the page being closed is the last open page
            if self.current_page == page_instance:
                return  # Hide the current page instead of closing it
            # Hide the current page
            self.current_page.pack_forget()

        # Show the new page
        if hasattr(page_instance, "pack"):
            page_instance.pack(fill=BOTH, expand=True)
        elif hasattr(page_instance, "grid"):
            page_instance.grid(row=0, column=0, sticky="nsew")
        elif hasattr(page_instance, "place"):
            page_instance.place(x=0, y=0, relwidth=1, relheight=1)
        else:
            raise AttributeError("Page instance doesn't support any layout manager")
        # Update the current page
        self.current_page = page_instance

    def update_cart(self, item):
        # Update cart display in ViewCart page
        self.viewcart_instance.update_cart_display(item)
        
    def initialize_ui(self):
        # Title
        title = Label(self.root, text="TILES SYSTEM", font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="c", padx=520)
        title.place(x=0, y=0, relwidth=1, height=70)
        
        btn_adm=Button(self.root,text="Admin Login",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2",command=self.open_admin).place(x=1300,y=20,height=30,width=150)
        
        # Clock
        self.lbl_clock = Label(self.root, text="", font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
        self.update_clock()
        
        # Left menu
        self.MenuLogo = Image.open("C:\\Users\\tejas\\Downloads\\tiles app\\menu_im.png").resize((200, 200))
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)
        
        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=15, y=140, width=350, height=535)
        
        lbl_menuLogo = Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)
        
        self.icon_side = PhotoImage(file="C:\\Users\\tejas\\Downloads\\images\\side.png")
        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20), bg="#009688").pack(side=TOP, fill=X)
        
        self.icon_title=PhotoImage(file="C:\\Users\\tejas\\Downloads\\tiles app\\welcome.png")
        title=Label(self.root,image=self.icon_title).place(x=380,y=150,height=500,width=1030)
        
        # Home button
        btn_home = Button(LeftMenu, text="HOME", image=self.icon_side, compound=LEFT, padx=20, font=("times new roman", 15), bg="white", bd=3, cursor="hand2", command=self.open_home)
        btn_home.pack(side=TOP, fill=X)
        
        # Category button
        btn_category = Button(LeftMenu, text="CATEGORY", image=self.icon_side, compound=LEFT, padx=20, font=("times new roman", 15), bg="white", bd=3, cursor="hand2", command=self.open_category)
        btn_category.pack(side=TOP, fill=X)
        
        # View Cart button
        btn_cart = Button(LeftMenu, text="VIEW CART", image=self.icon_side, compound=LEFT, padx=20, font=("times new roman", 15), bg="white", bd=3, cursor="hand2",command=self.open_view_cart)
        btn_cart.pack(side=TOP, fill=X)
        
        # Profile button
        btn_profile = Button(LeftMenu, text="PROFILE", image=self.icon_side, compound=LEFT, padx=20, font=("times new roman", 15), bg="white", bd=3, cursor="hand2",command=self.open_profile)
        btn_profile.pack(side=TOP, fill=X)
       
        # Feedback button
        btn_feedback = Button(LeftMenu, text="FEEDBACK", image=self.icon_side, compound=LEFT, padx=20, font=("times new roman", 15), bg="white", bd=3, cursor="hand2",command=self.open_feedback)
        btn_feedback.pack(side=TOP, fill=X)
        
        # About button
        btn_about = Button(LeftMenu, text="ABOUT", image=self.icon_side, compound=LEFT, padx=20, font=("times new roman", 15), bg="white", bd=3, cursor="hand2", command=self.open_about)
        btn_about.pack(side=TOP, fill=X)
        
        # Exit button
        btn_exit = Button(LeftMenu, text="EXIT", image=self.icon_side, compound=LEFT, padx=20, font=("times new roman", 15), bg="white", bd=3, cursor="hand2", command=self.exit)
        btn_exit.pack(side=TOP, fill=X)
         
        # Clock
        self.lbl_clock = Label(self.root, text="", font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
        self.update_clock()
        
        # Footer
        lbl_footer = Label(self.root, text="TS-TILES SYSTEM\nFor Technical Issue Contact: 98675xxx67\n DEVELOPED BY TEJAS & MILIND ", font=("times new roman", 12), bg="#4d636d", fg="white")
        lbl_footer.pack(side=BOTTOM, fill=X)
    
    def open_admin(self):
        # Check if the admin window exists and is not destroyed
        if self.admin_window and self.admin_window.winfo_exists():
            self.admin_window.deiconify()  # Show the existing admin window
        else:
            # If the admin window doesn't exist or is destroyed, create it
            self.admin_window = Toplevel(self.root)
            admin_obj = Login_System(self.admin_window)

    def open_home(self):
        if self.home_window and self.home_window.winfo_exists():  # If the home window exists and is not destroyed
            self.home_window.deiconify()  # Show the existing home window
        else:  # If the home window doesn't exist or is destroyed, create it
            self.home_window = Toplevel(self.root)
            home_obj = homeClass(self.home_window)

    def hide_home_window(self):
        # Hide the home window instead of destroying it
        self.home_window.withdraw()

    def update_clock(self):
        current_time = time.strftime('%H:%M:%S')
        current_date = time.strftime('%d-%m-%Y')
        self.lbl_clock.config(text=f"WELCOME TO TILES SYSTEM\t\t Date: {current_date}\t\t Time: {current_time}")
        self.lbl_clock.after(1000, self.update_clock)
    
    def open_category(self):
        if self.category_instance and self.category_instance.winfo_exists():
            self.category_instance.deiconify()
        else:
            self.category_instance = Toplevel(self.root)
            self.category_instance.title("Category")  # Set window title
            self.category_instance.protocol("WM_DELETE_WINDOW", self.hide_category_window)  # Set protocol
            category_obj = categoryClass(self.category_instance)

    def open_view_cart(self):
        if self.viewcart_instance and self.viewcart_instance.winfo_exists():  # If the view cart window exists and is not destroyed
            self.viewcart_instance.deiconify()  # Show the existing view cart window
        else:  # If the view cart window doesn't exist or is destroyed, create it
            self.viewcart_instance = ViewCart(self.root)

    def open_profile(self):
        if self.profile_instance and self.profile_instance.winfo_exists():
            self.profile_instance.deiconify()
        else:
            self.profile_instance = Toplevel(self.root)
            self.profile_instance.title("Profile")  # Set window title
            self.profile_instance.protocol("WM_DELETE_WINDOW", self.hide_profile_window)  # Set protocol
            profile_obj = profileClass(self.profile_instance)
    
    def open_feedback(self):
        if self.feedback_instance and self.feedback_instance.winfo_exists():
            self.feedback_instance.deiconify()
        else:
            self.feedback_instance = Toplevel(self.root)
            self.feedback_instance.title("feedback")  # Set window title
            self.feedback_instance.protocol("WM_DELETE_WINDOW", self.hide_feedback_window)  # Set protocol
            feedback_obj = feedbackClass(self.feedback_instance)

    def open_about(self):
        if self.about_instance:  # If the about window exists
            self.about_instance.deiconify()  # Show the existing about window
        else:  # If the about window doesn't exist, create it
            self.about_instance = AboutPage(self.root)
            self.about_instance.protocol("WM_DELETE_WINDOW", self.hide_about_window)
    
    def hide_category_window(self):
        if self.category_instance:
            self.category_instance.withdraw()

    def hide_profile_window(self):
        if self.profile_instance:
            self.profile_instance.withdraw()

    def hide_feedback_window(self):
        if self.feedback_instance:
            self.feedback_instance.withdraw()

    def hide_about_window(self):
        if self.about_instance:
            self.about_instance.withdraw()

    def exit(self):
        self.root.destroy()
    
if __name__ == "__main__":
    root = Tk()
    obj = IMSClass(root)
    root.protocol("WM_DELETE_WINDOW", obj.on_closing)
    root.mainloop()