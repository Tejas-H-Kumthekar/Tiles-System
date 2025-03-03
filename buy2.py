from tkinter import *
import pymysql # type: ignore

class BillingPage:
    def __init__(self, root, product_info, price_per_sqft, image_path):
        self.root = root        
        self.product_info = product_info
        self.price_per_sqft = price_per_sqft
        self.image_path = image_path
        self.quantity = IntVar()
        self.total_cost = 0
        self.root.title("Billing")
        self.root.geometry("400x700")
        
        title = Label(self.root, text="For Hall", font=("times new roman", 30, "bold"), bg="#010c48", fg="white")
        title.place(x=0, y=0, relwidth=1)
 
        self.lbl_title = Label(self.root, text="Billing Information", font=("times new roman", 20, "bold"), bg="#010c48",fg="white")
        self.lbl_title.pack(pady=10)
        
        # Customer Information Section
        self.lbl_customer_info = Label(self.root, text="Customer Information", font=("times new roman", 14, "bold"))
        self.lbl_customer_info.pack()
        
        self.lbl_name = Label(self.root, text="Name:", font=("times new roman", 12))
        self.lbl_name.pack()
        self.entry_name = Entry(self.root, font=("times new roman", 12))
        self.entry_name.pack(pady=5)
        
        self.lbl_address = Label(self.root, text="Address:", font=("times new roman", 12))
        self.lbl_address.pack()
        self.entry_address = Entry(self.root, font=("times new roman", 12))
        self.entry_address.pack(pady=5)
        
        self.lbl_contact = Label(self.root, text="Contact:", font=("times new roman", 12))
        self.lbl_contact.pack()
        self.entry_contact = Entry(self.root, font=("times new roman", 12))
        self.entry_contact.pack(pady=5)
        
        # Load and display the image
        self.lbl_image = Label(self.root)
        self.lbl_image.pack()
        self.load_image()
        
        # Display product information
        self.lbl_product_info = Label(self.root, text=self.product_info, font=("times new roman", 14))
        self.lbl_product_info.pack(pady=5)
        
        # Quantity selection
        self.lbl_quantity = Label(self.root, text="Quantity:", font=("times new roman", 14))
        self.lbl_quantity.pack(pady=5)
        self.entry_quantity = Entry(self.root, textvariable=self.quantity, font=("times new roman", 14))
        self.entry_quantity.pack(pady=5)
        
        # Calculate total cost
        self.btn_calculate = Button(self.root, text="Calculate Total", command=self.calculate_total, font=("times new roman", 14))
        self.btn_calculate.pack(pady=5)
        
        self.lbl_total = Label(self.root, text="", font=("times new roman", 14))
        self.lbl_total.pack(pady=5)
        
        # Generate Invoice button
        self.btn_invoice = Button(self.root, text="Generate Invoice", command=self.generate_invoice_window, font=("times new roman", 14))
        self.btn_invoice.pack(pady=10)
        
    def load_image(self):
        # Load and display the image
        try:
            self.image = PhotoImage(file=self.image_path)
            self.lbl_image.config(image=self.image)
        except Exception as e:
            print("Error loading image:", e)
        
    def calculate_total(self):
        try:
            quantity = self.quantity.get()
            total_cost = quantity * self.price_per_sqft
            self.lbl_total.config(text=f"Total Cost: ₹ {total_cost}")
            self.total_cost = total_cost
        except Exception as e:
            print("Error calculating total:", e)
            
    def generate_invoice_window(self):
        customer_name = self.entry_name.get()
        customer_address = self.entry_address.get()
        customer_contact = self.entry_contact.get()
        quantity = self.quantity.get()

        try:
            con = pymysql.connect(host="localhost", user="root", password="abc", database="ts")
            cur = con.cursor()
            
            # Insert data into the invoice table
            cur.execute("INSERT INTO invoices (customer_name,customer_address ,customer_contact,product_info,price_per_sqft, quantity, total_cost) VALUES (%s, %s, %s, %s,%s, %s,%s)",
                        (customer_name, customer_address,customer_contact,self.product_info, self.price_per_sqft,quantity, self.total_cost))
            con.commit()

            # Close the database connection
            cur.close()
            con.close()
        except pymysql.Error as e:
            print(f"Error inserting data into the database: {e}")
    
        invoice_window = Toplevel(self.root)
        invoice_window.title("Invoice")
        invoice_window.geometry("600x500")  # Set the dimensions of the invoice window
        invoice_window.config(bg="yellow")
      
        # Customer details
        lbl_customer_details = Label(invoice_window, text=f"Customer Name: {customer_name}\nAddress: {customer_address}\nContact: {customer_contact}", font=("times new roman", 20),fg="red",bg="yellow")
        lbl_customer_details.pack(pady=15)
        
        # Product details
        lbl_product_info = Label(invoice_window, text=self.product_info, font=("times new roman", 22),bg="yellow")
        lbl_product_info.pack(pady=5)
        
        # Quantity
        lbl_quantity = Label(invoice_window, text=f"Quantity: {quantity}", font=("times new roman", 22),bg="yellow")
        lbl_quantity.pack(pady=5)
        
        # Total cost
        lbl_total_cost = Label(invoice_window, text=f"Total Cost: ₹ {self.total_cost}", font=("times new roman", 22),bg="yellow")
        lbl_total_cost.pack(pady=5)
        
        # Order successful message
        lbl_success = Label(invoice_window, text="Order Successful!", font=("times new roman", 30, "bold"),bg="yellow", fg="green").place(x=150,y=350)
        lbl_success.pack(pady=10)

if __name__ == "__main__":
    root = Tk()
    product_info = "Vein Tile - Size 600x600 mm ft"
    price_per_sqft = 71
    image_path = "C:\\Users\\tejas\\Downloads\\111.png"
    obj = BillingPage(root, product_info, price_per_sqft, image_path)
    root.mainloop() 
