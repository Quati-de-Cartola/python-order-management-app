import tkinter as tk
from tkinter import messagebox

class Application:
    def __init__(self, root):
        self.root = root

        # Set the window title
        self.root.title("Snack Bar - App")

        # Set the window size
        self.root.geometry("720x720")

        # Set items and their prices
        self.items_menu = {
            "Chips": 2.00,
            "Soda" : 2.20,
            "Burguer" : 5.00
        }
        self.order = []

        # Label for the Menu
        tk.Label(root, text="SELECT THE ORDER ITEMS:", font=("Arial", 14)).pack(pady=10)

        # Creating a listbox to display the menu items
        self.listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, font=("Arial", 12))
        self.update_menu_list()
        self.listbox.pack(pady=10)

        # Button to add an item to the order
        tk.Button(root, text="Add to Order", command=self.add_to_order, font=("Arial", 12)).pack(pady=5)
        # Button to visualize the order
        tk.Button(root, text="Visualize Order", command=self.visualize_order, font=("Arial", 12)).pack(pady=5)
        # Button to Finish the order
        tk.Button(root, text="Finish Order", command=self.finish_order, font=("Arial", 12)).pack(pady=5)
        
        tk.Label(root, text="Item Name:", font=("Arial", 12)).pack(pady=5)
        self.entry_item_name = tk.Entry(root, font=("Arial", 12))
        self.entry_item_name.pack(pady=5)

        tk.Label(root, text="Item Price:", font=("Arial", 12)).pack(pady=5)
        self.entry_item_price = tk.Entry(root, font=("Arial", 12))

        self.entry_item_price.pack(pady=5)

        tk.Button(root, text="Add new Item to Menu", command=self.add_item_to_menu, font=("Arial", 12)).pack(pady=5)

    def add_item_to_menu(self):
        item_name = self.entry_item_name.get()
        item_price = self.entry_item_price.get()
        if not item_name or not item_price:
            messagebox.showerror("Error", "Please enter both item name and price")
            return
        try:
            item_price = float(item_price)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid price")
            return
        self.items_menu[item_name] = item_price
        self.update_menu_list()
        messagebox.showinfo("Menu", f"{item_name} added to menu successfully!")

    def update_menu_list(self):
        self.listbox.delete(0, tk.END)
        # Insert items into the listbox
        for item in self.items_menu.keys():
            self.listbox.insert(tk.END, item)

    def add_to_order(self):
        selected_items = self.listbox.curselection()
        for index in selected_items:
            item_name = self.listbox.get(index)
            self.order.append(item_name)
        messagebox.showinfo("Order", "Items added to order successfully!")
    
    def visualize_order(self):
        if not self.order:
            messagebox.showinfo("Order", "No items in the order")
            return
        order_summary = "\n".join(self.order)
        messagebox.showinfo("Order Summary", order_summary)

    def finish_order(self):
        if not self.order:
            messagebox.showinfo("Order", "No items in the order")
            return
        total = sum(self.items_menu[item] for item in self.order)
        messagebox.showinfo("Order Total", f"Total: ${total:.2f}")
        self.order.clear()
    
    def add_new_item(self):
        item_name = self.entry_item_name.get()
        item_price = self.entry_item_price.get()
        if not item_name or not item_price:
            messagebox.showerror("Error", "Please enter both item name and price")
            return
        try:
            item_price = float(item_price)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid price")
            return
        self.items_menu[item_name] = item_price
        self.update_menu_list()
        messagebox.showinfo("Menu", f"{item_name} added to menu successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()