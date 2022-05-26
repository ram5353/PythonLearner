from tkinter import *
from random import *
from tkinter import messagebox

FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def random_generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    print(f"Your password is: {password}")
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="information", message="please do not leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(),
                                       message=f"These are the details entered\n""Email: {email_entry.get()}\n""Password: {password_entry.get()}")
        if is_ok:
            with open("passwords.txt", mode="a") as file:
                file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=(FONT_NAME, 15))
email_label = Label(text="Email/Username:", font=(FONT_NAME, 15))
password_label = Label(text="Password:", font=(FONT_NAME, 15))

website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.insert(0, "ramkiran5353@gmail.com")
password_entry = Entry(width=18)

website_entry.grid(column=1, row=1, columnspan=2)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)

generate_password = Button(text="generate password", command=random_generate_password)
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width=33, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
