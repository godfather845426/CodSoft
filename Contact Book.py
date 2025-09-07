import tkinter as tk
from tkinter import messagebox
import json
import os

contacts = {}

DATA_FILE = "contacts.json"

def load_contacts():
    global contacts
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            contacts = json.load(f)

def save_contacts():
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()

    if name == "" or phone == "":
        messagebox.showwarning("Required", "Name and Phone are required.")
        return

    contacts[name] = {"phone": phone, "address": address}
    save_contacts()
    update_list()
    clear_fields()

def update_contact():
    selected = contact_listbox.curselection()
    if not selected:
        messagebox.showinfo("Info", "Please select a contact to update.")
        return

    name = contact_listbox.get(selected)
    if name in contacts:
        contacts[name]["phone"] = phone_entry.get()
        contacts[name]["address"] = address_entry.get()
        save_contacts()
        update_list()
        clear_fields()
        
def delete_contact():
    selected = contact_listbox.curselection()
    if not selected:
        messagebox.showinfo("Info", "Please select a contact to delete.")
        return

    name = contact_listbox.get(selected)
    if name in contacts:
        del contacts[name]
        save_contacts()
        update_list()
        clear_fields()

def search_contact():
    query = search_entry.get().lower()
    contact_listbox.delete(0, tk.END)
    for name in contacts:
        if query in name.lower() or query in contacts[name]["phone"]:
            contact_listbox.insert(tk.END, name)

def update_list():
    contact_listbox.delete(0, tk.END)
    for name in contacts:
        contact_listbox.insert(tk.END, name)

def show_contact(event):
    selected = contact_listbox.curselection()
    if not selected:
        return

    name = contact_listbox.get(selected)
    contact = contacts.get(name, {})
    name_entry.delete(0, tk.END)
    name_entry.insert(0, name)
    phone_entry.delete(0, tk.END)
    phone_entry.insert(0, contact.get("phone", ""))
    address_entry.delete(0, tk.END)
    address_entry.insert(0, contact.get("address", ""))

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Contact Book")
root.geometry("500x500")
root.resizable(False, False)

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=50)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root, width=50)
phone_entry.pack()

tk.Label(root, text="Address").pack()
address_entry = tk.Entry(root, width=50)
address_entry.pack()

tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact).pack()
tk.Button(root, text="Delete Contact", command=delete_contact).pack()

tk.Label(root, text="Search by Name/Phone").pack(pady=(10,0))
search_entry = tk.Entry(root, width=30)
search_entry.pack()
tk.Button(root, text="Search", command=search_contact).pack(pady=5)

contact_listbox = tk.Listbox(root, width=50)
contact_listbox.pack(pady=10)
contact_listbox.bind('<<ListboxSelect>>', show_contact)

load_contacts()
update_list()

root.mainloop()