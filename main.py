import tkinter as tk
from tkinter import messagebox
from escpos.printer import Usb

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant POS")

        self.selected_items = []

        self.pizzas = {
            "چیکن باربیکیو": "333",
            "چیکن": "330",
            "ژامبون": "367",
            "چیکن پستو": "345",
            "بوقلمون پستو": "387",
            "مینس میت": "435",
            "مارگاریتا": "210",
            "پپرونی": "357",
        }

        self.mini_pizzas = {
            "مینی پپرونی": "160",
            "مینی ژامبون": "165",
            "مینی مینس میت": "185",
            "مینی چیکن": "155",
            "مینی مارگاریتا": "90",
        }

        self.burgers = {
            "شیکاگو": "299",
            "پاریس": "330",
            "کلورادو": "359",
            "فلوریدا": "325",
            "مکزیکانو": "318",
            "میلان": "327",
            "تگزاس": "349",
            "دبل فولی": "518",
        }

        self.drinks = {
            "آب معدنی": "6",
            "نوشابه قوطی": "27",
            "دلستر": "30",
        }

        self.starters = {
            "سیب ساده": "120",
            "سیب ویژه": "175",
            "سالاد کلم": "30",
        }

        self.create_widgets()

    def create_widgets(self):
        self.create_category_buttons("Pizzas", self.pizzas)
        self.create_category_buttons("Mini Pizzas", self.mini_pizzas)
        self.create_category_buttons("Burgers", self.burgers)
        self.create_category_buttons("Drinks", self.drinks)
        self.create_category_buttons("Starters", self.starters)

        print_button = tk.Button(self.root, text="Print Receipt", command=self.print_receipt)
        print_button.pack(pady=20)


    def create_category_buttons(self, category, items):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)
        tk.Label(frame, text=category, font=("Arial", 14)).pack()
        for item, price in items.items():
            button = tk.Button(frame, text=f"{item} - {price}", command=lambda i=item: self.add_item(i))
            button.pack(side=tk.LEFT, padx=5)


    def add_item(self, item):
        self.selected_items.append(item)
        messagebox.showinfo("Item Added", f"{item} added to the list!")


    def print_receipt(self):
        try:
            p = Usb(0x04b8, 0x0202)  # Replace printer's Vendor ID and Product ID
            receipt = "\n".join(self.selected_items)
            p.text(receipt)
            p.cut()
            messagebox.showinfo("Success", "Receipt printed successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))



root = tk.Tk()
app = App(root)
root.mainloop()
