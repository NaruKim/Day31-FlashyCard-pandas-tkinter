import pandas

# French
data = pandas.read_csv("data/french_words.csv")
data2 = pandas.read_csv("data/learned_words.csv")

to_learn_words = data.to_dict(orient="records")
learned_words = data2.to_dict(orient="records")

for i in learned_words:
    if i in to_learn_words:
        print(i)
        to_learn_words.remove(i)

print(to_learn_words)


#-----------
# canvas.after(3000,eng_card)
#
#
# def eng_card():
#     canvas.itemconfig(card_background, image=card_back_img)
#     canvas.itemconfig(card_title, text="English")
#     canvas.itemconfig(card_word, text=current_card["English"])

list = [{"a", "b"},{"c","d"},{"e","f"}]
# e = {"c","d"}
# list.remove(e)
e = {"j", "k"}
list.append(e)
print(list)


