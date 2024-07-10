import tkinter as tk
from tkinter import messagebox
from database import add_book, add_member, borrow_book, return_book

class LibraryApp:
    def __init__(self, root):
        self.root = root
        root.title("Library Management System")

        # Add Book Section
        self.label_title = tk.Label(root, text="Title:")
        self.label_title.grid(row=0, column=0)
        self.entry_title = tk.Entry(root)
        self.entry_title.grid(row=0, column=1)

        self.label_author = tk.Label(root, text="Author:")
        self.label_author.grid(row=1, column=0)
        self.entry_author = tk.Entry(root)
        self.entry_author.grid(row=1, column=1)

        self.label_barcode = tk.Label(root, text="Barcode:")
        self.label_barcode.grid(row=2, column=0)
        self.entry_barcode = tk.Entry(root)
        self.entry_barcode.grid(row=2, column=1)

        self.button_add_book = tk.Button(root, text="Add Book", command=self.add_book)
        self.button_add_book.grid(row=3, column=1)

        # Add Member Section
        self.label_name = tk.Label(root, text="Member Name:")
        self.label_name.grid(row=4, column=0)
        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row=4, column=1)

        self.label_membership_id = tk.Label(root, text="Membership ID:")
        self.label_membership_id.grid(row=5, column=0)
        self.entry_membership_id = tk.Entry(root)
        self.entry_membership_id.grid(row=5, column=1)

        self.button_add_member = tk.Button(root, text="Add Member", command=self.add_member)
        self.button_add_member.grid(row=6, column=1)

        # Borrow Book Section
        self.label_borrow_barcode = tk.Label(root, text="Book Barcode:")
        self.label_borrow_barcode.grid(row=7, column=0)
        self.entry_borrow_barcode = tk.Entry(root)
        self.entry_borrow_barcode.grid(row=7, column=1)

        self.label_borrow_member_id = tk.Label(root, text="Membership ID:")
        self.label_borrow_member_id.grid(row=8, column=0)
        self.entry_borrow_member_id = tk.Entry(root)
        self.entry_borrow_member_id.grid(row=8, column=1)

        self.button_borrow_book = tk.Button(root, text="Borrow Book", command=self.borrow_book)
        self.button_borrow_book.grid(row=9, column=1)

        # Return Book Section
        self.label_return_barcode = tk.Label(root, text="Return Barcode:")
        self.label_return_barcode.grid(row=10, column=0)
        self.entry_return_barcode = tk.Entry(root)
        self.entry_return_barcode.grid(row=10, column=1)

        self.button_return_book = tk.Button(root, text="Return Book", command=self.return_book)
        self.button_return_book.grid(row=11, column=1)

    def add_book(self):
        title = self.entry_title.get()
        author = self.entry_author.get()
        barcode = self.entry_barcode.get()
        if title and author and barcode:
            add_book(title, author, barcode)
        else:
            messagebox.showerror("Error", "All fields are required!")

    def add_member(self):
        name = self.entry_name.get()
        membership_id = self.entry_membership_id.get()
        if name and membership_id:
            add_member(name, membership_id)
        else:
            messagebox.showerror("Error", "All fields are required!")

    def borrow_book(self):
        barcode = self.entry_borrow_barcode.get()
        membership_id = self.entry_borrow_member_id.get()
        if barcode and membership_id:
            borrow_book(barcode, membership_id)
        else:
            messagebox.showerror("Error", "All fields are required!")

    def return_book(self):
        barcode = self.entry_return_barcode.get()
        if barcode:
            return_book(barcode)
        else:
            messagebox.showerror("Error", "Barcode is required!")

# Main
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
