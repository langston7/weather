import tkinter as tk
from tkinter import messagebox
import requests
from urllib.request import urlopen
from PIL import ImageTk


def get_zip(): # fetch the zip from user and retrieve info

    #verify that zip is 5 digits
    zipcode = zip_entry.get()
    if len(zipcode) != 5:
        messagebox.showerror("gay if read", "Zipcode should be 5 digits")
        return

    url = f' http://api.openweathermap.org/data/2.5/weather?zip={zipcode},us&appid=c59ae20c829ab2f70420df085740501e'
    response = requests.get(url)
    
    #verify that zip is valid based on url
    if response.status_code != 200:
        messagebox.showerror("gay if read", "error with zip")
        return

    response_json = response.json()
    
    update_grid(response_json)


def update_grid(response_json): # updates grid with info from json file

    # prep icon retrieval and update display
    icon_code = response_json['weather'][0]['icon']
    icon_url = f'http://openweathermap.org/img/wn/{icon_code}@2x.png'
    icon_byt = urlopen(icon_url).read()
    icon_image = ImageTk.PhotoImage(data=icon_byt)
    output_icon.configure(image=icon_image)
    output_icon.image = icon_image

    # update text displays with info
    coord_text.set(str(response_json['coord']['lon']) + ', ' + str(response_json['coord']['lon']))
    weather_text.set(response_json['weather'][0]['main'])
    base_text.set(response_json['base'])
    temp_text.set(response_json['main']['temp'])
    feelslike_text.set(response_json['main']['feels_like'])
    min_text.set(response_json['main']['temp_min'])
    max_text.set(response_json['main']['temp_max'])
    pressure_text.set(response_json['main']['pressure'])
    wind_text.set(str(response_json['wind']['speed']) + 'mph')


window = tk.Tk()
window.columnconfigure([0, 1], minsize=250)
window.rowconfigure(0, minsize=260)
input_frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=3)
output_frame = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=5)
input_frame.grid(row=0, column=0, padx=5, pady=5)
output_frame.grid(row=0, column=1)

input_prompt = tk.Label(master=input_frame, text='Enter the zip code for the area:')
input_prompt.grid(row=0, column=0, padx=5, pady=5)

zip_entry = tk.Entry(master=input_frame)
zip_entry.grid(row=1, column=0, padx=5, pady=5)

button_zip = tk.Button(
    master=input_frame,
    text="Get Weather",
    width=12,
    height=2,
    command=get_zip
)
button_zip.grid(row=2, column=0, padx=5, pady=5)

label_coordinates = tk.Label(master=output_frame, text="coordinates:")
label_coordinates.grid(row=0, column=0)
label_weather = tk.Label(master=output_frame, text="weather:")
label_weather.grid(row=1, column=0)
label_base = tk.Label(master=output_frame, text="base:")
label_base.grid(row=2, column=0)
label_temp = tk.Label(master=output_frame, text="temp:")
label_temp.grid(row=3, column=0)
label_feelslike = tk.Label(master=output_frame, text="feels like:")
label_feelslike.grid(row=4, column=0)
label_temp_min = tk.Label(master=output_frame, text="low:")
label_temp_min.grid(row=5, column=0)
label_temp_max = tk.Label(master=output_frame, text="high:")
label_temp_max.grid(row=6, column=0)
label_pressure = tk.Label(master=output_frame, text="pressure:")
label_pressure.grid(row=7, column=0)
label_wind = tk.Label(master=output_frame, text="wind:")
label_wind.grid(row=8, column=0)

coord_text = tk.StringVar()
weather_text = tk.StringVar()
base_text = tk.StringVar()
temp_text = tk.StringVar()
feelslike_text = tk.StringVar()
min_text = tk.StringVar()
max_text = tk.StringVar()
pressure_text = tk.StringVar()
wind_text = tk.StringVar()

output_coordinates = tk.Label(master=output_frame, textvariable=coord_text)
output_coordinates.grid(row=0, column=1)
output_weather = tk.Label(master=output_frame, textvariable=weather_text)
output_weather.grid(row=1, column=1)
output_icon = tk.Label(master=output_frame)
output_icon.grid(row=1, column=2)
output_base = tk.Label(master=output_frame, textvariable=base_text)
output_base.grid(row=2, column=1)
output_temp = tk.Label(master=output_frame, textvariable=temp_text)
output_temp.grid(row=3, column=1)
output_feelslike = tk.Label(master=output_frame, textvariable=feelslike_text)
output_feelslike.grid(row=4, column=1)
output_temp_min = tk.Label(master=output_frame, textvariable=min_text)
output_temp_min.grid(row=5, column=1)
output_temp_max = tk.Label(master=output_frame, textvariable=max_text)
output_temp_max.grid(row=6, column=1)
output_pressure = tk.Label(master=output_frame, textvariable=pressure_text)
output_pressure.grid(row=7, column=1)
output_wind = tk.Label(master=output_frame, textvariable=wind_text)
output_wind.grid(row=8, column=1)


window.mainloop()


