import time
from tkinter import *
import tkinter as tk
import cv2
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import winshell
import requests
import pywhatkit as pwt
import psutil
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 185
engine.setProperty('rate', newVoiceRate)

window = tk.Tk()

global var
global var1

var = StringVar()
var1 = StringVar()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        var.set("Hello ! Good Morning Sir")
        window.update()
        speak("Hello ! Good Morning Sir!")
    elif 12 <= hour <= 18:
        var.set("Hello ! Good Afternoon Sir!")
        window.update()
        speak("Hello ! Good Afternoon Sir!")
    else:
        var.set("Hello ! Good Evening Sir")
        window.update()
        speak("Hello ! Good Evening Sir!")
    speak("Myself Vlingo! How may I help you sir")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
    except Exception:
        speak("Pardon me, please say that again")
        return "None"
    var1.set(query)
    window.update()
    return query


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)
    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)


def play():
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg='green')
    wishme()
    while True:
        btn1.configure(bg='dark blue')
        query = takeCommand().lower()
        if 'exit' in query:
            var.set("Bye sir")
            speak("Bye sir")
            btn1.configure(bg='#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            break

        elif 'hello' in query:
            var.set('Hello Sir')
            window.update()
            speak("Hello Sir")

        elif 'thank you' in query:
            var.set("Welcome Sir")
            window.update()
            speak("Welcome Sir")

        elif ('old are you' in query) or ('version' in query):
            var.set("Version 0.1.1 ")
            window.update()
            speak("I am a newbie sir ! Version 0.1.1")

        elif ('your name' in query) or ('who are you' in query):
            var.set("Myself Ruby,I am your personal assistant")
            window.update()
            speak("Myself Ruby,Myself Ruby,I am your personal assistant")

        elif 'who made you' in query:
            var.set("My Creators are Jayanth Rahul And Vishnu")
            window.update()
            speak("My Creators are Jayanth Rahul And Vishnu")

        elif 'sleep' in query:
            var.set('Sleeping...............')
            window.update()
            speak("OK sir!! time to sleep have a good day")
            quit()

            # System date and time
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%I %M %S %p")
            var.set("Sir the time is %s" % strtime)
            window.update()
            speak("Sir the time is %s" % strtime)

        elif 'date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Sir today's date is %s" % strdate)
            window.update()
            speak("Sir today's date is %s" % strdate)

        elif "remember that" in query:
            speak("what should I remember")
            data = takeCommand()
            speak("you said to remember" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you know anything" in query:
            remember = open("data.txt", "r")
            speak("you said me to remember that" + remember.read())

        elif 'open youtube' in query:
            var.set('opening Youtube')
            window.update()
            speak('opening Youtube')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            var.set('opening google')
            window.update()
            speak('opening google')
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            var.set('opening stackoverflow')
            window.update()
            speak('opening stackoverflow')
            webbrowser.open('stackoverflow.com')

        elif 'open github' in query:
            var.set('opening github')
            window.update()
            speak('opening github')
            webbrowser.open('https://github.com')

        elif "game" in query:
            var.set("Here's a game for you")
            window.update()
            speak("Here's a game for you")
            webbrowser.open('https://chromedino.com')

        elif "music" in query:
            var.set("Opening a music app for you")
            window.update()
            speak("Here's are some soothing songs for you,enjoy sir")
            webbrowser.open('https://wynk.in/music/playlist/wynk-top-100/bb_1577097670143')

        elif 'news' in query:
            var.set('Opening news')
            window.update()
            webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif 'wikipedia' in query:
            if 'open wikipedia' in query:
                webbrowser.open('wikipedia.com')
            else:

                try:
                    speak("searching wikipedia")
                    query = query.replace("according to wikipedia", "")
                    results = wikipedia.summary(query, sentences=1)
                    speak("According to wikipedia")
                    var.set(results)
                    window.update()
                    speak(results)
                except Exception:
                    var.set('sorry sir could not find any results')
                    window.update()
                    speak('sorry sir could not find any results')

            # empty recycle bin

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")

        elif 'weather' in query:
            api_key = ""
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

        elif 'on youtube' in query:
            song = query.replace('play', '')
            var.set('Playing on Youtube')
            speak('playing' + song)
            pwt.playonyt(song)

        elif 'click photo' in query:
            stream = cv2.VideoCapture(0)
            grabbed, frame = stream.read()
            if grabbed:
                cv2.imshow('pic', frame)
                cv2.imwrite('pic.jpg', frame)
                stream.release()
        elif "cpu" in query:
            cpu()

        elif "logout" in query:
            os.system("shutdown - l")

        elif "shutdown" in query:
            os.system("shutdown /s /t l")

        elif "restart" in query:
            os.system("shutdown /r /t l")


def update(ind):
    frame = frames[ind % 10]
    ind += 1
    label.configure(image=frame)
    window.after(10, update, ind)


label2 = Label(window, textvariable=var1, bg='#730cfa')
label2.config(font=("Fixedsys", 30))
var1.set('YOU SAID:')
label2.pack(pady=10)

label1 = Label(window, textvariable=var, bg='#ADD8E6')
label1.config(font=("Fixedsys", 20))
var.set('Welcome')
label1.pack()

# noinspection PyRedundantParentheses
frames = [PhotoImage(file='assist.gif', format='gif -index %i' % (i)) for i in range(10)]
window.title('Ruby by JRV')

label = Label(window, width=500, height=350)
label.pack(pady=35)
window.after(0, update, 0)


def mode1():
    window.configure(bg='black')


def mode2():
    window.configure(bg='#f0f0f0')


btn0 = Button(text='SAY HI', width=20, command=wishme, bg='#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text='START', width=20, command=play, bg='DARK BLUE')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text='QUIT', width=20, command=window.destroy, bg='RED')
btn2.config(font=("Courier", 12))
btn2.pack()
btn3 = Button(window, text='DARK MODE', width=20, command=mode1, bg='Black', fg='White')
btn3.config(font=("Courier", 12))
btn3.pack()
btn4 = Button(window, text='LIGHT MODE', width=20, command=mode2, fg='Black', bg='WHITE')
btn4.config(font=("Courier", 12))
btn4.pack()

window.mainloop()
