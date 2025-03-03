import sys
import subprocess
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from buy2 import BillingPage
from cart import ViewCart

class homeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1540x780+0+0")
        self.root.title("Home")
        self.cart_manager = ViewCart(root)
        self.buy_instance = None
        def on_closing(self):
        # Hide the window instead of destroying it
            self.root.withdraw()
        def show(self):
            self.mainloop()
        self.icon_title = PhotoImage(file="C:\\Users\\tejas\\Downloads\\tiles app\\wp10701716 (1).png")
        title = Label(self.root, image=self.icon_title, compound=LEFT)
        title.place(x=20, y=50, relwidth=1, height=10)

        title = Label(self.root, text="Search Tiles ", font=("times new roman", 40, "bold"), bg="#010c48",
                      fg="white")
        title.place(x=5, y=0, relwidth=1)

        SearchFrame = LabelFrame(self.root, text="Search Tile", bg="orange", font=("times new roman", 12), bd=2,
                                 relief=RIDGE)
        SearchFrame.place(x=1000, y=0, width=600, height=68)

        self.cmb_search = ttk.Combobox(SearchFrame, values=("Hall", "Bedroom", "Kitchen", "Bathroom", "Garden"),
                                       state='readonly', justify=CENTER, font=("times new roman", 20, "bold"))
        self.cmb_search.place(x=10, y=5, width=250)
        self.cmb_search.current(0)

        btn_search = Button(SearchFrame, text="Search", font=("times new roman", 15), bg="green",
                            command=self.open_selected)
        btn_search.place(x=300, y=6, width=150, height=35)

        # White frame below search bar
        frame1 = Frame(self.root, bd=2, bg="white", relief=RIDGE)
        frame1.place(x=0, y=100, width=1500, height=1000)

        # Tile 1
        self.icon_title = PhotoImage(file="C:\\Users\\tejas\\Downloads\\111.png")
        title = Label(self.root, image=self.icon_title)
        title.place(x=40, y=150)
        lbl_name = Label(self.root, text="Vein Tile", font=("times new roman", 20, "bold"), bg="white", fg="black")
        lbl_name.place(x=40, y=310)
        lbl_price = Label(self.root, text="MRP ₹ 71/-Sq.ft", font=("times new roman", 15), bg="white", fg="black")
        lbl_price.place(x=40, y=350)
        lbl_size = Label(self.root, text="Size 600x600 mm ft", font=("times new roman", 15), bg="white", fg="black")
        lbl_size.place(x=40, y=380)
        btn_buy = Button(self.root, text="Buy Now", font=("times new roman", 20, "bold"), bg="#13EAC9", fg="black",command=self.open_buy_page)
        btn_buy.place(x=230, y=350, height=40, width=130)
        lbl_cart = Button(self.root, text="Add To Cart", font=("times new roman", 15, "bold"), bg="green", fg="white",command=lambda: self.add_to_cart({
                      "Name": "Vein Tile",
                      "Price": "MRP ₹ 71/-Sq.ft",
                      "Size": "Size 600x600 mm ft"
                  }))
        lbl_cart.place(x=40, y=430, height=30, width=320)

        # Tile 2
        self.icon_title1 = PhotoImage(file="C:\\Users\\tejas\\Downloads\\222.png")
        title = Label(self.root, image=self.icon_title1)
        title.place(x=400, y=150, height=165)
        lbl_name = Label(self.root, text="Block Tile", font=("times new roman", 20, "bold"), bg="white", fg="black")
        lbl_name.place(x=400, y=310)
        lbl_price = Label(self.root, text="MRP ₹ 55/-Sq.ft", font=("times new roman", 15), bg="white", fg="black")
        lbl_price.place(x=400, y=350)
        lbl_size = Label(self.root, text="Size 550x550 mm ft", font=("times new roman", 15), bg="white", fg="black")
        lbl_size.place(x=400, y=380)
        btn_buy = Button(self.root, text="Buy Now", font=("times new roman", 20, "bold"), bg="#13EAC9", fg="black",command=self.open_buy_page2)
        btn_buy.place(x=590, y=350, height=40, width=130)
        lbl_cart = Button(self.root, text="Add To Cart", font=("times new roman", 15, "bold"), bg="green", fg="white",command=lambda: self.add_to_cart({
                      "Name": "Block Tile",
            "Price": "MRP ₹ 55/-Sq.ft",
            "Size": "Size 550x550 mm ft"
                  }))
        lbl_cart.place(x=400, y=430, height=30, width=320)

        # Tile 3
        self.icon_title2 = PhotoImage(file="C:\\Users\\tejas\\Downloads\\333 - Copy.png")
        title = Label(self.root, image=self.icon_title2)
        title.place(x=760, y=150, height=165)
        lbl_name = Label(self.root, text="Flower Tile", font=("times new roman", 20, "bold"), bg="white", fg="black")
        lbl_name.place(x=760, y=310)
        lbl_price = Label(self.root, text="MRP ₹ 65/-Sq.ft", font=("times new roman", 15), bg="white", fg="black")
        lbl_price.place(x=760, y=350)
        lbl_size = Label(self.root, text="Size 500x565 mm ft", font=("times new roman", 15), bg="white", fg="black")
        lbl_size.place(x=760, y=380)
        btn_buy = Button(self.root, text="Buy Now", font=("times new roman", 20, "bold"), bg="#13EAC9", fg="black",command=self.open_buy_page3)
        btn_buy.place(x=950, y=350, height=40, width=130)
        lbl_cart = Button(self.root, text="Add To Cart", font=("times new roman", 15, "bold"), bg="green", fg="white",command=self.add_to_cart3)
        lbl_cart.place(x=760, y=430, height=30, width=320)

        # Tile 4
        self.icon_title3 = PhotoImage(file="C:\\Users\\tejas\\Downloads\\444.png")
        title = Label(self.root, image=self.icon_title3)
        title.place(x=1120, y=150, height=165)
        lbl_name = Label(self.root, text="Black & White Block Tile", font=("times new roman", 20, "bold"), bg="white", fg="black")
        lbl_name.place(x=1120, y=310)
        lbl_price = Label(self.root, text="MRP ₹ 65/-Sq.ft", font=("times new roman", 15), bg="white", fg="black")
        lbl_price.place(x=1120, y=350)
        lbl_size = Label(self.root, text="Size 500x505 mm ft", font=("times new roman", 15), bg="white", fg="black")
        lbl_size.place(x=1120, y=380)
        btn_buy = Button(self.root, text="Buy Now", font=("times new roman", 20, "bold"), bg="#13EAC9", fg="black",command=self.open_buy_page4)
        btn_buy.place(x=1310, y=350, height=40, width=130)
        lbl_cart = Button(self.root, text="Add To Cart", font=("times new roman", 15, "bold"), bg="green", fg="white",command=self.add_to_cart4)
        lbl_cart.place(x=1120, y=430, height=30, width=320)
    
    #tile 5......================================================================
        self.icon_title4=PhotoImage(file="C:\\Users\\tejas\\Downloads\\555.png")
        title=Label(self.root,image=self.icon_title4,).place(x=40,y=500,height=165)
        lbl_name=Label(self.root,text="Star Tile",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=40,y=660)
        lbl_price=Label(self.root,text="MRP ₹ 86/-Sq.ft",font=("times new roman",15),bg="white",fg="black").place(x=40,y=700)
        lbl_size=Label(self.root,text="Size 500x550 mm ft",font=("times new roman",15),bg="white",fg="black").place(x=40,y=730)
        btn_buy=Button(self.root,text="Buy Now",font=("times new roman",20,"bold"),bg="#13EAC9",fg="black",command=self.open_buy_page5).place(x=230,y=700,height=40,width=130)
        lbl_cart=Button(self.root,text="       Add To Cart        ",font=("times new roman",15,"bold"),bg="green",fg="WHITE",command=self.add_to_cart5).place(x=40,y=760,height=30,width=320)

    #tile 6.............====================================================
        self.icon_title5=PhotoImage(file="C:\\Users\\tejas\\Downloads\\666.png")
        title=Label(self.root,image=self.icon_title5,).place(x=400,y=500,height=165)
        lbl_name=Label(self.root,text="Quardinate Tile",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=400,y=660)
        lbl_price=Label(self.root,text="MRP ₹ 86/-Sq.ft",font=("times new roman",15),bg="white",fg="black").place(x=400,y=700)
        lbl_size=Label(self.root,text="Size 500x550 mm ft",font=("times new roman",15),bg="white",fg="black").place(x=400,y=730)
        btn_buy=Button(self.root,text="Buy Now",font=("times new roman",20,"bold"),bg="#13EAC9",fg="black",command=self.open_buy_page6).place(x=590,y=700,height=40,width=130)
        lbl_cart=Button(self.root,text="       Add To Cart        ",font=("times new roman",15,"bold"),bg="green",fg="WHITE",command=self.add_to_cart6).place(x=400,y=760,height=30,width=320)

    #tile 7.......======================================================================
        self.icon_title6=PhotoImage(file="C:\\Users\\tejas\\Downloads\\777.png")
        title=Label(self.root,image=self.icon_title6,).place(x=760,y=500,height=165)
        lbl_name=Label(self.root,text="Roon Tile",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=760,y=660)
        lbl_price=Label(self.root,text="MRP ₹ 86/-Sq.ft",font=("times new roman",15),bg="white",fg="black").place(x=760,y=700)
        lbl_size=Label(self.root,text="Size 500x550 mm ft",font=("times new roman",15),bg="white",fg="black").place(x=760,y=730)
        btn_buy=Button(self.root,text="Buy Now",font=("times new roman",20,"bold"),bg="#13EAC9",fg="black",command=self.open_buy_page7).place(x=950,y=700,height=40,width=130)
        lbl_cart=Button(self.root,text="       Add To Cart        ",font=("times new roman",15,"bold"),bg="green",fg="WHITE",command=self.add_to_cart7).place(x=760,y=760,height=30,width=320)

