from tkinter import *
import pandas
import random

# ---------------------------- Functions ------------------------------- #

def flash():
    canvas_france.itemconfig(canvas_img, image=card_back_image)
    canvas_france.itemconfig(language_text, text="English", fill="white")
    canvas_france.itemconfig(word_text, text=current_card["English"], fill="white")

def next_card():
    global current_card,flash_timer
    window.after_cancel(flash_timer)
    current_card = random.choice(to_learn)
    canvas_france.itemconfig(canvas_img, image=card_front_image)
    canvas_france.itemconfig(language_text, text="French", fill="black")
    canvas_france.itemconfig(word_text, text=current_card["French"], fill="black")
    flash_timer = window.after(3000, flash)

def right_change():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()

def wrong_change():
    next_card()

# ---------------------------- DATA ------------------------------- #

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
current_card = {}

# ---------------------------- UI SETUP ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")

canvas_france = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img = canvas_france.create_image(400, 263, image=card_front_image)
language_text = canvas_france.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"))
word_text = canvas_france.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas_france.grid(row=0, column=0, columnspan=2)

flash_timer = window.after(3000, flash)

button_right = Button(image=right_image, highlightthickness=0, command=right_change)
button_right.grid(row=1, column=1)

button_wrong = Button(image=wrong_image, highlightthickness=0, command=wrong_change)
button_wrong.grid(row=1, column=0)

next_card()

window.mainloop()