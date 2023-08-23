# THREE LAYOUT MANAGERS
# pack, place, grid
"""
pack stacks widgets in order of creation.
place specifically places a widget at a coordinate. Gets difficult when widgets are many
grid - THE GOAT!
⚠⚠⚠ You can't use grid() and pack() in the same program. Pick a hustle bro.
"""


import tkinter as tk


def button_clicked():
    print(input.get())
    new_text = input.get()
    my_label.config(text=new_text)


window = tk.Tk()
window.minsize(width=500, height=500)
window.title("GUI Program")

my_label = tk.Label(text='I am a Label', font=('Chelsea Basis', 11, 'bold'))
my_label.config(text='New Text', fg='green')
my_label.grid(column=0, row=0)

button = tk.Button(text='Submit', command=button_clicked, bg='green', fg='white')
button.grid(column=2, row=1)

input = tk.Entry(width=20)
input.grid(column=0, row=1)


window.mainloop()
