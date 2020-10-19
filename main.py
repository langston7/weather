
import tkinter as tk
import requests


def get_zip_and_update():
    zipcode = zip_entry.get()
    url = f' http://api.openweathermap.org/data/2.5/weather?zip={zipcode},us&appid=c59ae20c829ab2f70420df085740501e'
    response = requests.get(url)
    response_json = response.json()
    output_coordinates.text = response_json['coord']


window = tk.Tk()
window.columnconfigure([0, 1], minsize=250)
window.rowconfigure(0, minsize=260)
input_frame = tk.Frame(master=window)
output_frame = tk.Frame(master=window)
input_frame.grid(row=0, column=0)
output_frame.grid(row=0, column=1)

input_prompt = tk.Label(master=input_frame, text='Enter the zip code for the area:')
input_prompt.grid(row=0, column=0)

zip_entry = tk.Entry(master=input_frame)
zip_entry.grid(row=1, column=0)

button_zip = tk.Button(
    master=input_frame,
    text="Get Weather",
    width=12,
    height=2,
    command=get_zip_and_update()
)
button_zip.grid(row=2, column=0)

label_coordinates = tk.Label(master=output_frame, text="coordinates:")
label_coordinates.grid(row=0, column=0)
label_weather = tk.Label(master=output_frame, text="coordinates:")
label_weather.grid(row=1, column=0)
label_base = tk.Label(master=output_frame, text="coordinates:")
label_base.grid(row=2, column=0)
label_temp = tk.Label(master=output_frame, text="coordinates:")
label_temp.grid(row=3, column=0)
label_feelslike = tk.Label(master=output_frame, text="coordinates:")
label_feelslike.grid(row=4, column=0)
label_temp_min = tk.Label(master=output_frame, text="coordinates:")
label_temp_min.grid(row=5, column=0)
label_temp_max = tk.Label(master=output_frame, text="coordinates:")
label_temp_max.grid(row=6, column=0)
label_pressure = tk.Label(master=output_frame, text="coordinates:")
label_pressure.grid(row=7, column=0)
label_wind = tk.Label(master=output_frame, text="coordinates:")
label_wind.grid(row=8, column=0)

output_coordinates = tk.Label(master=output_frame, text="")
output_coordinates.grid(row=0, column=1)
output_weather = tk.Label(master=output_frame, text="")
output_weather.grid(row=1, column=1)
output_icon = tk.Label(master=output_frame, text="")
output_icon.grid(row=1, column=1)
output_base = tk.Label(master=output_frame, text="")
output_base.grid(row=2, column=1)
output_temp = tk.Label(master=output_frame, text="")
output_temp.grid(row=3, column=1)
output_feelslike = tk.Label(master=output_frame, text="")
output_feelslike.grid(row=4, column=1)
output_temp_min = tk.Label(master=output_frame, text="")
output_temp_min.grid(row=5, column=1)
output_temp_max = tk.Label(master=output_frame, text="")
output_temp_max.grid(row=6, column=1)
output_pressure = tk.Label(master=output_frame, text="")
output_pressure.grid(row=7, column=1)
output_wind = tk.Label(master=output_frame, text="")
output_wind.grid(row=8, column=1)


window.mainloop()

