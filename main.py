from tkinter import *

window = Tk()
window.title("Weather App")
window.config(padx=20, pady=20)

canvas=Canvas(width=200,height=300)
canvas.grid(column=0,row=0)
city = canvas.create_text(110,20,text="Enter City Name",font=("Arial", 16, "bold"))
input_field = Entry()
input_field.grid(column=0, row=0)


window.mainloop()