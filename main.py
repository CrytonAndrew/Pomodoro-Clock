from tkinter import *
import time as t
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec= SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps <= 1 or reps == 3 or reps == 5 or reps == 7:
        label.config(text="Work")
        if reps == 3 or reps == 7:
            label2.config(text="✓", fg=GREEN)
        count_down(work_sec)
        reps += 1
    elif reps == 2 or reps == 4 or reps == 6:
        label.config(text="Break", fg=RED)
        count_down(short_break_sec)
        reps += 1
    elif reps == 8:
        count_down(long_break_sec)
        reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:  # Dynamic Typing
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    print(count)
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()
    print(f"Reps: {reps}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Technique")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, highlightthickness=0)
image = PhotoImage(file="tomato.png")  # Read the image file
canvas.create_image(100, 100, image=image)  # Pass in x and y position for the image
timer_text = canvas.create_text(100, 110, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.config(bg=YELLOW)
canvas.grid(row=1, column=1)


label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
label.grid(row=0, column=1)

button = Button(text="Start", bg=YELLOW, command=start_timer, highlightthickness=0)
button.grid(row=2, column=0)

button2 = Button(text="Reset", bg=YELLOW, highlightthickness=0)
button2.grid(row=2, column=2)

label2 = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
label2.grid(row=3, column=1)


window.mainloop()
