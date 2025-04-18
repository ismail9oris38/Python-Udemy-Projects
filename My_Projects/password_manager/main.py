from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = web_entry.get()
    email = mail_entry.get()
    password = password_entry.get()
    new_data = {
        website : {
            "email" : email,
            "password" : password
        }
    }

    if website and email and password:
        is_ok = messagebox.askokcancel(title="Your Sure",message=f"These are the details entered: \n Website: {website} \nEmail: {email}"
                                                                 f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file: # noqa
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file: # noqa
                    json.dump(data, data_file, indent=4)
            finally:
                web_entry.delete(0,END)
                password_entry.delete(0, END)

    else:
        messagebox.showinfo(title="Warning", message="Please don't leave any fields empty!")

# ---------------------------- FİND PASSWORD ------------------------------- #

def find_password():
    website = web_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
        email, password = data[website]["email"], data[website]["password"]
    except KeyError:
        messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file Found.")
    else:
        messagebox.showinfo(title=website.strip(), message=f"Email: {email}\nPassword: {password}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

lock = PhotoImage(file="logo.png")

kanvas = Canvas(width=200,height=200)
kanvas.create_image(100,100,image=lock)
kanvas.grid(row=0,column=1)

web = Label(text="Website:")
web.grid(row=1,column=0)

mail = Label(text="Email/Username:")
mail.grid(row=2,column=0)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)


#label
web_entry = Entry(width=21)
web_entry.grid(row=1,column=1)
web_entry.focus()

mail_entry = Entry(width=38)
mail_entry.grid(row=2,column=1,columnspan=2)
mail_entry.insert(0,"ismailorhan831@gamil.com")

password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

#Button
password_search = Button(text="Search", command=find_password,width=13)
password_search.grid(row=1,column=2)

generate_button = Button(text="Generate Password",command=generate_password,width=13)
generate_button.grid(row=3,column=2)

add_button = Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()