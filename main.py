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
reps = 0
timer = None


# tick_shape = "✔"


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer",fg=GREEN)
    canvas.itemconfig(time_text, text="00:00")
    tick.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        countdown(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)
    if reps == 8:
        countdown(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=RED)
    if reps == 2 or reps == 4 or reps == 6:
        countdown(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK)
    elif reps>8:
        timer_label.config(text = "YOU did it! Great JOB!")
        canvas.itemconfig(time_text, text="00:00")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(number):
    minute = math.floor(number / 60)
    second = number % 60
    if second == 0:
        second = "00"
    if minute == 0:
        canvas.itemconfig(time_text, text=f"{second}")
    else:
        canvas.itemconfig(time_text, text=f"{minute}:{second}")
    if number > 0:
        global timer
        timer = window.after(1000, countdown, number - 1)
    else:
        start_timer()
        marks = ""
        for i in range(math.floor(reps / 2)):
            marks += "✔"
        tick.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=100, bg=YELLOW)
window.title("Tomato app")

canvas = Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 100, image=tomato, )
time_text = canvas.create_text(100, 120, text="00:00", font=(FONT_NAME, 25, "bold"), fill="white")
canvas.grid(row=2, column=2)
# the Timer text
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, "bold"), pady=20)
timer_label.grid(row=1, column=2)

# the buttons
start_button = Button(text="Start", padx=7, pady=7, font=(FONT_NAME, 12, "bold"), bg="#ffffff", command=start_timer)
start_button.grid(row=3, column=1)

reset_button = Button(text="Reset", padx=7, pady=7, font=(FONT_NAME, 12, "bold"), bg="#ffffff", command=reset)
reset_button.grid(row=3, column=3)

# tick
tick = Label(text="", font=(FONT_NAME, 25), fg=GREEN)
tick.grid(row=4, column=2)

window.mainloop()
