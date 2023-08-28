from tkinter import *
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    ''' HOW I DID IT
    password_list = [char for char in random.choices(population=letters, k=random.randint(8, 10))]
    random_symbols = [_ for _ in random.choices(population=symbols, k=random.randint(2, 4))]
    random_numbers = [num for num in random.choices(population=numbers, k=random.randint(2, 4))]
    
    password_list.extend(random_symbols)
    password_list.extend(random_numbers)
    
    ANGELA'S VERSION BELOW
    '''
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers  # Concatenate the 3 lists

    random.shuffle(password_list)  # Shuffling list

    random_password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, random_password)
    pyperclip.copy(random_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title='⚠️ Error!', message='One or more fields empty!')
        return
    else:
        okay_to_save = messagebox.askokcancel(title=website, message=f"These are the details entered:\nUsername: "
                                                                     f"{username}\nPassword: {password}\n\nIs it okay to save?")

        if okay_to_save:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            with open("data.txt", "a") as file:
                file.write(f"{website} | {username} | {password}\n")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
username_label = Label(text='Email/Username:')
username_label.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=51)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, pady=3)
username_entry = Entry(width=51)
username_entry.insert(END, 'ifeoluwajoel794@gmail.com')
username_entry.grid(row=2, column=1, columnspan=2, pady=3)
password_entry = Entry(width=33, )
password_entry.grid(row=3, column=1, pady=3)

# Buttons
generate_password = Button(text='Generate Password', command=password_generator)
generate_password.grid(row=3, column=2)
add_password = Button(text='Add', width=43, command=save)
add_password.grid(row=4, column=1, columnspan=2)

window.mainloop()
