from tkinter import *
import pandas
import json
import random

data = pandas.read_csv("./data/french_words.csv")
data_dic ={row.French:row.English for (index, row) in data.iterrows()}
BACKGROUND_COLOR = "#B1DDC6"
data_list = list(data_dic)
time = 0



def save_mis():
    missing = {data_list[time-1]:data_dic[data_list[time-1]]}
    try:
        with open("Missing word.json", 'r') as file:
            data = json.load(file)
    except:
        with open("Missing word.json", 'w') as file:
            json.dump(missing, file, indent=4)
    else:
        data.update(missing)
        with open("Missing word.json", 'w') as file:
            json.dump(data, file, indent=4)

def words(count=3):
    global label, word, time, back_img

    if count == 0:

        label.config(text="English", bg="aquamarine4", fg="white")
        word.config(text=data_dic[data_list[time]], bg="aquamarine4", fg="white")
        canvas.itemconfig(image, image=back_img)

        time = random.randint(0, 103)
    else:
        canvas.itemconfig(image, image=front_img)
        label.config(text="French", bg="white", fg="black")
        word.config(text=data_list[time], bg="white", fg="black")
        window.after(1000, words, count-1)


# setup ui

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#button
true_button_img = PhotoImage(file="./images/right.png")
true_button = Button(image=true_button_img, command=words, highlightthickness=0)
true_button.grid(column=2, row=1)
false_button_img = PhotoImage(file="./images/wrong.png")
false_button = Button(image=false_button_img, highlightthickness=0, command=save_mis)
false_button.grid(column=0, row=1)

#background
back_img = PhotoImage(file="./images/card_back.png")
front_img = PhotoImage(file="./images/card_front.png")
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
image = canvas.create_image(400, 263, image= front_img)
canvas.grid(column=1, row=0)

#lable

label = Label(text="French", font=("Arila", 38, "italic"), bg="white", fg="black")
label.place(x=420,y=80)
word =  Label(text="Word", font=("Arila", 60, "bold"), bg="white", fg="black")
word.grid(column=1, row=0)













window.mainloop()
