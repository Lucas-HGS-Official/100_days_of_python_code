import random
import tkinter as tk

import pandas as pd

BG_COLOR = "#B1DDC6"

current_card = {}


def do_nothing():
    return


def next_card():
    global current_card

    _ = right_button.config(command=do_nothing)
    _ = wrong_button.config(command=do_nothing)

    current_card = random.choice(to_learn)
    _ = card_canvas.itemconfig(language_text_label, text="French")
    _ = card_canvas.itemconfig(word_text_label, text=current_card["French"])
    _ = card_canvas.itemconfig(card_background, image=card_front_img)

    _ = window.after(3000, func=flip_card)


def flip_card():
    _ = right_button.config(command=is_known)
    _ = wrong_button.config(command=next_card)
    _ = card_canvas.itemconfig(language_text_label, text="English")
    _ = card_canvas.itemconfig(word_text_label, text=current_card["English"])
    _ = card_canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    # print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")
    next_card()


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Flash Cards")
    _ = window.config(padx=50, pady=50, bg=BG_COLOR)

    try:
        df = pd.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        original_data = pd.read_csv("data/french_words.csv")
        to_learn = original_data.to_dict(orient="records")
    else:
        to_learn = df.to_dict(orient="records")

    # Flashcard #
    card_canvas = tk.Canvas(height=526, width=800, bg=BG_COLOR, highlightthickness=0)
    card_front_img = tk.PhotoImage(file="images/card_front.png")
    card_back_img = tk.PhotoImage(file="images/card_back.png")
    card_background = card_canvas.create_image(400, 263, image=card_front_img)

    language_text_label = card_canvas.create_text(
        400, 150, text="Title", fill="black", font=("Ariel", 40, "italic")
    )
    word_text_label = card_canvas.create_text(
        400, 263, text="word", fill="black", font=("Ariel", 60, "bold")
    )

    card_canvas.grid(row=0, column=0, columnspan=2)
    #############

    # Buttons #
    wrong_button_img = tk.PhotoImage(file="images/wrong.png")
    wrong_button = tk.Button(image=wrong_button_img, highlightthickness=0, command=next_card)
    wrong_button.grid(row=1, column=0)

    right_button_img = tk.PhotoImage(file="images/right.png")
    right_button = tk.Button(image=right_button_img, highlightthickness=0, command=is_known)
    right_button.grid(row=1, column=1)
    #############

    next_card()

    window.mainloop()
