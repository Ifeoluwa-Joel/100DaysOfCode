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


window.mainloop()


# import tkinter as tk
#
# window = tk.Tk()
# window.minsize(width=600, height=600)
#
# heading = tk.Label(text="BIO-DATA FORM", font=('Poppins', 18, 'bold'), fg='green')
# heading.pack()
#
# first_name = tk.Entry()
# first_name.pack()
# first_name_gotten = first_name.get()
#
#
# def submit_button():
#     info_text = tk.Label(text=f"Your first name is {first_name_gotten}")
#     info_text.pack()
#
#
# submit = tk.Button(text='Submit', fg='green', command=submit_button)
# submit.pack()
#
# window.mainloop()
#
