from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():


    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [(choice(letters)) for _ in range(randint(8, 10))]
    password_symbols = [(choice(symbols)) for _ in range(randint(2, 4))]
    password_numbers = [(choice(numbers)) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    generated_password = "".join(password_list)
    password.delete(0, END)
    password.insert(0, generated_password)
    pyperclip.copy(generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website_data = website.get()
    user_data = user.get()
    password_data = password.get()
    new_data = {
        website_data: {
            'user': user_data,
            'password': password_data,
        }
    }

    if len(website_data) == 0 or len(password_data) == 0: #this is superfluous as we prefill user entry()
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
        return

    # is_ok = messagebox.askokcancel(title=website_data, message=f"These are the details entered: \nEmail: {user_data} "
    #                                                    f"\nPassword: {password_data} \nIs it ok to save?")
    else:
        try:
            with open('data.json', 'r') as data_file:
                #reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open('data.json', 'w') as data_file2:
                json.dump(new_data, data_file2, indent=4)

        else:
            #update old data with new data
            data.update(new_data)

            with open('data.json', 'w') as data_file3:
                #saving updated data
                json.dump(data, data_file3, indent=4)

        finally:
            website.delete(0, END)
            password.delete(0, END)

# ---------------------------- SEARCH DATA ------------------------------- #

def search():
    website_data = website.get()
    try:
        with open('data.json', 'r') as data_file:
            database = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="No data file found")

    else:
        if website_data in database:
            data = database.get(website_data)
            messagebox.showinfo(title=website_data, message=f"Email: {data['user']}\nPassword: {data['password']}")
            website.delete(0, END)
        else:
            messagebox.showerror(title="Oops", message=f"No details for {website_data} exists")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky='e')
website = Entry()
website.grid(column=1, row=1, columnspan=2, sticky='ew')
website.focus()

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2, sticky='e')
user = Entry()
user.grid(column=1, row=2, columnspan=2, sticky='ew')
user.insert(0, "loscakes@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky='e')
password = Entry()
password.grid(column=1, row=3, sticky='ew')

generate = Button(text="Generate Password", command=generate)
generate.grid(column=2, row=3)

add = Button(text="Add", command=save, width=35)
add.grid(column=1, row=4, columnspan=2, sticky='ew')

search = Button(text="Search", command=search)
search.grid(column=2, row=2, columnspan=2, sticky='ew')

window.mainloop()
