import pyttsx3 #engine of voice
import datetime #date and time of system
import time
import speech_recognition as sr #recognize what we speak
import wikipedia as wiki #search item in wikipedia
import webbrowser as wb #open web brower
import os #os of system
import random #generate random value
import pyjokes #generate random jokes
import wolframalpha #search anything you want
import urllib.request #open specific url
import re #search value from console
from pytube import YouTube #download video from youtube
from twilio.rest import Client #makes call and message
import smtplib #send mail
from tkinter import *
from PIL import Image, ImageTk
#from dude_ui import *
#import winsound

#clear console
os.system('cls')
global msg

#engine of dude
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)
#winsound.PlaySound("dude.wav", winsound.SND_ASYNC | winsound.SND_LOOP)

#client for call and message
acc_id = "AC8a2069611989b3df4acb2fe9180da404"
acc_token = "945ea4d751b53afb6c29e3ff894b92b1"
client = Client(acc_id, acc_token)

#Day of Week
Day_dict = {
    1: 'Monday', 
    2: 'Tuesday',                         
    3: 'Wednesday',
    4: 'Thursday',  
    5: 'Friday', 
    6: 'Saturday', 
    7: 'Sunday'
    } 

def msg(message):
    mess = str(message)
    label1 = Label(box, text=mess, bg="#04223e", font=("MV Boli", 11),wraplength=400, justify="left")
    label1.pack(anchor=W)
    label1.after(15000, lambda : label1.destroy())

#fuction where dude speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#function for wolframalpha
def wolfram(query):
    try:
        app_id = "4PR658-EH496Q2K4X"
        client = wolframalpha.Client(app_id)
        res = client.query(''.join(query))
        ans = next(res.results).text
        msg('Answer is ' + ans)
        speak('Answer is ' + ans)
    except Exception as e:
        print(e)
        speak("Due to some problem, I am not able to process")

#function to send mail
def email(body, to):
    try:
        user = "babbarraghav44@gmail.com"
        password = "fsepzqpcpccrfgkd"
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, password)
        server.sendmail(user, to, body)
        server.close()
    except Exception as e:
        print(e)
        speak("Not able to send mail")

#function where dude wish
def wish():
    speak("Activating Dude")
    hour = datetime.datetime.now().hour
    if hour>0 and hour<12:
        speak("Good Morning")

    elif hour>12 and hour<18:
        speak("Good Afternoon")

    elif hour>18 and hour<21:
        speak("Good Evening")

    else:
        speak("Good Night")

    speak("Now its time to introduce myself. I am DUDE, the virtual artificial intelligence, and I am here to assist you with the varity of task as best as I can, 24 hours a day, 7 days a week, importing all preferences from home interface system are now fully operational")
    msg("Now its time to introduce myself. I am DUDE, the virtual artificial intelligence, and I am here to assist you with the varity of task as best as I can, 24 hours a day, 7 days a week, importing all preferences from home interface system are now fully operational")
    #winsound.PlaySound(None, winsound.SND_ASYNC)

#function where user output returns
def talk():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            #msg("recognise")
            query = r.recognize_google(audio, language="en-IN")
            #msg("user said: ", query)

        except Exception as e:
            print(e)
            print("Not recognize what you said. Can you please repeat?")
            speak("Not recognize what you said. Can you please repeat?")
            return "None"

    return query

#funtion where user talk
def talking():
    msg("How can I help you")
    speak("How can I help you")
    query = talk()
    task(query)

def chat():
    msg("listening")
    query = querys.get()
    msg(query)
    return query

#funtion where user talk
def chating():
    q = chat()
    task(q)

def day():
    date = str(datetime.datetime.now().day)
    month = str(datetime.datetime.now().month)
    year = str(datetime.datetime.now().year)
    day = datetime.datetime.today().weekday() + 1
    if day in Day_dict.keys(): 
        day_of_the_week = Day_dict[day] 
        msg("Today day is " + day_of_the_week) 
        speak("Today day is " + day_of_the_week) 
        msg("And date is " + date + "/" + month + "/" + year)
        speak("And date is " + date)
        speak("Month is " + month)
        speak("Year is" + year)

def active():
    root.withdraw()
    while True:
        wake = talk().lower()
        if 'activate' in wake:
            root.deiconify()
            wish()
            break

