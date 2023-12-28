from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.2#25
SHORT_BREAK_MIN = 0.1#5
LONG_BREAK_MIN = 0.3#20

# ---------------------------- TIMER RESET ------------------------------- #




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")

timer = Label(text="TIMER", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=PINK)
timer.grid(column=2, row=1)

window.minsize(400,400)
window.config(padx=100, pady=50, bg=PINK)
my_canvas = Canvas(width=200, height=223, bg=PINK, highlightthickness=0)

tomato = PhotoImage(file="tomato.png")
my_canvas.create_image(100, 112, image=tomato)


on_tomato_text = my_canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
my_canvas.grid(column=2, row=2)
# ---------------------------- TIMER MECHANISM ------------------------------- #
def on_click_start():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
    # # reps = 1
    #
    # while reps < 9:
    #     if reps % 8 == 0:
    #         count_down(long_break_sec)
    #
    #     elif reps % 2 == 0:
    #         column_count = 2
    #         count_down(short_break_sec)
    #         check = Label(text="✔", font=("bold"), fg=GREEN, bg=PINK)
    #         check.grid(column=column_count, row=4)
    #         column_count += 1
    #         # reps += 1
    #
    #     else:
    #         count_down(work_sec)
    #
    #     reps += 1
    #


    # # if its 8 rep:
    # if reps % 8 == 0:
    #     count_down(long_break_sec)
    #
    # # if its 2,4,6 rep:
    # elif reps % 2 == 0:
    #     column_count = 2
    #     count_down(short_break_sec)
    #     check = Label(text="✔", font=("bold"), fg=GREEN, bg=PINK)
    #     check.grid(column=column_count, row=4)
    #     column_count += 1
    #     reps += 1
    #
    #
    # # if its 1,3,5,7 rep:
    # else:
    #     count_down(work_sec)
    #     reps += 1
    #



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# concept-- after( ml(milli seconds), function, argument to pass in function)
def count_down(count):
    if count > 0:
        minutes = math.floor(count/60)
        seconds = count % 60
        if seconds < 10:
            seconds = f"0{seconds}"

        my_canvas.itemconfig(on_tomato_text, text=f"{minutes}:{seconds}")
        window.after(1000, count_down, count - 1)

    else:
        on_click_start()

def on_click_reset():
    on_click_start = False

start = Button(text="Start", command=on_click_start)
start.grid(column=1, row=3)

reset = Button(text="Reset", command=on_click_reset)
reset.grid(column=3, row=3)

# check = Label(text="✔", font=("bold"), fg=GREEN, bg=PINK)
# check.grid(column=2, row=4)





window.mainloop()