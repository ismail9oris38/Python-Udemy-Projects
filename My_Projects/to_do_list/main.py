from tkinter import *
from tkinter import messagebox

ROW = 1
tasks_list = []
completed_list = []

# ---------------------------- COMPlETED TASKS -------------------------------- #

def check_button(task, checkbutton):
    completed_list.append(task)
    with open("completed_file.txt", "a") as file:
        file.write(task + "\n")
    checkbutton.destroy()

    with open("task_file.txt", "w") as data:
        for i in tasks_list:
            if i not in completed_list:
                data.write(i + "\n")

def show_completed():
    if not completed_list:
        messagebox.showinfo("Completed Tasks", "No tasks completed yet.")
    else:
        messagebox.showinfo("Completed Tasks", "\n".join(completed_list))

# ---------------------------- ADD TASKS -------------------------------- #

def add_task():
    global ROW
    task = add_tasks_entry.get().strip()

    if not task:
        messagebox.showinfo(title="Warning", message="No Tasks")
        return

    if ROW == 1:
        canvas.destroy()

    tasks_list.append(task)

    checkbutton = Checkbutton(text=task, width=50, anchor="w", font=("Arial", 12))
    checkbutton.config(command=lambda: check_button(task, checkbutton))
    checkbutton.grid(row=ROW, column=0, columnspan=2, pady=2, sticky="w")

    with open("task_file.txt", "w") as data:
        for i in tasks_list:
            if i not in completed_list:
                data.write(i + "\n")

    ROW += 1
    add_tasks_entry.delete(0, END)
    add_tasks_entry.grid(row=ROW + 1, column=0, pady=10)
    task_add_button.grid(row=ROW + 1, column=1, padx=5)
    completed_button.grid(row=ROW + 2, column=0, columnspan=2, pady=(5, 0))

# ---------------------------- UI SETUP --------------------------------- #

window = Tk()
window.title("ToDo List")
window.config(padx=30, pady=30)

no_task_image = PhotoImage(file="no_tasks_yet_.png")

try:
    with open("completed_file.txt") as completed_file:
        for line in completed_file:
            completed_list.append(line.strip())
except FileNotFoundError:
    pass

try:
    with open("task_file.txt") as task_file:
        tasks = task_file.readlines()
except FileNotFoundError:
    canvas = Canvas(width=256, height=256)
    canvas.create_image(128, 128, image=no_task_image)
    canvas.grid(row=ROW, column=0, columnspan=2)
else:
    for task in tasks:
        task = task.strip()
        if task in completed_list:
            continue
        tasks_list.append(task)

        checkbutton = Checkbutton(text=task, width=30, anchor="w", font=("Arial", 12))
        checkbutton.config(command=lambda t=task, cb=checkbutton: check_button(t, cb))
        checkbutton.grid(row=ROW, column=0, columnspan=2, pady=2, sticky="w")
        ROW += 1

task_label = Label(text="TASKS", font=("Arial", 24, "bold"))
task_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

add_tasks_entry = Entry(width=30, font=("Arial", 15))
add_tasks_entry.grid(row=ROW + 1, column=0, pady=10)

task_add_button = Button(text="Add", command=add_task, font=("Arial", 15, "bold"), width=10)
task_add_button.grid(row=ROW + 1, column=1, padx=5)

completed_button = Button(text="Completed", command=show_completed, font=("Arial", 13), width=50)
completed_button.grid(row=ROW + 2, column=0, columnspan=2, pady=(5, 0))

window.mainloop()