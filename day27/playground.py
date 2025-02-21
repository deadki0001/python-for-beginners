from tkinter import *

window = Tk()

window.title("My First GUI Program")
# Resolution
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)
# Component label
my_label = Label(text="I am a Button", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=100, pady=200)

# Button
# Grid = Row:Horizontal and Column:Vertical
def button_clicked():
    print(f"I Got clicked")
    new_text = input.get()
    my_label.config(text=new_text)
    my_label.grid()

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry

input = Entry(width=10)
input.grid(column=3, row=2)
print(input.get())