def task(query):
    query = query.lower()
    speak(query)
    #search on wikipeadia
    if 'wikipedia' in query:
        speak('Searching for wikipedia query...')
        try:
            result = wiki.summary(query, sentences=2)
            speak("According to Wikipedia")
            msg(result)
            speak(result)
        except Exception as e:
            speak("Due to some problem, I am not able to access wikipedia regarding")
            speak(query)
            print(e)

    #opens youtube
    elif 'open youtube' in query:
        try:
            speak("Opening Youtube")
            msg("Opening Youtube")
            wb.open('https://www.youtube.com/')
        except Exception as e:
            print(e)
            speak("Due to some problem, I am not able to open")

    #opens google
    elif 'open google' in query:
        try:
            speak("Opening Google")
            msg("Opening Google")
            wb.open('https://www.google.com/')
        except Exception as e:
            print(e)
            speak("Due to some problem, I am not able to open")

    #opens VS Code
    elif 'open vs code' in query:
        path = "C:\\Users\\raghav\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        speak("Opening VS Code. Enjoy your coding time")
        msg("Opening VS Code. Enjoy your coding time")
        os.startfile(path)

    #tells joke
    elif 'joke' in query:
        joke = pyjokes.get_joke()
        msg(joke)
        speak(joke)

    #terminate from program
    elif 'quit' in query:
        speak('It was nice to help you')
        speak('Dude out!!!')
        msg('It was nice to help you')
        msg('Dude out!!!')
        exit()

    #tells weather
    elif 'weather' in query:
        wolfram(query)

    #calculate the value
    elif 'calculate' in query:
        wolfram(query)

    #search for value in google
    elif 'search for' in query:
        try:
            query = query.replace("search for", "")
            msg('Searching for ' + query)
            speak('Searching for ' + query)
            query = query.replace(" ", "+")          
            wb.open("https://www.google.com/search?q="+query)
        except Exception as e:
            print(e)
            speak("Due to some problem, I am not able to search")

    #tell about himself
    elif 'who are you' in query:
        msg("I am DUDE, virtual artificial intelligence made by Raghav")
        speak("I am DUDE, virtual artificial intelligence made by Raghav")

    elif 'how are you' in query:
        msg("I am fine sir")
        speak("I am fine sir")

    elif 'fine' in query or 'good' in query:
        speak('Thats Great')

    #play video in youtube and also can download it!
    elif 'video on' in query:
        try:
            query = query.replace('play video on ', '')
            query = query.replace(' ', '+')
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + query)
            video = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            speak("Enjoy the video on " + query)
            wb.open("https://www.youtube.com/watch?v=" + video[0])
            time.sleep(10)
            speak("Do you want to download this song")
            speak("If yes then press Y else press N")
            value = chat()
            if 'y' in value or 'Y' in value:
                yt = YouTube("https://www.youtube.com/watch?v=" + video[0])
                speak("Downloading " + query)
                msg("Downloading " + query)
                videos = yt.streams.filter(only_audio=True).first()
                videos.download('C:\\Users\\raghav\\Music\\Playlists')
                speak("Downloaded")
                msg("Downloaded")

            else:
                speak("OK")
        except Exception as e:
            print(e)
            speak("Due to some problem, I am not able to open")

    elif 'play song' in query:
        path = "C:\\Users\\raghav\\Music\\Playlists"
        speak("Playing a song. Please wait")
        msg("Playing a song. Please wait")
        song = os.listdir(path)
        value = random.choice(song)
        os.startfile(os.path.join(path, value))

    elif 'call' in query:
        try:
            speak("Who do you want to call")
            msg("Who do you want to call")
            number = chat()
            call = client.calls.create(
                    twiml='<Response><Say>I am DUDE, virtual artificial intelligence made by Raghav</Say></Response>',
                    to = '+91'+number,
                    from_ = '+19138082981'
            )
            speak("Calling")
        except Exception as e:
            print(e)
            speak("Due to some problem, I am not able to call")

    elif 'message' in query:
        try:
            msg("Enter the number whom you want to send message")
            speak("Enter the number whom you want to send message")
            number = chat()
            msg("What message you want to send")
            speak("What message you want to send")
            message = chat()
            message_no = client.messages.create(
                    body = message,
                    from_ = '+19138082981',
                    to = '+91'+number
            )
            print(message_no.sid)
            speak("Messaging")
        except Exception as e:
            print(e)
            speak("Due to some problem, I am not able to send message")

    elif 'wait' in query:
        speak("Ok. I am going to sleep for 10 seconds")
        msg("Ok. I am going to sleep for 10 seconds")
        time.sleep(10)

    elif 'sleep' in query:
        speak("Ok, I am going to sleep. If you want to activate again then spell the magical wordS... 'ACTIVATE DUDE'")
        msg("Ok, I am going to sleep. If you want to activate again then spell the magical wordS... 'ACTIVATE DUDE'")
        active()

    elif 'time' in query:
        hours = str(datetime.datetime.now().hour)
        minutes = str(datetime.datetime.now().minute)
        msg("The time is "+hours+":"+minutes)
        speak("The time is "+hours+":"+minutes)

    elif 'date' in query or 'day' in query:
        day()      

    elif 'send email' in query:
        msg("Who do you want to send email")
        speak("Who do you want to send email")
        to = chat()
        msg("what message you want to send")
        speak("what message you want to send")
        letter = chat()
        email(letter, to)

    elif 'change voice' in query:
        speak("OK, i am changing my voice")
        msg("OK, i am changing my voice")
        value = random.choice(voices)
        engine.setProperty('voice', value.id)

