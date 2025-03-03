import tkinter as tk
from tkinter import Label, Button, PhotoImage

class AboutPage:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("About Page")
        self.window.geometry("450x650")

        app_logo_path = "C:/Users/tejas/Downloads/tiles app/ts-logo.png"
        
        try:
            self.app_logo = PhotoImage(file=app_logo_path)
            print("Image loaded successfully")
        except Exception as e:
            print("Error loading image:", e)
            self.app_logo = None

        app_name = "Tiles System"
        app_version = "1.0.0"

        logo_label = Label(self.window, image=self.app_logo)
        name_label = Label(self.window, text=f"{app_name}\n", font=("Arial", 16, "bold"))
        version_label = Label(self.window, text=f"Version {app_version}\n")
        about_text = f"""
        Welcome to the {app_name} About page!

        Here you can find information about our app and its features.

        Version {app_version} was released on Feb 21, 2023.
        """
        about_label = Label(self.window, text=about_text, wraplength=350, font=("Arial", 12))
        close_button = Button(self.window, text="Close", command=self.window.destroy)

        logo_label.pack(pady=10)
        name_label.pack(pady=10)
        version_label.pack(pady=10)
        about_label.pack(pady=10)
        close_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    obj = AboutPage(root)
    root.mainloop()
