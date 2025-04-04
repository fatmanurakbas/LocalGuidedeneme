# login.py
import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

def login():
    email = email_entry.get()
    password = password_entry.get()
    # Giriş işlemleri burada yapılabilir
    messagebox.showinfo("Login", f"Giriş yapıldı:\nEmail: {email}")
    
    # Login başarılıysa main.py'yi aç
    root.destroy()  # Login penceresini kapat
    if getattr(sys, 'frozen', False):
        script_path = os.path.join(sys._MEIPASS, 'main.py')
    else:
        script_path = os.path.abspath("main.py")

    subprocess.Popen([sys.executable, script_path])

def forgot_password():
    messagebox.showinfo("Şifre", "Şifrenizi mi unuttunuz?")

def sign_up():
    messagebox.showinfo("Kayıt", "Kayıt sayfasına yönlendiriliyorsunuz...")

# Ana pencere
root = tk.Tk()
root.title("Login")
root.geometry("400x500")
root.configure(bg='#5CCBF0')

# Başlık
title = tk.Label(root, text="Welcome back!", bg="#5CCBF0", fg="white", font=("Helvetica", 24, "bold"))
title.pack(pady=40)

# Email alanı
tk.Label(root, text="Email", bg="#5CCBF0", fg="white", font=("Helvetica", 12)).pack()
email_entry = tk.Entry(root, font=("Helvetica", 12))
email_entry.pack(pady=10, ipadx=10, ipady=5)

# Şifre alanı
tk.Label(root, text="Password", bg="#5CCBF0", fg="white", font=("Helvetica", 12)).pack()
password_entry = tk.Entry(root, show="*", font=("Helvetica", 12))
password_entry.pack(pady=10, ipadx=10, ipady=5)

# Şifreyi unuttum
tk.Button(root, text="Forgot password?", bg="#5CCBF0", fg="white", borderwidth=0, command=forgot_password).pack(anchor='e', padx=30)

# Giriş butonu
tk.Button(root, text="Log in", bg="#1B2C49", fg="white", font=("Helvetica", 12, "bold"),
          command=login, padx=10, pady=5).pack(pady=30)

# Kayıt ol bölümü
footer_frame = tk.Frame(root, bg='#5CCBF0')
footer_frame.pack(pady=10)
tk.Label(footer_frame, text="Don't have an account?", bg='#5CCBF0', fg='white').pack(side='left')
tk.Button(footer_frame, text="Sign up", bg='#5CCBF0', fg='white', font=("Helvetica", 10, "bold"),
          borderwidth=0, command=sign_up).pack(side='left')

root.mainloop()
