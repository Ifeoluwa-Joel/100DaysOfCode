from tkinter import *

window = Tk()
window.minsize(width=500, height=500)
window.title("Test-Bed")



entry = Entry(width=15)
entry.pack()
entry.insert(index=END, string='Email')

text = Text(height=5, width=50)
text.insert(END, "The pain itself is important to the main adipisicing elite. Extremely flexible The annoyances which"
                 " even the advantage must be repudiated are the result of the pleasures of toil never let any one of "
                 "them flatter him.")
text.focus()
text.pack()


# Spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=20, width=2, command=spinbox_used)
spinbox.pack()


# Scale
def scale_slid(value):
    print(value)

scale = Scale(from_=0, to=10, command=scale_slid)
scale.pack()


# Checkbox
def checkbutton_used():
    """
    prints 1 if checkbox is ON or 0 if otherwise
    """
    print(checked_state.get())

checked_state = IntVar()
check_button = Checkbutton(text='Print on two sides', variable=checked_state, command=checkbutton_used)
check_button.pack()


# Radiobutton
def radio_used():
    """
    print 1 if 'male' or 2 if choice is 'female'
    """
    print(radio_variable.get())
radio_variable = IntVar()
radio_1 = Radiobutton(text='Male', variable=radio_variable, value=1, command=radio_used)
radio_2 = Radiobutton(text='Female', value=2, variable=radio_variable, command=radio_used)
radio_1.pack()
radio_2.pack()


# List Boxes
def listbox_used(event):
    print(club_listbox.get(club_listbox.curselection()))

club_listbox = Listbox(height=4)
clubs = ['Chelsea', 'Manchester City', 'Liverpool', 'Arsenal']
for club in clubs:
    club_listbox.insert(clubs.index(club), club)
club_listbox.bind("<<ListboxSelect>>", listbox_used)
club_listbox.pack()

window.mainloop()
