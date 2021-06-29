from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "" or password == "":
        field_empty = messagebox.showinfo(title="Oops", message="Some of the fields are empty")

    else:
        save_info = messagebox.askyesno(title=website, message=f"These are details: \nemail: {email}\npassword: {password}\nAre you sure to proceed?")
        if save_info:
            with open("Password_Manager_Data.txt", "a") as data:
                data.write(f"{website} | {email} | {password}\n")
            website_entry.delete(first=0, last=END)
            password_entry.delete(first=0, last=END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website")
website_label.grid(column=0, row=1, sticky="w")

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, pady=5, sticky="w")

email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2, sticky="w")

email_entry = Entry(width=35)
email_entry.insert(0, "d**d*****francis@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, pady=5, sticky="w")

password_label = Label(text="Password")
password_label.grid(column=0, row=3, sticky="w")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="w")

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=1, row=3, columnspan=2,pady=5, sticky="e")

add_button = Button(text="Add", command=save, width=36)
add_button.grid(column=1, row=4, columnspan=2, pady=5)


window.mainloop()
