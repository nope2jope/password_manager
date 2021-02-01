from tkinter import *
import pyperclip
from tkinter import messagebox
from password_jenny import jenny
import json

DEF_USE = "yikes.okay.dad@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def improv():
    password_label_entry.delete(0, END)
    new_pass = jenny()
    pyperclip.copy(new_pass)
    password_label_entry.insert(0, new_pass)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    website = web_entry.get()
    username = email_user_entry.get()
    new_password = password_label_entry.get()
    new_data= {
        website: {
            "email": username,
            "password":new_password,
        }}

    if len(website) == 0 or len(new_password) == 0:
        messagebox.showerror("E R R O R", "Please do not leave fields empty.")
    else:
        proceed = messagebox.askokcancel("Confirmation requested", f"Please confirm the information below. "
                                                                   f"\nDesired website: {website}"
                                                                   f"\nDesired username: {username}"
                                                                   f"\nDesired password: {new_password}")
        if not proceed:
            return
        try:
            with open("data.json", "r") as data_file:
                # read
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                # update
                data.update(new_data)
                json.dump(data, data_file, indent=4)
        finally:
            password_label_entry.delete(0, END)
            web_entry.delete(0, END)
            email_user_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# window, canvas

window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# input labels

web_label = Label(text="Website: ")
web_label.grid(row=1, column=0)

email_user_label = Label(text="Email/Username: ")
email_user_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# input fields

web_entry = Entry(width=20)
web_entry.grid(row=1, column=1)
web_entry.focus()

email_user_entry = Entry(width=35)
email_user_entry.insert(END, DEF_USE)
email_user_entry.grid(row=2, column=1, columnspan=2)

password_label_entry = Entry(width=20)
password_label_entry.grid(row=3, column=1)

# buttons

def search():
    key = web_entry.get()
    try:
        with open("data.json", "r") as data_file:
            booby = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="File not found", message="Error: No such entry exists")
    else:
        for entry in booby:
            if entry == key:
                mail = booby[key]['email']
                pw = booby[key]['password']

                ok_message = messagebox.showinfo(title="ok then", message=f"Email/username: {mail}\n"
                                                                          f"Password: {pw}\n")
            else:
                messagebox.showerror(title="Key error", message="Error: No such entry exists")

search_button = Button(text="Search", command=search, width=14)
search_button.grid(row=1, column=2)

generate_button = Button(text="Generate Password", command=improv)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()