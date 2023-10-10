from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Weather App")
window.config(padx=20, pady=20)

canvas=Canvas(width=300, height=200)
img = Image.open("img.png")
r_img = img.resize((200,200))
logo = ImageTk.PhotoImage(r_img)
canvas.create_image(150,100,image=logo)
canvas.grid(column=0,row=0,columnspan=3)

city = Label(text="Enter City Name",font=("Arial",16,"bold"))
city.configure(pady=10)
city.grid(column=1, row=1)
input_field = Entry(width=35)
input_field.grid(column=1, row=2,ipady=5)

btn = Button(text="Check Weather")
btn.grid(column=1,row=3,pady=10)

weather_label = Label(text="The weather is: ",font=("Arial", 15, "bold"))
weather_label.grid(column=1,row=4)


weather_result = Entry(window,width=35)
weather_result.place(width=200,height=100)
weather_result.grid(column=1,row=5,pady=10,ipady=10)


window.mainloop()