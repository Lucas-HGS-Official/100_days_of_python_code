# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
import random
import tkinter as tk
from tkinter import messagebox

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

for char in range(nr_letters):
    password_list.append(random.choice(letters))

for char in range(nr_symbols):
    password_list += random.choice(symbols)

for char in range(nr_numbers):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_credentials():
    website = website_entry.get()
    username = user_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        _ = messagebox.showinfo(title="Error", message="Please fill all fields.")
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"Are these your credentials?\nEmail: {username}\nPassword: {password}",
        )
        if is_ok:
            with open("data.txt", "a") as data_file:
                _ = data_file.write(f"{website} | {username} | {password}\n")
                website_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #


if __name__ == "__main__":
    window = tk.Tk()
    _ = window.config(padx=50, pady=50)

    # Logo #
    canvas = tk.Canvas(width=165, height=200)
    logo_img = tk.PhotoImage(file="logo.png")
    _ = canvas.create_image(100, 100, image=logo_img)
    canvas.grid(column=1, row=0)
    ########

    # Label #
    website_label = tk.Label(text="Website:")
    website_label.grid(column=0, row=1)

    user_label = tk.Label(text="Email/Username:")
    user_label.grid(column=0, row=2)

    password_label = tk.Label(text="Password:")
    password_label.grid(column=0, row=3)
    ########

    # Entry #
    website_entry = tk.Entry(width=37)
    website_entry.focus()
    website_entry.grid(column=1, row=1, columnspan=2)

    user_entry = tk.Entry(width=37)
    user_entry.insert(tk.END, "user_exemple@email.com")
    user_entry.grid(column=1, row=2, columnspan=2)

    password_entry = tk.Entry(width=20)
    password_entry.grid(column=1, row=3)
    ########

    # Button #
    generate_button = tk.Button(text="Generate Password", width=13)
    generate_button.grid(column=2, row=3)

    add_button = tk.Button(text="Add", width=34, command=save_credentials)
    add_button.grid(column=1, row=4, columnspan=2)
    ########

    window.mainloop()
