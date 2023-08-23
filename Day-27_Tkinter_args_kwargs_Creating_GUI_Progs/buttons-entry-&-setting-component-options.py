import tkinter as tk

window = tk.Tk()
window.title("My First TKinter Program")
window.minsize(width=700, height=500)

# Label
my_label = tk.Label(text="I AM A LABEL", font=("SegoeUI", 11, 'bold'))
my_label.pack()

# There are 3 ways to set options in TKinter, we  have done one above on line 8
# https://docs.python.org/3/library/tkinter.html#handy-reference

my_label['text'] = "I am a new text"
my_label.config(text='Another new text')


# BUTTON
button_label = tk.Label(text='Please wait. Processing...')


def button_clicked():
    button_label.pack()
    input = first_name.get()
    my_label.config(text=input, fg='red')


button = tk.Button(text="Click me", fg='black', command=button_clicked)
button.pack()


# ENTRY
first_name = tk.Entry()
first_name.pack()



window.mainloop()
