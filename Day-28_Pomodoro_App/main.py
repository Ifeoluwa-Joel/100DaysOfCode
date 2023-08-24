from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TITLE_LABEL_FONT_SIZE = 30
reps = 0
timer = None  # None assigned because the type of value we will later assign to this variable is
            # a window.after() object which is found in Tkinter only.


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_label.config(text='Timer', font=(FONT_NAME, 40))
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    cycle_counter.config(text='')

    focus_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_secs)
        timer_label.config(text='Long Break', fg=RED, font=('Courier', TITLE_LABEL_FONT_SIZE))
    elif reps % 2 == 0:
        count_down(short_break_secs)
        timer_label.config(text='Short Break', fg=PINK, font=('Courier', TITLE_LABEL_FONT_SIZE))
    else:
        count_down(focus_secs)
        timer_label.config(text='Work', fg=GREEN, font=('Courier', TITLE_LABEL_FONT_SIZE))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # count_min = count // 60
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(10, count_down, count - 1)
    else:
        start_timer()  # Recall the timer after a session. The function will decide how many minutes to run for

        marks = ''
        every_other_work_session = math.floor(reps / 2)  # math.floor is necessary so that we don't get floats here
        for _ in range(every_other_work_session):  # floats can't be used in range, hence math.floor in prev line
            marks += '✔'
            cycle_counter.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(pady=50, padx=100, bg=YELLOW)

timer_label = Label(text='Timer', font=(FONT_NAME, 40, 'normal'), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', font=(FONT_NAME, 30, 'bold'), fill='white')
canvas.grid(row=1, column=1)

start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

cycle_counter = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15))
cycle_counter.grid(row=3, column=1)

quit_button = Button(text='Quit', command=window.destroy)
quit_button.grid(row=4, column=1)


window.mainloop()
