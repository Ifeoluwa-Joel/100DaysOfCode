import requests
from tkinter import *

FONT = ("Arial", 15, "bold")


def spawn_quote():
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    quote = response.json()["quote"]
    canvas.itemconfig(quote_on_canvas, text=quote)


window = Tk()
window.title("Kanye says...")
window.config(padx=50, pady=50, bg="#FBF0B2")

canvas = Canvas(width=300, height=414, highlightthickness=0, bg="#FBF0B2")
quote_background = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=quote_background)
quote_on_canvas = canvas.create_text(150, 180, text="Press Kanye's head.\nHe will say something batshit crazy",
                                     font=FONT, width=250, justify="center", fill="white")
canvas.grid(row=0, column=0)

kanye_button = Button(command=spawn_quote, highlightthickness=0, relief="flat", bg="#FBF0B2",
                      activebackground="#FBF0B2")
kanye_button_thumbnail = PhotoImage(file="kanye.png")
kanye_button.config(image=kanye_button_thumbnail)
kanye_button.grid(row=1, column=0)
window.bind('<Return>', lambda event: spawn_quote())

window.mainloop()
