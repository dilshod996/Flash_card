from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
random_word = {}
my_word = {}
try:
    words = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    exist_file= pandas.read_csv("./data/french_words.csv")
    my_word = exist_file.to_dict(orient="records")
else:
    my_word = words.to_dict(orient="records")




def press_button():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(my_word)
    my_canvas.itemconfig(french_title, text="French", fill="black")
    my_canvas.itemconfig(word_tile, text=random_word["French"], fill="black")
    my_canvas.itemconfig(canvas_image, image=my_image)
    flip_timer=window.after(3000, func=change_card)




    # list_of_words = words.to_list()



def change_card():

    my_canvas.itemconfig(canvas_image, image=back_image)
    my_canvas.itemconfig(french_title, text="English", fill= "white")
    my_canvas.itemconfig(word_tile, text=random_word["English"], fill="white")



def is_known():
    my_word.remove(random_word)
    print(len(my_word))
    my_data = pandas.DataFrame(my_word)
    my_data.to_csv("data/words_to_learn.csv", index=FALSE)

    press_button()



window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=change_card)
my_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")

my_canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image=my_canvas.create_image(400, 263, image=my_image)
my_canvas.grid(row=0, column=0, sticky="EW", columnspan=2)
# my_canvas.create_image(400, 263, image=back_image)

french_title = my_canvas.create_text(400,150, text="Title", font=("Ariel", 40, "italic"))
word_tile = my_canvas.create_text(400,263, text="Word", font=("Arial", 60, "bold"))


cancel_image = PhotoImage(file="./images/wrong.png")
cancel_button = Button(image=cancel_image, highlightthickness=0, bg=BACKGROUND_COLOR, activebackground= BACKGROUND_COLOR, bd=0, command=press_button)
cancel_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, activebackground= BACKGROUND_COLOR, bd=0, command=is_known)
right_button.grid(row=1, column=1)


press_button()













window.mainloop()