# create_account.py
import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

def sign_up():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if not name or not email or not password:
        messagebox.showwarning("Eksik Bilgi", "Lütfen tüm alanları doldurun.")
        return

    # Geçici olarak mesajla bildiriyoruz
    messagebox.showinfo("Kayıt Başarılı", f"Hoş geldin {name}!\nEmail: {email}")
    
    root.destroy()
    if getattr(sys, 'frozen', False):
        script_path = os.path.join(sys._MEIPASS, 'verification.py')  # İleride anasayfa olacak
    else:
        script_path = os.path.abspath("verification.py")

    subprocess.Popen([sys.executable, script_path])

def back_to_login():
    root.destroy()
    if getattr(sys, 'frozen', False):
        script_path = os.path.join(sys._MEIPASS, 'login.py')
    else:
        script_path = os.path.abspath("login.py")

    subprocess.Popen([sys.executable, script_path])

# Ana pencere
root = tk.Tk()
root.title("Create Account")
root.geometry("400x550")
root.configure(bg='#5CCBF0')

# Başlık
title = tk.Label(root, text="Create account!", bg="#5CCBF0", fg="white", font=("Helvetica", 24, "bold"))
title.pack(pady=30)

# Giriş alanları
tk.Label(root, text="Name", bg="#5CCBF0", fg="white", font=("Helvetica", 12)).pack()
name_entry = tk.Entry(root, font=("Helvetica", 12))
name_entry.pack(pady=8, ipadx=10, ipady=5)

tk.Label(root, text="Email", bg="#5CCBF0", fg="white", font=("Helvetica", 12)).pack()
email_entry = tk.Entry(root, font=("Helvetica", 12))
email_entry.pack(pady=8, ipadx=10, ipady=5)

tk.Label(root, text="Password", bg="#5CCBF0", fg="white", font=("Helvetica", 12)).pack()
password_entry = tk.Entry(root, show="*", font=("Helvetica", 12))
password_entry.pack(pady=8, ipadx=10, ipady=5)

# Kayıt butonu
tk.Button(root, text="Sign Up", bg="#1B2C49", fg="white", font=("Helvetica", 12, "bold"),
          command=sign_up, padx=10, pady=5).pack(pady=20)

# Girişe geri dön
footer_frame = tk.Frame(root, bg='#5CCBF0')
footer_frame.pack(pady=10)
tk.Label(footer_frame, text="Already have an account?", bg='#5CCBF0', fg='white').pack(side='left')
tk.Button(footer_frame, text="Log in", bg='#5CCBF0', fg='white', font=("Helvetica", 10, "bold"),
          borderwidth=0, command=back_to_login).pack(side='left')

root.mainloop()