from tkinter import *
import json

class ViewCart:
    def __init__(self, root):
        self.root = root
        self.cart_items = self.load_cart_items()  # Load cart items from file
        self.initialize_ui()

    def initialize_ui(self):
        # Initialize UI components for the view cart page
        self.cart_frame = Frame(self.root, bd=2, bg="white", relief=SUNKEN)
        self.cart_frame.place(x=1000, y=100, width=500, height=600)

        cart_title = Label(self.cart_frame, text="Shopping Cart", font=("times new roman", 20, "bold"), bg="white")
        cart_title.pack(side="top", fill="x")
        
        # Create a listbox to display cart items
        self.cart_listbox = Listbox(self.cart_frame, font=("times new roman", 12), bg="white", bd=0, selectbackground="orange")
        self.cart_listbox.pack(fill="both", expand=True)

        # Button to clear the cart
        clear_cart_btn = Button(self.cart_frame, text="Clear Cart", command=self.clear_cart)
        clear_cart_btn.pack(side="bottom", pady=10)

        close_btn = Button(self.cart_frame, text="Close", command=self.close)
        close_btn.pack(side="bottom", pady=10)
        # Update cart display with loaded items
        for item in self.cart_items:
            self.cart_listbox.insert(END, f"{item['Name']} - {item['Price']} - {item['Size']}")

    def update_cart_display(self, item):
        self.cart_items.append(item)
        self.cart_listbox.insert(END, f"{item['Name']} - {item['Price']} - {item['Size']}")
        self.save_cart_items()  # Save updated cart items to file

    def clear_cart(self):
        # Clear the cart and the listbox
        self.cart_items = []
        self.cart_listbox.delete(0, END)
        self.save_cart_items()  # Save cleared cart items to file

    def load_cart_items(self):
        try:
            with open("cart_items.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_cart_items(self):
        with open("cart_items.json", "w") as file:
            json.dump(self.cart_items, file)

    def close(self):
        self.cart_frame.destroy()

if __name__ == "__main__":
    root = Tk()
    app = ViewCart(root)  
    root.mainloop()
