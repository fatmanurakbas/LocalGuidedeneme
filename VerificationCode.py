import tkinter as tk
from tkinter import messagebox
from create_new_password import create_new_password_screen  # 🔄 Burada yönlendirme yapıyoruz

def go_to_create_password():
    if all(entry.get() for entry in code_entries):
        messagebox.showinfo("Success", "Code verified successfully!")
        root.destroy()
        create_new_password_screen()  # Artık dış dosyadan geliyor
    else:
        messagebox.showwarning("Warning", "Please enter all 4 digits.")

def resend_code():
    messagebox.showinfo("Resend Code", "Verification code has been resent to your email.")

def verification_code_screen():
    global root, code_entries
    root = tk.Tk()
    root.title("Verification Code")
    root.geometry("400x400")
    root.configure(bg="#5CCBF0")

    title = tk.Label(root, text="Check your email!", font=("Helvetica", 24), fg="white", bg="#5CCBF0")
    title.pack(pady=30)

    label = tk.Label(root, text="Enter verification code", fg="white", bg="#5CCBF0", font=("Helvetica", 14))
    label.pack()

    code_frame = tk.Frame(root, bg="#5CCBF0")
    code_frame.pack(pady=20)

    code_entries = []
    for _ in range(4):
        entry = tk.Entry(code_frame, width=3, font=("Helvetica", 24), justify="center")
        entry.pack(side="left", padx=5)
        code_entries.append(entry)

    send_btn = tk.Button(root, text="Send", bg="#1B2C49", fg="white", font=("Helvetica", 14, "bold"),
                         width=20, command=go_to_create_password)
    send_btn.pack(pady=15)

    resend_label = tk.Label(root, text="Didn't receive a code?", fg="white", bg="#5CCBF0")
    resend_label.pack()

    resend_btn = tk.Button(root, text="Resend", bg="#5CCBF0", fg="white", relief="flat", command=resend_code)
    resend_btn.pack()

    root.mainloop()


# Ekranı başlat
if __name__ == "__main__":
    verification_code_screen()
