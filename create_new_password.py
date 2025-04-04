# create_new_password.py
import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

def go_to_password_changed():
    messagebox.showinfo("Password Changed", "Şifreniz başarıyla değiştirildi.")
    root.destroy()

# Pencere oluştur
root = tk.Tk()python create_new_password.py
root.title("Create New Password")
root.geometry("400x500")
root.configure(bg='#5CCBF0')

# Başlık
title = tk.Label(root, text="Create new\npassword!", bg="#5CCBF0", fg="white", font=("Helvetica", 24, "bold"))
title.pack(pady=40)

# Yeni şifre
tk.Label(root, text="New Password", bg="#5CCBF0", fg="white", font=("Helvetica", 12)).pack()
new_pass = tk.Entry(root, show="*", font=("Helvetica", 12))
new_pass.pack(pady=10, ipadx=10, ipady=5)

# Şifre tekrar
tk.Label(root, text="Confirm Password", bg="#5CCBF0", fg="white", font=("Helvetica", 12)).pack()
confirm_pass = tk.Entry(root, show="*", font=("Helvetica", 12))
confirm_pass.pack(pady=10, ipadx=10, ipady=5)

# Gönder butonu
tk.Button(root, text="Send", bg="#1B2C49", fg="white", font=("Helvetica", 12, "bold"),
          command=go_to_password_changed, padx=10, pady=5).pack(pady=30)

root.mainloop()
