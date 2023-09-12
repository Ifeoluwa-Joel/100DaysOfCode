from tkinter import *
from tkinter import messagebox
import pandas
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Poppins"
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("french_words.csv")
finally:
    to_learn = data.to_dict(orient="records")
current_card = {}


# --------------------- CREATE NEW FLASH CARDS --------------
def new_flash_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    new_word = current_card["French"]
    canvas.itemconfig(card_background, image=front_card_img)
    canvas.itemconfig(current_language, text="Français", fill="#000000")
    canvas.itemconfig(current_word, text=new_word, fill="#000000")
    flip_timer = window.after(3000, flip_card)


# ---------------------- FLIP CARD -----------------------------
def flip_card():
    canvas.itemconfig(card_background, image=back_card_img)
    canvas.itemconfig(current_language, text="English", fill="#ffffff")
    canvas.itemconfig(current_word, text=current_card["English"], fill="#ffffff")


# ---------------------- SAVE PROGRESS -------------------------
def remove_known_word():
    global current_card
    to_learn.remove(current_card)  # remove the current card from the list of cards to learn
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("words_to_learn.csv", index=False) # Save the rest to a file where we will read from next time
    try:
        new_flash_card()
    except IndexError:
        messagebox.showinfo(title="Congratulations!",
                            message="BRAVO!\nYou have completed the course!")
        os.remove("words_to_learn.csv")  # Delete the file so that when program is run after completion,
        # no error is thrown while attempting to read from an empty file


# --------------------- UI DESIGN -------------------------
window = Tk()
window.title("Flash Card App")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="card_front.png")
back_card_img = PhotoImage(file="card_back.png")
card_background = canvas.create_image(400, 263, image=front_card_img)
current_language = canvas.create_text(400, 150, text="", font=(FONT, 35, "normal"))
current_word = canvas.create_text(400, 263, text="", font=(FONT, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


# Buttons
wrong_img = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=new_flash_card)
wrong_button.grid(row=1, column=0)
right_img = PhotoImage(file="right.png")
right_button = Button(image=right_img, highlightthickness=0, borderwidth=0, command=remove_known_word)
right_button.grid(row=1, column=1)


new_flash_card()

window.mainloop()
