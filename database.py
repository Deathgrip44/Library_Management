import sqlite3
from datetime import datetime
from tkinter import messagebox

def add_book(title, author, barcode):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO books (title, author, barcode) VALUES (?, ?, ?)', (title, author, barcode))
        conn.commit()
        messagebox.showinfo("Success", "Book added successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Book with this barcode already exists!")
    conn.close()

def add_member(name, membership_id):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO members (name, membership_id) VALUES (?, ?)', (name, membership_id))
        conn.commit()
        messagebox.showinfo("Success", "Member added successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Member with this ID already exists!")
    conn.close()

def borrow_book(barcode, membership_id):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM books WHERE barcode=?', (barcode,))
    book = cursor.fetchone()
    cursor.execute('SELECT id FROM members WHERE membership_id=?', (membership_id,))
    member = cursor.fetchone()
    if book and member:
        cursor.execute('INSERT INTO transactions (book_id, member_id, borrow_date) VALUES (?, ?, ?)', 
                       (book[0], member[0], datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        conn.commit()
        messagebox.showinfo("Success", "Book borrowed successfully!")
    else:
        messagebox.showerror("Error", "Invalid book barcode or membership ID!")
    conn.close()

def return_book(barcode):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM books WHERE barcode=?', (barcode,))
    book = cursor.fetchone()
    if book:
        cursor.execute('UPDATE transactions SET return_date=? WHERE book_id=? AND return_date IS NULL', 
                       (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), book[0]))
        conn.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Success", "Book returned successfully!")
        else:
            messagebox.showerror("Error", "Book not currently borrowed!")
    else:
        messagebox.showerror("Error", "Invalid book barcode!")
    conn.close()
