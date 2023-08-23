# FINAL PROJECT
# Mile to KM Converter
'''
My solution. Works well, except the clear button is a dud. It does not do anything.
See Angela's approach in mile-to-km-angela.py
'''
import tkinter as tk


def calculate_clicked():
    mile_value = int(float(prompt.get()))
    km_value = round(mile_value * 1.609, 2)
    result_label.config(text=km_value)


def clear_clicked():
    prompt.config()


window = tk.Tk()
window.title('Mile to Km Converter')
window.config(pady=20, padx=20)

prompt = tk.Entry(width=10)
prompt.grid(column=1, row=0, pady=10, padx=10)
mile_label = tk.Label(text='Miles')
mile_label.grid(column=2, row=0)
equal_info = tk.Label(text='is equal to')
equal_info.grid(column=0, row=1)
result_label = tk.Label(text='0')
result_label.grid(column=1, row=1)
km_label = tk.Label(text='Km')
km_label.grid(column=2, row=1)

calculate = tk.Button(text='Calculate', command=calculate_clicked)
calculate.grid(column=1, row=2)
clear_button = tk.Button(text='Clear', bg='green', fg='white', command=clear_clicked)
clear_button.grid(column=2, row=2)
exit_ = tk.Button(text='Quit', bg='red', fg='white', command=window.destroy)
exit_.grid(column=1, row=3, pady=10)

window.mainloop()

