from tkinter import *

FONT_NAME = 'Poppins'


# TIMER
def timer(count):
    timer_min = count // 60
    timer_sec = count % 60
    timer_hour = timer_min // 60

    canvas.itemconfig(timer_text, text=f"{timer_hour}:{timer_min}:{timer_sec}")
    window.after(1000, timer, count + 1)


def start_timer():
    timer(3595)


# Does not really work, yet
def reset_timer():
    canvas.itemconfig(timer_text, text=f"0:00:00")


# UI DESIGN
window = Tk()
window.title('Stopwatch')
window.config(padx=50, pady=50, bg='light yellow')


canvas = Canvas(width=512, height=512, bg='light yellow', highlightthickness=0)
stopwatch_img = PhotoImage(file='stopwatch.png')
canvas.create_image(256, 256, image=stopwatch_img)
timer_text = canvas.create_text(256, 295, text="00:00", fill='black', font=(FONT_NAME, 60, 'bold'))


canvas.grid(column=1, row=1)

start_button = Button(text='Start', command=start_timer)
start_button.grid(column=0, row=2, pady=10)

reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(column=0, row=3)

window.mainloop()
