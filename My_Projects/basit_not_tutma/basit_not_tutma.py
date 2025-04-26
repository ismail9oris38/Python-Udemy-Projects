from tkinter import *
from tkinter import messagebox, filedialog
import os

# ---------------------------- MENU --------------------------------- #

tmp = 1
file_name = "Not Defteri"
new_button = None
open_button = None
save_button = None
exit_button = None

def menu():
    global tmp, new_button, open_button, save_button, exit_button

    if tmp > 0:
        tmp = -1
        new_button = Button(text="New", width=15, height=2, command=new)
        open_button = Button(text="Open", width=15, height=2, command=open_file)
        save_button = Button(text="Save", width=15, height=2, command=save)
        exit_button = Button(text="Exit", width=15, height=2, command=exit_programing)

        new_button.grid(row=1, column=0, pady=5)
        open_button.grid(row=2, column=0, pady=5)
        save_button.grid(row=3, column=0, pady=5)
        exit_button.grid(row=4, column=0, pady=5)

    else:
        tmp = 1
        new_button.destroy()
        open_button.destroy()
        save_button.destroy()
        exit_button.destroy()

def new(event=None):
    text.delete(1.0, END)

def open_file(event=None):
    global file_name

    new()
    file_name = filedialog.askopenfilename(
        title="Open a text file",
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
    )
    if file_name:
        window.title(os.path.basename(file_name))
        with open(file_name, "r") as data:
            file = data.read()
            text.insert(1.0, file)

def save(event=None):
    global file_name

    if text.get(1.0, END).strip():
        file_name = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
        )
        if file_name:
            window.title(os.path.basename(file_name))
            with open(file_name, "w") as file:
                file.write(text.get(1.0, END).strip())

    else:
        messagebox.showinfo(title="Warning", message="Text is empty")

def exit_programing():
    is_on = True
    if text.get(1.0, END).strip():
        is_on = messagebox.askokcancel(title="Warning", message="Text isn't saved, are you sure you want to exit?")
    if is_on:
        window.destroy()

# ---------------------------- UI SETUP --------------------------------- #

window = Tk()
window.title(file_name)
window.config(padx=20, pady=20)

window.bind("<Command-n>", new)
window.bind("<Command-o>", open_file)
window.bind("<Command-s>", save)

menu_button = Button(text="MENU", width=15, height=2, command=menu)
menu_button.grid(row=0, column=0, pady=10)

text = Text(width=70, height=25, font=("Arial", 12))
text.focus()
text.grid(row=0, column=1, rowspan=100, padx=20)

window.mainloop()
