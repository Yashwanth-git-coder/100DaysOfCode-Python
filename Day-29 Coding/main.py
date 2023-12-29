import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_paassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters

    shuffle(password_list)

    password = "".join(password_list)
    password_Entry.insert(0, password)
    pyperclip.copy(password)
# password = ""
# for char in password_list:
#   password += char

    # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_file():

    website = web_Entry.get()
    email = Email_Entry.get()
    password = password_Entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields.")
    else:
        try:
            with open("data.json", "r") as data_files:
                data = json.load(data_files)

                data.update(new_data)

        except FileNotFoundError:

            with open("data.json", "w") as data_files:
                json.dump(new_data, data_files, indent=4)

                # web_Entry.delete(0, END)
                # password_Entry.delete(0, END)

        else:
            with open("data.json", "w") as data_files:
                json.dump(data, data_files, indent=4)

        finally:
            web_Entry.delete(0, END)
            password_Entry.delete(0, END)
# ---------------------------- Find Password ------------------------------- #

def find_password():
    website = web_Entry.get()
    try:
        with open("data.json") as data_files:
            data = json.load(data_files)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Data Form")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200,highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image = logo_img)
canvas.grid(column=1, row=0)

website_lable = Label(text="Website :")
website_lable.grid(column=0, row=1)

web_Entry = Entry(width=17)
web_Entry.grid(column=1, row=1)
web_Entry.focus()

Generate_Button = Button(text="Search", command=find_password, width=16)
Generate_Button.grid(column=2, row=1)

Email_lable = Label(text="Email/Username :")
Email_lable.grid(column=0, row=3)

Email_Entry = Entry(width=35)
Email_Entry.insert(0,"yashwanth7795@gmail.com")
Email_Entry.grid(column=1, row=3, columnspan=2)

password_lable = Label(text="Password :")
password_lable.grid(column=0, row=4)

password_Entry = Entry(width=17)
password_Entry.grid(column=1, row=4)

Generate_Button = Button(text="Generate Password", command=generate_paassword)
Generate_Button.grid(column=2, row=4)

Add_button = Button(text="Add", width=36, command=save_file)
Add_button.grid(column=1, row=5, columnspan=2)

window.mainloop()