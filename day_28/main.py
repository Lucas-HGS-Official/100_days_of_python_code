import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
TEXT_COLOR = "#DAFFB9"
BG_COLOR = "#123701"
BUTTON_COLOR = "#006ACE"
HIGHLIGHT_COLOR = "#FF1D59"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
_ = window.config(padx=80, pady=40, bg=BG_COLOR)

# Canvas #
canvas = tk.Canvas(width=200, height=224, bg=BG_COLOR, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
_ = canvas.create_image(100, 112, image=tomato_img)

_ = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=1, row=1)
##########

# Title #
timer_title_label = tk.Label(text="Timer", font=(FONT_NAME, 46, "bold"), bg=BG_COLOR, fg=TEXT_COLOR)
timer_title_label.grid(column=1, row=0)
##########

# Buttons #
start_button = tk.Button(
    text="Start",
    font=(FONT_NAME, 11, "bold"),
    width=4,
    height=1,
    anchor="s",
    bg=BUTTON_COLOR,
    fg=TEXT_COLOR,
    highlightthickness=0,
    # command=
)
start_button.grid(column=0, row=2)

reset_button = tk.Button(
    text="Reset",
    font=(FONT_NAME, 11, "bold"),
    width=4,
    height=1,
    anchor="s",
    bg=BUTTON_COLOR,
    fg=TEXT_COLOR,
    highlightthickness=0,
    # command=
)
reset_button.grid(column=2, row=2)
##########

# check #
checkmark_label = tk.Label(text="✔", font=(FONT_NAME, 16), bg=BG_COLOR, fg=HIGHLIGHT_COLOR)
checkmark_label.grid(column=1, row=3)
##########
window.mainloop()

# if __name__ == "__main__":
#     print("Hello World!!")
