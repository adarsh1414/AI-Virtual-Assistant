# To install Packages open terminal and pip install package_name
import subprocess#allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes
import pyautogui #cross-platform GUI automation Python module for human beings. Used to programmatically control the mouse & keyboard
import psutil #Cross-platform lib for process and system monitoring in Python
import pyttsx3 #is a text to speech conversion
import speech_recognition as sr #understand whatever the humans speak and converts the speech to text
import datetime #it works on date and time
import wikipedia #extracts data’s required from Wikipedia
import webbrowser #in-built package in python. It extracts data from the web
import os # it is a module provides the function to interact with operating system
import smtplib #to sender and receiver email addresses
import ecapture as ec #to capture images from your camera
import time # module helps us to display time
import subprocess as call # standard library use to process various system commands like to log off or to restart your PC
import requests #request module is used to send all types of HTTP request. Its accepts URL as parameters and gives access to the given URL’S
import _json #module is used f
import wolframalpha # API which can compute expert-level answers using Wolfram’s algorithms, knowledge base and AI technology
from AppOpener import open #for opening the apps

print('Loading your AI personal assistant Addy')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading your AI personal assistant Addy")
wishMe()


if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Addy is shutting down,Good bye')
            print('your personal assistant Addy is shutting down,Good bye')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(3)

        elif "close youtube" in statement:
            os.system("taskkill /f /im msedge.exe")

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(3)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(3)

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is{strTime}")

        elif 'news' in statement:

            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headline")
            speak("Here are some headlines from the Times of India,Happy reading")
            print("Here are some headlines from the Times of India,Happy reading")
            time.sleep(4)

        elif "camera" in statement or "take a photo" in statement or "photo" in statement:
            ec.capture(0,"robo camera","img.jpg")

        elif 'search' in statement:
            statement = statement.replace("Search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(3)

        elif "features" in statement or 'calculate' in statement:
            speak("I can answer to computational and geographical questions and what question do you want to ask now")
            questions=takeCommand()
            app_id="JG2U7T-4UL98HHPPK"
            client = wolframalpha.Client('JG2U7T-4UL98HHPPK')
            res = client.query(questions)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("What is the city name")
            city_name=takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x['main']
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

            else:
                speak("City Not Found")


        elif "what are you doing" in statement or "How are you" in statement:
            speak("I am good Waiting for your commannd sir..")
            print("I am good Waiting for your commannd sir..")
            time.sleep(3)

        elif 'hey' in statement or 'hello' in statement or 'whatsup' in statement:
            speak("Welcome sir, How can I help you..")
            print("Welcome sir, How can I help you..")
            time.sleep(3)

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Adarsh Gupta")
            print("I was built by Adarsh Gupta")
            time.sleep(3)

        elif "word" in statement or 'open word' in statement:
            speak("Opening Microsoft Word")
            print("Opening Microsoft Word")
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk")
            time.sleep(3)

        elif "excel" in statement:
            speak("Opening Excel")
            print("Opening Excel")
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk")
            time.sleep(3)

        elif "Powerpoint" in statement or "ppt" in statement or "open ppt" in statement or "open powerpoint" in statement:
            speak("Opening Powerpoint")
            print("Opening Powerpoint")
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk")
            time.sleep(3)

        elif "note" in statement or "notepad" in statement  or "open notepad" in statement:
            speak("Opening Notepad")
            print("Opening Notepad")
            os.startfile("notepad")
            time.sleep(3)

        elif "microsoft edge" in statement or "edge" in statement:
            speak("Opening Microsft Edge")
            print("Opening Microsft Edge")
            os.startfile("msedge")
            time.sleep(3)

        elif "music" in statement or "play music" in statement:
            speak("Playing Music")
            print("Playing Music")
            os.startfile("spotify")
            time.sleep(3)

        elif "open telegram" in statement or "telegram" in statement:
            speak("Opening Telegram")
            print("Opening Telegram")
            open("telegram desktop")
            time.sleep(3)

        elif "open whatsapp" in statement:
            speak("opening whatsapp")
            open("whatsapp")
            time.sleep(3)

        elif "send whatsapp message" in statement:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = takeCommand().lower()
            open("whatsapp")
            speak("I've sent the message sir.")

        elif "vs code" in statement or "visual studio" in statement:
            speak("opening vs")
            open("visual studio code")
            time.sleep(3)

        elif "piecharm" in statement or "pie" in statement:
            speak("opening pycharm  for happy python coding")
            open("pycharm community edition")
            time.sleep(3)

        elif "mail" in statement or "write a mail" in statement:
            speak("Opening email")
            open("mail")
            time.sleep(3)


        elif "calculator" in statement:
            os.startfile("calc")
            speak("Opening Calculator")
            print("Opening Calculator")
            time.sleep(3)

        elif "battery percentage" in statement or "battery status" in statement or "batter" in statement:
            batteryinformation = psutil.sensors_battery()
            speak("The battery percentage of the system is "+str(batteryinformation.percent))
            print("The battery percentage of the system is "
                  ,batteryinformation.percent)
            if batteryinformation.power_plugged == True:
                speak("The battery of the system is charging")
                print("The battery of the system is charging")
            time.sleep(3)

        elif "find my ip address"  in statement or "my ip address" in statement:
            ip_addess = requests.get("https://api64.ipify.org?format=json").json()
            speak(ip_addess['ip'])
            print(ip_addess['ip'])
            time.sleep(3)

        elif "joke" in statement or "tell joke" in statement:
            headers = {
                'Accept': 'application/json'
            }
            res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
            speak(res['joke'])
            print(res['joke'])
            time.sleep(3)

        elif "tell me advice" in statement or "advice" in statement:
            res = requests.get("http://api.adviceslip.com/advice").json()
            speak(res['slip']['advice'])
            print(res['slip']['advice'])
            time.sleep(3)

        elif "cpu usage" in statement or "cpu" in statement:
            speak("The CPU Usage is "+str(psutil.cpu_percent(4)))
            print("The CPU Usage is ", psutil.cpu_percent(4))
            time.sleep(3)

        elif "ram" in statement:
            speak("Ram memory % used is"+str(psutil.virtual_memory()[2]))
            speak("Ram memory GB is"+str(psutil.virtual_memory()[3]/1000000000))
            print("Ram memory % used is",psutil.virtual_memory()[2])
            print("Ram memory GB is" ,(psutil.virtual_memory()[3] / 1000000000))
            time.sleep(3)

        elif "lof of" in statement or "sign out" in statement or "switch off" in statement:
            speak("ok, your pc will log of in 10 sec make sure you exit from all application")
            subprocess.call("shutdown /s /t 1")
            time.sleep(3)

        elif "mute" in statement:
            speak("The system is on mute mood sir")
            pyautogui.press("volumemute")
            time.sleep(3)

        elif "are you single" in statement or "single" in statement:
            speak("I am in a relationship with wifi")
            print("I am in a relationship with wifi")
            time.sleep(3)

        elif "search on youtube" in statement:
            speak("Opening Sir")
            statement = statement.replace("Seach on youtube", "")
            webbrowser.open(f"www.youtube.com/results?search_statement={statement}")
            time.sleep(3)


        elif "where is" in statement:
            statement = statement.split(" ")
            location_url = "https://www.google.com/maps/place/" + str(statement[2])
            speak("Hold on Sir, I will show you where" + statement[2] + " is.")
            webbrowser.open(location_url)
            time.sleep(3)

        elif "restart the system" in statement:
            os.startfile("shutdown /r /t 5")
            time.sleep(3)

        elif "lock the system" in statement:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            time.sleep(3)

        elif "take screenshot" in statement or "screenshot" in statement or "take a screenshot" in statement:
            speak("tell me a name for the file")
            name = takeCommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot saved")

        elif "volume up" in statement or "volume increase" in statement or "increase volume" in statement:
            speak("Volume Increseing")
            pyautogui.press("volumeup")

        elif "volume decrease" in statement or "decrease volume" in statement or "volume down" in statement:
            speak("volume decreasing")
            pyautogui.press("volumedown")











