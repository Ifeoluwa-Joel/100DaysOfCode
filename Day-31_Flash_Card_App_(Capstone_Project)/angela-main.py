from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}

try:
    data = pandas.read_csv("words_to_learn_2.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill='black')
    canvas.itemconfig(card_word, text=current_card["French"], fill='black')
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn_2.csv", index=False)

    next_card()


window = Tk()
window.title("Flash Card App")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="card_front.png")
card_back_img = PhotoImage(file="card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 35, "normal"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


# Buttons
wrong_img = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=next_card)
wrong_button.grid(row=1, column=0)
right_img = PhotoImage(file="right.png")
right_button = Button(image=right_img, highlightthickness=0, borderwidth=0, command=is_known)
right_button.grid(row=1, column=1)


next_card()


window.mainloop()
