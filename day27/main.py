from tkinter import *

window = Tk()

window.title("Mile to KM Converter")
window.config(padx=20, pady=20)
# Resolution
window.minsize(width=200, height=100)

miles_my_label = Label(text="Miles", font=("Arial", 10, "bold"))
miles_my_label.grid(column=2, row=0)

is_qual_my_label = Label(text="is equal to", font=("Arial", 10, "bold"))
is_qual_my_label.grid(column=0, row=1)

kilometer_label = Label(text="Km", font=("Arial", 10, "bold"))
kilometer_label.grid(column=2, row=1)

kilometer_result_label = Label(text="0", font=("Arial", 10, "bold"))
kilometer_result_label.grid(column=1, row=1)

# Button
# Grid = Row:Horizontal and Column:Vertical
def miles_calculate():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")
    
# Enter the Miles
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)


button = Button(text="Calculate", command=miles_calculate)
button.grid(column=1, row=2)

















window.mainloop()
