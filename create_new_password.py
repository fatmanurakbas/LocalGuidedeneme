# create_new_password.py
import tkinter as tk
from password_changed import show_password_changed_screen  # 👈 Bunu ekle

def create_new_password_screen():
    root = tk.Tk()
    root.title("Create New Password")
    root.geometry("400x400")
    root.configure(bg="#5CCBF0")

    label = tk.Label(root, text="Create new password!", font=("Helvetica", 24), fg="white", bg="#5CCBF0")
    label.pack(pady=40)

    tk.Label(root, text="New Password", fg="white", bg="#5CCBF0").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=5)

    tk.Label(root, text="Confirm Password", fg="white", bg="#5CCBF0").pack()
    confirm_entry = tk.Entry(root, show="*")
    confirm_entry.pack(pady=5)

    def submit():
        if password_entry.get() == confirm_entry.get() and password_entry.get():
            root.destroy()
            show_password_changed_screen()  # 👈 Şifre değişince yönlendir
        else:
            tk.messagebox.showerror("Error", "Passwords do not match or are empty!")

    submit_btn = tk.Button(root, text="Submit", bg="#1B2C49", fg="white", command=submit)
    submit_btn.pack(pady=30)

    root.mainloop()
