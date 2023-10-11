from tkinter import *
from PIL import Image, ImageTk
import requests
PINK = "#ffffff"

api_key="2077c6d11f21406480a51937231110"
base_url="http://api.weatherapi.com/v1/current.json"
weather_params={
    "key":api_key,
    "q":"Paris",
}

def check_weather():
    city=input_field.get()
    weather_params["q"]=city
    response = requests.get(base_url, params=weather_params)
    data = response.json()


    country = data["location"]['country']
    time = data["location"]['localtime']
    temp = data["current"]["temp_c"]
    condition =data["current"]["condition"]["text"]
    is_cloud = data["current"]["cloud"]
    humidity = data["current"]["humidity"]
    weather_report = f"Country: {country}\nTime: {time}\nTemperature: {temp}°C\nCondition: {condition}\nHumidity: {humidity}"
    output.config(text=weather_report, font=("Arial",14,"normal"),bg=PINK,padx=10,pady=5)


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
input_field.focus()

btn = Button(text="Check Weather", command=check_weather)
btn.grid(column=1,row=3,pady=10)

weather_label = Label(text="The weather is: ",font=("Arial", 15, "bold"))
weather_label.grid(column=1,row=4)

result=Canvas(width=220, height=100,bg=PINK)
result.grid(column=1,row=5,padx=10,pady=10)
output=Label(text="",bg=PINK)
output.grid(column=1,row=5)


window.mainloop()