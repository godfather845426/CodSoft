import tkinter as tk
from tkinter import messagebox
import random
import string

PASSWORD_LENGTH = 18

def generate_password():
    charset = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(charset) for _ in range(PASSWORD_LENGTH))
    
    password_output.delete(0, tk.END)
    password_output.insert(0, password)

def copy_to_clipboard():
    pwd = password_output.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Empty", "No password to copy.")

def save_password():
    pwd = password_output.get()
    if pwd:
        with open("saved_passwords.txt", "a") as file:
            file.write(pwd + "\n")
        messagebox.showinfo("Saved", "Password saved to saved_passwords.txt!")
    else:
        messagebox.showwarning("Empty", "No password to save.")

def detect_caps_lock(event=None):
    if root.tk.call("tk", "windowingsystem") == 'win32':
        import ctypes
        caps_state = ctypes.WinDLL("User32.dll").GetKeyState(0x14)
        if caps_state:
            caps_label.config(text="⚠ CAPS LOCK IS ON!", fg="red")
        else:
            caps_label.config(text="")
    else:
        caps_label.config(text="")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.config(bg="#f0f0f0")

title = tk.Label(root, text="🔐 Password Generator", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
title.pack(pady=10)

caps_label = tk.Label(root, text="", font=("Arial", 10, "bold"), bg="#f0f0f0")
caps_label.pack()

password_output = tk.Entry(root, font=("Arial", 14), width=30, justify="center")
password_output.pack(pady=15)
password_output.bind("<KeyPress>", detect_caps_lock)
password_output.bind("<FocusIn>", detect_caps_lock)

generate_btn = tk.Button(root, text="Generate Password", command=generate_password, bg="#27ae60", fg="white", font=("Arial", 12, "bold"))
generate_btn.pack(pady=5)

copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#2980b9", fg="white", font=("Arial", 12, "bold"))
copy_btn.pack(pady=5)

save_btn = tk.Button(root, text="Save Password", command=save_password, bg="#8e44ad", fg="white", font=("Arial", 12, "bold"))
save_btn.pack(pady=5)

root.after(100, detect_caps_lock)

root.mainloop()
