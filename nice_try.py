language = "French"
word = "word"

window = Tk()
window.title("Naru's french words")
window.config(padx=0, pady=0, bg=BACKGROUND_COLOR)

background_img = PhotoImage(file="./images/card_back.png")


canvas = Canvas(width=860, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)
img = PhotoImage(file="./images/card_front.png")
canvas.create_image(430, 275, image=img)
canvas.grid(row=0, column=0, columnspan=2)

img_right = PhotoImage(file="./images/right.png")
right_label = Label(window, image=img_right, highlightthickness=0)
right_label.grid(row=1,column=1)

img_wrong = PhotoImage(file="./images/wrong.png")
wrong_label = Label(window, image=img_wrong, highlightthickness=0)
wrong_label.grid(row=1,column=0)

language_label = Label(text=language, font=("Arial", 40, "italic"), bg='white')
language_label.place(x=430, y=80, anchor='center')

word_label = Label(text=word, font=("Arial", 60, "bold"), bg='white')
word_label.place(x=430, y=200, anchor='center')











window.mainloop()
