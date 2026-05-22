import math
import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
BREAK_COLOR = "#e2979c"
TEXT_COLOR = "#DAFFB9"
BG_COLOR = "#123701"
BUTTON_COLOR = "#006ACE"
HIGHLIGHT_COLOR = "#FF1D59"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer_sec = ""


def do_nothing():
    return


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer_sec)

    _ = timer_title_label.config(text="Timer", fg=TEXT_COLOR)

    timer_text = "00:00"
    _ = canvas.itemconfig(timer_text_label, text=timer_text)

    global reps
    reps = 0
    _ = checkmark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    _ = start_button.config(command=do_nothing)

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        count_down(work_sec)
        _ = timer_title_label.config(text="Work", fg=TEXT_COLOR)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        _ = timer_title_label.config(text="Break", fg=HIGHLIGHT_COLOR)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        _ = timer_title_label.config(text="Break", fg=BREAK_COLOR)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count: int):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    timer_text = f"{count_min}:{count_sec}"
    _ = canvas.itemconfig(timer_text_label, text=timer_text)

    if count > 0:
        global timer_sec
        timer_sec = window.after(1000, count_down, count - 1)
    else:
        start_timer()

        mark = ""
        global reps
        mark = "✔" * math.floor(reps / 2)
        _ = checkmark_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
_ = window.config(padx=80, pady=40, bg=BG_COLOR)


# Canvas #
canvas = tk.Canvas(width=200, height=224, bg=BG_COLOR, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
_ = canvas.create_image(100, 112, image=tomato_img)

timer_text_label = canvas.create_text(
    100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)

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
    command=start_timer,
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
    command=reset_timer,
)
reset_button.grid(column=2, row=2)
##########

# check #
checkmark_label = tk.Label(text="", font=(FONT_NAME, 16), bg=BG_COLOR, fg=HIGHLIGHT_COLOR)
checkmark_label.grid(column=1, row=3)
##########
window.mainloop()

# if __name__ == "__main__":
#     print("Hello World!!")
