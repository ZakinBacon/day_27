from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def button_clicked():
    my_label["text"] = input.get()
    print("I got clicked")


# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

my_label["text"] = "new text"  # changes the text of the label

# button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="2nd Button", command=button_clicked)
button2.grid(column=2, row=0)
# entry
input = Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()
