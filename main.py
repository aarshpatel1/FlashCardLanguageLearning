from tkinter import *
import random
import pandas

# constants
BACKGROUND_COLOR = "#B1DDC6"

# ----------------------- Creating New Random Flash Card ----------------------- #
data = pandas.read_csv("data/french_words.csv")
dictionary = data.to_dict(orient="records")


def random_card():
    random_word_pair = random.choice(dictionary)
    random_french_word = random_word_pair["French"]
    # random_english_word = random_word_pair["English"]
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=random_french_word)


# ----------------------- UI setup ----------------------- #
# created the output screen using tkinter
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=60, bg=BACKGROUND_COLOR)

# created the canvas
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)

# canvas image
front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(405, 275, image=front_image)

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
right_button = Button(image=right, highlightthickness=0, command=random_card)
right_button.grid(column=1, row=1)

# holding output screen open until program runs
window.mainloop()
