# forgot_password.py
import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

def send_verification():
    email = email_entry.get()
    if not email:
        messagebox.showwarning("Uyarı", "Lütfen email adresinizi girin.")
        return
    root.destroy()
    # Verification ekranına yönlendirme
    if getattr(sys, 'frozen', False):
        script_path = os.path.join(sys._MEIPASS, 'VerificationCode.py')
    else:
        script_path = os.path.abspath("VerificationCode.py")

    subprocess.Popen([sys.executable, script_path])

def back_to_login():
    root.destroy()
    if getattr(sys, 'frozen', False):
        script_path = os.path.join(sys._MEIPASS, 'login.py')
    else:
        script_path = os.path.abspath("login.py")

    subprocess.Popen([sys.executable, script_path])

# Pencere
root = tk.Tk()
root.title("Forgot Password")
root.geometry("400x500")
root.configure(bg='#5CCBF0')

# Başlık
title = tk.Label(root, text="Forgot password?", bg="#5CCBF0", fg="white", font=("Helvetica", 24, "bold"))
title.pack(pady=40)

# E-posta alanı
tk.Label(root, text="Enter Email Address", bg="#5CCBF0", fg="white", font=("Helvetica", 12)).pack()
email_entry = tk.Entry(root, font=("Helvetica", 12))
email_entry.pack(pady=10, ipadx=10, ipady=5)

# Gönder Butonu
tk.Button(root, text="Send", bg="#1B2C49", fg="white", font=("Helvetica", 12, "bold"),
          command=send_verification, padx=10, pady=5).pack(pady=30)

# Geri dön Butonu
tk.Button(root, text="Back to log in", bg="#5CCBF0", fg="white", font=("Helvetica", 10, "underline"),
          borderwidth=0, command=back_to_login).pack()

root.mainloop()
