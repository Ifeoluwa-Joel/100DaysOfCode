import tkinter as tk


def button_clicked():
    print(input.get())
    new_text = input.get()
    my_label.config(text=new_text)


window = tk.Tk()
window.minsize(width=500, height=300)
window.title("Challenge Two")
window.config(padx=20, pady=20)

my_label = tk.Label(text='Label', font=('Chelsea Basis', 11, 'bold'))
my_label.config(text='Label', fg='green')
my_label.grid(column=0, row=0)

button = tk.Button(text='Button', command=button_clicked, bg='green', fg='white')
button.grid(column=1, row=1)

new_button = tk.Button(text='New Button', command=button_clicked, bg='green', fg='white')
new_button.grid(column=2, row=0)

input = tk.Entry(width=20)
input.grid(column=3, row=2)


window.mainloop()
