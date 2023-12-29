from tkinter import *

windows = Tk()
windows.minsize(width=500, height=300)
windows.config(padx=30,pady=30)

def miles_to_km():
    miles = float(input_entry.get())
    km = round(miles * 1.689)
    kilometer_lable.config(text=f"{km}")

input_entry = Entry(width=7)
input_entry.grid(column=1, row=0)

mile_lable = Label(text="Miles")
mile_lable.grid(column=2, row=0)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

kilometer_lable = Label(text="0")
kilometer_lable.grid(column=1, row=1)

km_lable = Label(text="Km")
km_lable.grid(column=2, row=1)

button = Button(text="Calcultor", command=miles_to_km)
button.grid(column=1, row=2)


windows.mainloop()