def timer():
    hours = str(datetime.datetime.now().hour)
    minutes = str(datetime.datetime.now().minute)
    seconds = str(datetime.datetime.now().second)
    time = hours+":"+minutes+":"+seconds
    times.config(text=time)
    times.after(1000, timer)

root = Tk()

root.title("Dude - Virtual Voice Assistant")
root.attributes('-fullscreen', True)
root.configure(bg='black')
#root.wm_attributes("-transparentcolor", 'black')

#add menu bar
menubar = Menu(root)
menubar.add_command(label="Setting", command=None)
menubar.add_command(label="Exit", command=exit)
root.config(menu=menubar)

#adding images
im1 = Image.open('image/text1.png')
im1 = im1.resize((165, 80), Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(im1)

im1 = im1.resize((165, 200), Image.ANTIALIAS)
text_huge = ImageTk.PhotoImage(im1)

im2 = Image.open('image/center_img.png')
im2 = im2.resize((200, 150), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(im2)

im3 = Image.open('image/center_bottom.png')
im3 = im3.resize((300, 150), Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(im3)

im4 = Image.open('image/top.png')
im4 = im4.resize((1366, 100), Image.ANTIALIAS)
photo4 = ImageTk.PhotoImage(im4)

im5 = Image.open('image/voice.png')
im5 = im5.resize((100, 100), Image.ANTIALIAS)
photo5 = ImageTk.PhotoImage(im5)

#adding images to root
text1 = Label(root, image=photo1, bg="black")
text1.place(x=115, y=200)

text2 = Label(root, image=photo1, bg="black")
text2.place(x=115, y=300)

text3 = Label(root, image=text_huge, bg="black")
text3.place(x=115, y=400)

center_img = Label(root, image=photo2, bg="black")
center_img.place(x=600, y=200)

center_bottom = Label(root, image=photo3, bg="black")
center_bottom.place(x=550, y=350)

top = Label(root, image=photo4, bg="black")
top.pack(fill=X, side=TOP)

voice = Button(root, image=photo5, bg="black", activebackground="black", bd=0, command=talking)
voice.place(x=650, y=600)

#values in images
day = str(datetime.datetime.now().day)
month = str(datetime.datetime.now().month)
year = str(datetime.datetime.now().year)
date = day + "/" + month + "/" + year
days = Label(root, text=date, fg="white", bg="#04223e", font=("MV Boli", 14))
days.place(x=145, y=225)

times = Label(root, text="", fg="white", bg="#04223e", font=("MV Boli", 14))
times.place(x=155, y=325)

#chatting space
global box
box = LabelFrame(root, bg="#04223e", fg="white", width=450)
box.pack(side = RIGHT, fill = Y)
box.pack_propagate(False)
box.bind('<Enter>', lambda x : msg("How can I help you?"))

querys = Entry(box, font=("MV Boli", 11), width=30)
querys.pack(anchor="w", side="bottom", ipady=8)

submit = Button(box, text="hello", width=14, command=chating)
submit.place(x=335, y=615)

timer()

#if __name__ == "__main__":
    #active()

mainloop()