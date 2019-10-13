import tkinter
import random

window = tkinter.Tk()
window.title("моё окно")
window.geometry("600x500")
label = tkinter.Label(text="0", fg="black", bg="red", font="Arial 22")
label.place(x=25, y=25)

def random_color():
    color = ["red", "green", "blue"]
    label["bg"] = random.choice(color)

def count():
    random_color()
    num = int (label["text"])
    num = num + 1
    label["text"] = str(num)



button = tkinter.Button(text="кнопка", command = count)
button.place(x=25, y=100)
label["text"] = "другая надпись"
label["bg"] = "#0ac9c0"


window.mainloop()
