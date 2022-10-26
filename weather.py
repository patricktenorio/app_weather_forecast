from ctypes import resize
import json
from tkinter import *
import tkinter as tk
from unittest import result
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk
from creds import API_KEY

root = Tk()
root.title("Weather App")
root.geometry("655x600+300+200")
root.config(bg="#c35f56")
root.resizable(False, False)

def getWeather():
    city = textfield.get()

    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude, 1)}°N, {round(location.longitude, 1)}°E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    ## WEATHER
    api="https://api.openweathermap.org/data/2.5/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+f"&units=metric&exclude=hourly&appid={API_KEY}"
    json_data = requests.get(api).json()

    ## CURRENT
    temp = json_data['current']['temp']
    humidity = json_data['current']['humidity']
    pressure = json_data['current']['pressure']
    wind = json_data['current']['wind_speed']
    description = json_data['current']['weather'][0]['description']

    t.config(text=(temp, "°C"))
    h.config(text=(humidity, "%"))
    p.config(text=(pressure, "hPa"))
    w.config(text=(wind, "m/s"))
    d.config(text=description)

    ## FIRST CELL
    firstdayimage = json_data['daily'][0]['weather'][0]['icon']
    photo1 = ImageTk.PhotoImage(file=f"icons/{firstdayimage}@2x.png")
    firstimage.config(image=photo1)
    firstimage.image=photo1

    ## TEMP DAY 1
    tempday1 = json_data['daily'][0]['temp']['day']
    tempnight1 = json_data['daily'][0]['temp']['night']
    day1temp.config(text=f"Day: {tempday1}°C\n Night: {tempnight1}°C")

    ## SECOND CELL
    seconddayimage = json_data['daily'][1]['weather'][0]['icon']
    img=(Image.open(f"icons/{seconddayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image=photo2

    ## TEMP DAY 2
    tempday2 = json_data['daily'][1]['temp']['day']
    tempnight2 = json_data['daily'][1]['temp']['night']
    day2temp.config(text=f"Day: {tempday2}°C\n Night: {tempnight2}°C")

    ## THIRD CELL
    thirddayimage = json_data['daily'][2]['weather'][0]['icon']
    img=(Image.open(f"icons/{thirddayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo3 = ImageTk.PhotoImage(resized_image)
    thirdimage.config(image=photo3)
    thirdimage.image=photo3

    ## TEMP DAY 3
    tempday3 = json_data['daily'][2]['temp']['day']
    tempnight3 = json_data['daily'][2]['temp']['night']
    day3temp.config(text=f"Day: {tempday3}°C\n Night: {tempnight3}°C")

    ## FOURTH CELL
    fourthdayimage = json_data['daily'][3]['weather'][0]['icon']
    img=(Image.open(f"icons/{fourthdayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo4 = ImageTk.PhotoImage(resized_image)
    fourthimage.config(image=photo4)
    fourthimage.image=photo4

    ## TEMP DAY 4
    tempday4 = json_data['daily'][3]['temp']['day']
    tempnight4 = json_data['daily'][3]['temp']['night']
    day4temp.config(text=f"Day: {tempday4}°C\n Night: {tempnight4}°C")

    ## FIFTH CELL
    fifthdayimage = json_data['daily'][4]['weather'][0]['icon']
    img=(Image.open(f"icons/{fifthdayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo5 = ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image=photo5

    ## TEMP DAY 5
    tempday5 = json_data['daily'][4]['temp']['day']
    tempnight5 = json_data['daily'][4]['temp']['night']
    day5temp.config(text=f"Day: {tempday5}°C\n Night: {tempnight5}°C")

    ## SIXTH CELL
    sixthdayimage = json_data['daily'][5]['weather'][0]['icon']
    img=(Image.open(f"icons/{sixthdayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo6 = ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo6)
    sixthimage.image=photo6

    ## TEMP DAY 6
    tempday6 = json_data['daily'][5]['temp']['day']
    tempnight6 = json_data['daily'][5]['temp']['night']
    day6temp.config(text=f"Day: {tempday6}°C\n Night: {tempnight6}°C")

    ## SEVENTH CELL
    seventhdayimage = json_data['daily'][6]['weather'][0]['icon']
    img=(Image.open(f"icons/{seventhdayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo7 = ImageTk.PhotoImage(resized_image)
    seventhimage.config(image=photo7)
    seventhimage.image=photo7

    ## TEMP DAY 3
    tempday7 = json_data['daily'][6]['temp']['day']
    tempnight7 = json_data['daily'][6]['temp']['night']
    day7temp.config(text=f"Day: {tempday7}°C\n Night: {tempnight7}°C")

    ## DAYS
    first = datetime.now()
    day1.config(text=first.strftime("%A"))

    second = first + timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = first + timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fourth = first + timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))

    fifth = first + timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth = first + timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))

    seventh = first + timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))


## ICONS------------------------------------------------------------------------------
image_icon = PhotoImage(file="images/logo.png")
root.iconphoto(False, image_icon)

Round_box = PhotoImage(file="images/details.png")
Label(root, image=Round_box, bg="#c35f56").place(x=333, y=278) #30, 110


## LABEL------------------------------------------------------------------------------
label1 = Label(root, text="Temperature:", font=('Helvetica', 11), fg='black', bg="#fff")
label1.place(x=350, y=290)

label2 = Label(root, text="Humidity:", font=('Helvetica', 11), fg='black', bg="#fff")
label2.place(x=350, y=310)

label3 = Label(root, text="Pressure:", font=('Helvetica', 11), fg='black', bg="#fff")
label3.place(x=350, y=330)

label4 = Label(root, text="Wind Speed:", font=('Helvetica', 11), fg='black', bg="#fff")
label4.place(x=350, y=350)

label5 = Label(root, text="Descrpition:", font=('Helvetica', 11), fg='black', bg="#fff")
label5.place(x=350, y=370)


## SEARCH BOX-------------------------------------------------------------------------
Search_image = PhotoImage(file="images/searchbar.png")
myimage = Label(image=Search_image, bg="#c35f56")
myimage.place(x=110, y=140)

textfield = tk.Entry(root, justify='left', width=15, font=('poppins', 25, 'bold'), bg="#fff", border=0, fg="#a34465")
textfield.place(x=150, y=150)
textfield.focus()

Search_icon = PhotoImage(file="images/magni.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#fff", command=getWeather)
myimage_icon.place(x=485, y=145)


## CLOCK-------------------------------------------------------------------------------
clock = Label(root, font=("Helvetica", 30, 'bold'), fg="white", bg="#c35f56")
clock.place(x=30, y=20)


## TIMEZONE----------------------------------------------------------------------------
timezone = Label(root, font=("Helvetica", 15), fg="white", bg="#c35f56")
timezone.place(x=33, y=62)

long_lat = Label(root, font=("Helvetica", 10), fg="white", bg="#c35f56")
long_lat.place(x=33, y=86)


## THPWD-------------------------------------------------------------------------------
t = Label(root, font=("Helvetica", 11), fg="#c35f56", bg="#fff")
t.place(x=444, y=290)

h = Label(root, font=("Helvetica", 11), fg="#c35f56", bg="#fff")
h.place(x=416, y=310)

p = Label(root, font=("Helvetica", 11), fg="#c35f56", bg="#fff")
p.place(x=420, y=330)

w = Label(root, font=("Helvetica", 11), fg="#c35f56", bg="#fff")
w.place(x=440, y=350)

d = Label(root, font=("Helvetica", 11), fg="#c35f56", bg="#fff")
d.place(x=435, y=370)


## FIRST CELL--------------------------------------------------------------------------
firstframe = Frame(root, width=290, height=132, bg="#282829")
firstframe.place(x=35, y=280)

day1 = Label(firstframe, font="arial 20", bg="#282829", fg="#fff")
day1.place(x=100, y=10)

firstimage = Label(firstframe, bg="#282829")
firstimage.place(x=-5, y=15)

day1temp = Label(firstframe, bg="#282829", fg="#c35f56", font="arial 15 bold")
day1temp.place(x=100, y=65)


## SECOND CELL-------------------------------------------------------------------------
secondframe = Frame(root, width=90, height=115, bg="#282829")
secondframe.place(x=35, y=425)

day2 = Label(secondframe, bg="#282829", fg="#fff")
day2.place(x=23, y=5)

secondimage = Label(secondframe, bg="#282829")
secondimage.place(x=20, y=25)

day2temp = Label(secondframe, bg="#282829", fg="#fff")
day2temp.place(x=2, y=75)


## THIRD CELL--------------------------------------------------------------------------
thirdframe = Frame(root, width=90, height=115, bg="#282829")
thirdframe.place(x=135, y=425)

day3 = Label(thirdframe, bg="#282829", fg="#fff")
day3.place(x=23, y=5)

thirdimage = Label(thirdframe, bg="#282829")
thirdimage.place(x=20, y=25)

day3temp = Label(thirdframe, bg="#282829", fg="#fff")
day3temp.place(x=2, y=75)


## FOURTH CELL-------------------------------------------------------------------------
fourthframe = Frame(root, width=90, height=115, bg="#282829")
fourthframe.place(x=235, y=425)

day4 = Label(fourthframe, bg="#282829", fg="#fff")
day4.place(x=23, y=5)

fourthimage = Label(fourthframe, bg="#282829")
fourthimage.place(x=20, y=25)

day4temp = Label(fourthframe, bg="#282829", fg="#fff")
day4temp.place(x=2, y=75)


## FIFTH CELL--------------------------------------------------------------------------
fifthframe = Frame(root, width=90, height=115, bg="#282829")
fifthframe.place(x=335, y=425)

day5 = Label(fifthframe, bg="#282829", fg="#fff")
day5.place(x=23, y=5)

fifthimage = Label(fifthframe, bg="#282829")
fifthimage.place(x=20, y=25)

day5temp = Label(fifthframe, bg="#282829", fg="#fff")
day5temp.place(x=2, y=75)


## SIXTH CELL--------------------------------------------------------------------------
sixthframe = Frame(root, width=90, height=115, bg="#282829")
sixthframe.place(x=435, y=425)

day6 = Label(sixthframe, bg="#282829", fg="#fff")
day6.place(x=23, y=5)

sixthimage = Label(sixthframe, bg="#282829")
sixthimage.place(x=20, y=25)

day6temp = Label(sixthframe, bg="#282829", fg="#fff")
day6temp.place(x=2, y=75)


## SEVENTH CELL------------------------------------------------------------------------
seventhframe = Frame(root, width=90, height=115, bg="#282829")
seventhframe.place(x=535, y=425)

day7 = Label(seventhframe, bg="#282829", fg="#fff")
day7.place(x=23, y=5)

seventhimage = Label(seventhframe, bg="#282829")
seventhimage.place(x=20, y=25)

day7temp = Label(seventhframe, bg="#282829", fg="#fff")
day7temp.place(x=2, y=75)


root.mainloop()
