import tkinter as tk
from tkinter import ttk
import pymysql # type: ignore

class adminClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1540x800+0+0")
        self.root.title("Admin Page")

        self.user_tree = ttk.Treeview(self.root, columns=("Product Name", "Price", "Quantity", "Total Cost"))
        self.user_tree.heading("#0", text="Username")
        self.user_tree.heading("Product Name", text="Product Name")
        self.user_tree.heading("Price", text="Price")
        self.user_tree.heading("Quantity", text="Quantity")
        self.user_tree.heading("Total Cost", text="Total Cost")
        self.user_tree.pack(expand=True, fill=tk.BOTH)

        # Fetch and display user orders
        self.display_user_orders()

    def display_user_orders(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="abc", database="ts")
            cur = con.cursor()

            # Fetch all orders
            cur.execute("SELECT customer_name, product_info, price_per_sqft, quantity, total_cost FROM invoices")
            orders = cur.fetchall()

            for order in orders:
                username, product_name, price, quantity, total_cost = order
                self.user_tree.insert("", "end", text=username, values=(product_name, price, quantity, total_cost))

        except pymysql.Error as e:
            print(f"Error fetching orders: {e}")
        finally:
            cur.close()
            con.close()

if __name__ == "__main__":
    root = tk.Tk()
    admin_page = adminClass(root)
    root.mainloop()