##### 8...........====================================================================
        self.icon_title7=PhotoImage(file="C:\\Users\\tejas\\Downloads\\888.png")
        title=Label(self.root,image=self.icon_title7,).place(x=1120,y=500,height=165)
        lbl_name=Label(self.root,text="Marble Tile",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=1120,y=660)
        lbl_price=Label(self.root,text="MRP ₹ 86/-Sq.ft",font=("times new roman",15),bg="white",fg="black").place(x=1120,y=700)
        lbl_size=Label(self.root,text="Size 500x550 mm ft",font=("times new roman",15),bg="white",fg="black").place(x=1120,y=730)
        btn_buy=Button(self.root,text="Buy Now",font=("times new roman",20,"bold"),bg="#13EAC9",fg="black",command=self.open_buy_page8).place(x=1310,y=700,height=40,width=130)
        lbl_cart=Button(self.root,text="       Add To Cart        ",font=("times new roman",15,"bold"),bg="green",fg="WHITE",command=self.add_to_cart8).place(x=1120,y=760,height=30,width=320)

    def open_selected(self):
        selected_option = self.cmb_search.get()
        if selected_option == "Bedroom":
            python_executable = sys.executable
            subprocess.Popen([python_executable, "#bedroom.py"])
        elif selected_option == "Hall":
            python_executable = sys.executable
            subprocess.Popen([python_executable, "hall.py"])
        elif selected_option == "Kitchen":
            python_executable = sys.executable
            subprocess.Popen([python_executable, "kitchen.py"])
        elif selected_option == "Bathroom":
            python_executable = sys.executable
            subprocess.Popen([python_executable, "bathroom.py"])
        elif selected_option == "Garden":
            python_executable = sys.executable
            subprocess.Popen([python_executable, "garden.py"])

    def open_buy_page(self):
        if not self.buy_instance:  
            # Provide dummy values for product_info, price_per_sqft, and image_path
            product_info = "Vein Tile"
            price_per_sqft = 71  
            image_path = "C:\\Users\\tejas\\Downloads\\111.png"

            # Create a new instance of BillingPage and pass the image path
            self.buy_instance = BillingPage(self.root, product_info, price_per_sqft, image_path)

            # Open the new instance
            self.open_page(self.buy_instance)
        else:
            # If an instance already exists, bring it to the front
            self.buy_instance.root.lift()


    def open_page(self, instance):
        instance.root.lift()
 

    def open_buy_page2(self):
        if not self.buy_instance:
            # Provide dummy values for product_info, price_per_sqft, and image_path
            product_info = "Block Tile"
            price_per_sqft = "MRP ₹ 55/-Sq.ft"
            image_path = "C:\\Users\\tejas\\Downloads\\222.png"
            
            # Create a new instance of BillingPage
        buy_instance = BillingPage(self.root, product_info, price_per_sqft, image_path)
        
        # Open the new instance
        self.open_page(buy_instance)
    
    def open_buy_page3(self):
        if not self.buy_instance:
            # Provide dummy values for product_info, price_per_sqft, and image_path
            product_info = "Flower Tile"
            price_per_sqft = "MRP ₹ 65/-Sq.ft"
            image_path = "C:\\Users\\tejas\\Downloads\\333 - Copy.png"
            
           # Create a new instance of BillingPage
        buy_instance = BillingPage(self.root, product_info, price_per_sqft, image_path)
        
        # Open the new instance
        self.open_page(buy_instance)
    
    def open_buy_page4(self):
        if not self.buy_instance:
            # Provide dummy values for product_info, price_per_sqft, and image_path
            product_info = "Black & White Block Tile"
            price_per_sqft = "MRP ₹ 65/-Sq.ft"
            image_path = "C:\\Users\\tejas\\Downloads\\444.png"
            
           # Create a new instance of BillingPage
        buy_instance = BillingPage(self.root, product_info, price_per_sqft, image_path)
        
        # Open the new instance
        self.open_page(buy_instance)

    def open_buy_page5(self):
        if not self.buy_instance:
            # Provide dummy values for product_info, price_per_sqft, and image_path
            product_info = "Star Tile"
            price_per_sqft = "MRP ₹ 86/-Sq.ft"
            image_path = "C:\\Users\\tejas\\Downloads\\555.png"
            
            # Create a new instance of BillingPage
        buy_instance = BillingPage(self.root, product_info, price_per_sqft, image_path)
        
        # Open the new instance
        self.open_page(buy_instance)

    def open_buy_page6(self):
        if not self.buy_instance:
            # Provide dummy values for product_info, price_per_sqft, and image_path
            product_info = "Quardinate Tile"
            price_per_sqft = "MRP ₹ 86/-Sq.ft"
            image_path = "C:\\Users\\tejas\\Downloads\\666.png"
            
            # Create a new instance of BillingPage
        buy_instance = BillingPage(self.root, product_info, price_per_sqft, image_path)
        
        # Open the new instance
        self.open_page(buy_instance)

    def open_buy_page7(self):
        if not self.buy_instance:
            # Provide dummy values for product_info, price_per_sqft, and image_path
            product_info = "Roon Tile"
            price_per_sqft = "MRP ₹ 86/-Sq.ft"
            image_path = "C:\\Users\\tejas\\Downloads\\777.png"
            
           # Create a new instance of BillingPage
        buy_instance = BillingPage(self.root, product_info, price_per_sqft, image_path)
        
        # Open the new instance
        self.open_page(buy_instance)

    def open_buy_page8(self):
        if not self.buy_instance:
            # Provide dummy values for product_info, price_per_sqft, and image_path
            product_info = "Marble Tile"
            price_per_sqft = "MRP ₹ 86/-Sq.ft"
            image_path = "C:\\Users\\tejas\\Downloads\\888.png"
            
            # Create a new instance of BillingPage
        buy_instance = BillingPage(self.root, product_info, price_per_sqft, image_path)
        
        # Open the new instance
        self.open_page(buy_instance)

    def add_to_cart(self, selected_item):
        # Update cart display and show message
        self.cart_manager.update_cart_display(selected_item)
        messagebox.showinfo("Success", "Product added to cart!")


    def add_to_cart2(self, selected_item):
        # Update cart display and show message
        self.cart_manager.update_cart_display(selected_item)
        messagebox.showinfo("Success", "Product added to cart!")

    def add_to_cart3(self):
        # Logic to add the selected item to the cart
        selected_item = {
            "Name": "Flower Tile",
            "Price": "MRP ₹ 65/-Sq.ft",
            "Size": "Size 500x565 mm ft"
        }
        # Update cart display and show message
        self.cart_manager.update_cart_display(selected_item)
        messagebox.showinfo("Success", "Product added to cart!")
    def add_to_cart4(self):
        # Logic to add the selected item to the cart
        selected_item = {
            "Name": "Black & White Block Tile",
            "Price": "MRP ₹ 65/-Sq.ft",
            "Size": "Size 500x505 mm ft"
        }
        # Update cart display and show message
        self.cart_manager.update_cart_display(selected_item)
        messagebox.showinfo("Success", "Product added to cart!")
    def add_to_cart5(self):
        # Logic to add the selected item to the cart
        selected_item = {
            "Name": "Star Tile",
            "Price": "MRP ₹ 86/-Sq.ft",
            "Size": "Size 500x550 mm ft"
        }
        # Update cart display and show message
        self.cart_manager.update_cart_display(selected_item)
        messagebox.showinfo("Success", "Product added to cart!")
    def add_to_cart6(self):
        # Logic to add the selected item to the cart
        selected_item = {
            "Name": "Quardinate Tile",
            "Price": "MRP ₹ 86/-Sq.ft",
            "Size": "Size 500x550 mm ft"
        }
        # Update cart display and show message
        self.cart_manager.update_cart_display(selected_item)
        messagebox.showinfo("Success", "Product added to cart!")
    def add_to_cart7(self):
        # Logic to add the selected item to the cart
        selected_item = {
            "Name": "Roon Tile",
            "Price": "MRP ₹ 86/-Sq.ft",
            "Size": "Size 500x550 mm ft"
        }
        # Update cart display and show message
        self.cart_manager.update_cart_display(selected_item)
        messagebox.showinfo("Success", "Product added to cart!")
    def add_to_cart8(self):
        # Logic to add the selected item to the cart
        selected_item = {
            "Name": "Marble Tile",
            "Price": "MRP ₹ 86/-Sq.ft",
            "Size": "Size 500x550 mm ft"
        }
        # Update cart display and show message
        self.cart_manager.update_cart_display(selected_item)
        messagebox.showinfo("Success", "Product added to cart!")

if __name__ == "__main__":
    root = Tk()
    obj = homeClass(root) 
    root.mainloop()

