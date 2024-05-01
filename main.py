from tkinter import *
import random
import pandas
import os.path

# constants
BACKGROUND_COLOR = "#B1DDC6"
WORDS_TO_LEARN = "data/words_to_learn.csv"

# global variables
random_word_pair = {}


# ----------------------- Storing unknown words into new file and managing it ----------------------- #
def known_word():
    random_card()
    dictionary.remove(random_word_pair)
    left_words = pandas.DataFrame(dictionary)
    left_words.to_csv(WORDS_TO_LEARN, index=False)


# ----------------------- Card Flipping Mechanism ----------------------- #
def flash_card():
    # showing english translation of the French word previously displayed
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=random_word_pair["English"], fill="white")


# ----------------------- Creating New Random Flash Card ----------------------- #
if os.path.exists(WORDS_TO_LEARN):
    # print("The file exists.")
    data = pandas.read_csv(WORDS_TO_LEARN)
else:
    # print("The file does not exist.")
    data = pandas.read_csv("data/french_words.csv")

dictionary = data.to_dict(orient="records")


def random_card():
    global random_word_pair, flash_card_timer

    # cancels the current running loop
    window.after_cancel(flash_card_timer)

    # choosing randomly word pair from the dictionary created using pandas from french_words.csv
    random_word_pair = random.choice(dictionary)

    # changing canvas background color, text color and French word
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=random_word_pair["French"], fill="black")

    # starts a new loop for 3 seconds
    flash_card_timer = window.after(3000, flash_card)


# ----------------------- UI setup ----------------------- #
# created the output screen using tkinter
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=60, bg=BACKGROUND_COLOR)

# timer for the remembering the French word
flash_card_timer = window.after(3000, flash_card)

# created the canvas
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)

# canvas images
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(405, 275, image=front_image)

# canvas text
title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

# canvas location
canvas.grid(column=0, row=0, columnspan=2)

# wrong button
wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=random_card)
wrong_button.grid(column=0, row=1)

# right button
right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, command=known_word)
right_button.grid(column=1, row=1)

random_card()

# holding output screen open until program runs
window.mainloop()
