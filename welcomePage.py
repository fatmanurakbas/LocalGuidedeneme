import tkinter as tk
from tkinter import messagebox

# Giriş ekranını açan fonksiyon
def open_login():
    root.destroy()  # Ana pencereyi kapat
    import login  # login.py dosyasını çalıştır

# Kayıt olma ekranını açan fonksiyon
def open_signup():
    root.destroy()  # Ana pencereyi kapat
    import sign_up  # signup.py dosyasını çalıştır

# Ana pencere
root = tk.Tk()
root.title("Local Guide")
root.geometry("350x600")
root.configure(bg="#5CCBF0")
root.resizable(False, False)

# Başlık
label_title = tk.Label(root, text="LOCAL GUIDE", font=("Arial", 30, "bold"), bg="#5CCBF0")
label_title.pack(pady=50)


label_subtitle = tk.Label(root, text="WELCOME TO LOCALGUIDE!", font=("Arial", 12), bg="#5CCBF0")
label_subtitle.pack(pady=50)

# Butonlar
button_login = tk.Button(root, text="Log in", font=("Arial", 14), bg="#1B2C49", fg="white", width=15, command=open_login)
button_login.pack(pady=10)

button_signup = tk.Button(root, text="Sign up", font=("Arial", 14), bg="#1B2C49", fg="white", width=15, command=open_signup)
button_signup.pack(pady=20)

# Uygulamayı başlat
root.mainloop()
