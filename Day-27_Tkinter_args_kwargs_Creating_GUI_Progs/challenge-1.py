import tkinter as tk

window = tk.Tk()
window.title("My First TKinter Program")
window.minsize(width=700, height=500)

# Label
my_label = tk.Label(text="I AM A LABEL", font=("Segoe UI", 11, 'bold'))
my_label.pack()


# There are 3 ways to set options in TKinter, we  have done one above on line 8
# https://docs.python.org/3/library/tkinter.html#handy-reference

my_label['text'] = "I am a new text"
my_label.config(text='Another new text', font=("Consolas", 11, 'bold'))

# ENTRY
first_name = tk.Entry()
first_name.pack()


# BUTTON
button_label = tk.Label()


def button_clicked():
    button_label.pack()

    first_name_gotten = first_name.get()
    my_label.config(text=first_name_gotten, fg='red')


button = tk.Button(text="Click me", fg='black', command=button_clicked)
button.pack()


window.mainloop()
