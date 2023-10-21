import tkinter as tk
from PIL import Image,ImageTk
import requests
import json

def get_weather():
    city = city_entry.get()
    url = f"https://api.weatherapi.com/v1/current.json?key=813e7077a15640be80d51040232110&q={city}"
    r = requests.get(url)
    wdic = json.loads(r.text)
    temp_c = wdic['current']['temp_c']
    temp_f = wdic['current']['temp_f']
    temp_lable.config(text=f"The Temperature in celsius in {city} is {temp_c}\nThe Temperature in Farenheit in {city} is {temp_f}")
    img_icon = wdic['current']['condition']['icon']

    icon_response = requests.get(f"https:{img_icon}",stream=True)
    if icon_response.status_code == 200:
        icon = Image.open(icon_response.raw)
        icon = icon.resize((350,350),Image.LANCZOS)
        icon_photo = ImageTk.PhotoImage(icon)
        icon_lable.config(image=icon_photo)
        icon_lable.image = icon_photo


window = tk.Tk()
window.title("Weather")

city_lable = tk.Label(window,text="Enter the City")
city_lable.pack()

city_entry = tk.Entry(window)
city_entry.pack()

but = tk.Button(window,text="Search",command=get_weather)
but.pack()

temp_lable = tk.Label(window,text="")
temp_lable.pack()

icon_lable = tk.Label(window,image="")
icon_lable.pack()

window.mainloop()