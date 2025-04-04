# password_changed.py
import tkinter as tk
import subprocess
import sys
import os

def show_password_changed_screen():
    root = tk.Tk()
    root.title("Password Changed")
    root.geometry("400x500")
    root.configure(bg='#5CCBF0')

    frame = tk.Frame(root, bg='#5CCBF0')
    frame.pack(expand=True)

    title = tk.Label(frame, text="Password\nchanged\nsuccessfully", bg="#5CCBF0", fg="white",
                     font=("Helvetica", 26, "bold"), justify='center')
    title.pack(pady=30)

    def go_to_login():
        root.destroy()
        if getattr(sys, 'frozen', False):
            script_path = os.path.join(sys._MEIPASS, 'login.py')
        else:
            script_path = os.path.abspath("login.py")
        subprocess.Popen([sys.executable, script_path])

    login_btn = tk.Button(frame, text="Go to the log in", bg="#1B2C49", fg="white",
                          font=("Helvetica", 14, "bold"), padx=20, pady=10,
                          command=go_to_login)
    login_btn.pack(pady=20)

    root.mainloop()
