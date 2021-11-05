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
from tkinter import filedialog
from PIL import Image, ImageTk, ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
from bs4 import BeautifulSoup as soup
#import winsound

#clear console
os.system('cls')

#engine of dude
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)
#winsound.PlaySound("dude.wav", winsound.SND_ASYNC | winsound.SND_LOOP)

#client for call and message
acc_id = "AC8a2069611989b3df4acb2fe9180da404"
acc_token = "945ea4d751b53afb6c29e3ff894b92b1"

'''
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
'''
def msg(message):
    mess = str(message)
    label1 = Label(box, text=mess, bg="#04223e", fg="white", font=("MV Boli", 11),wraplength=400, justify="left")
    label1.pack(anchor=W)
    label1.after(30000, lambda : label1.destroy())

def change_color():
    hexa = "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    root.configure(bg=hexa)
    text1.configure(bg=hexa)
    text2.configure(bg=hexa)
    text3.configure(bg=hexa)
    center_img.configure(bg=hexa)
    center_bottom.configure(bg=hexa)
    top.configure(bg=hexa)
    voice.configure(bg=hexa)

def change_voice():
    speak("OK, i am changing my voice")
    msg("OK, i am changing my voice")
    root.update_idletasks()
    root.update()
    value = random.choice(voices)
    engine.setProperty('voice', value.id)
    speak("Voice Changed Successfully")
    msg("Voice Changed Successfully")

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
        root.update_idletasks()
        root.update()
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
        speak("Email sended successfully")
        msg("Email sended successfully")
    except Exception as e:
        print(e)
        speak("Not able to send mail")
        msg("Not able to send mail")

def timer():
    hours = str(datetime.datetime.now().hour)
    minutes = str(datetime.datetime.now().minute)
    seconds = str(datetime.datetime.now().second)
    time = hours+":"+minutes+":"+seconds
    times.config(text=time)
    times.after(1000, timer)

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
        msg("listening")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise = 1
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
    querys.delete(0, END)
    return query

#funtion where user talk
def chating(e=""):
    q = chat()
    task(q)

'''
def day():
    date = str(datetime.datetime.now().day)
    month = str(datetime.datetime.now().month)
    year = str(datetime.datetime.now().year)
    #day = datetime.datetime.today().weekday() + 1
    #if day in Day_dict.keys(): 
    #    day_of_the_week = Day_dict[day] 
     #   msg("Today day is " + day_of_the_week) 
      #  speak("Today day is " + day_of_the_week) 
    msg("And date is " + date + "/" + month + "/" + year)
    speak("And date is " + date)
    speak("Month is " + month)
    speak("Year is" + year)
'''

#activate dude
def active():
    root.withdraw()
    while True:
        wake = talk().lower()
        if 'activate' in wake:
            root.deiconify()
            wish()
            break

def root2():
    global top
    top = Toplevel()
    label_top=Label(top, text="Enter Query")
    label_top.grid(row=0, column=0, pady=2)
    global entry
    entry=Text(top, width=20, height=3)
    entry.grid(row=0, column=1, pady=2)
    entry.bind('<Return>', lambda x : top.quit())
    button = Button(top, text="Submit", command=lambda : top.quit())
    button.grid(row=1, column=0, columnspan = 2, pady=2)
    top.mainloop()
    return entry.get("1.0", "end-1c")

#function where task for dude
def task(query):
    query = query.lower()
    speak(query)
    msg(query)
    #search on wikipeadia
    if 'wikipedia' in query:
        speak('Searching for wikipedia query...')
        try:
            result = wiki.summary(query, sentences=2)
            speak("According to Wikipedia")
            msg(result)
            root.update_idletasks()
            root.update()
            speak(result)
            last_task.config(text="Wikipedia")
        except Exception as e:
            speak("Due to some problem, I am not able to access wikipedia regarding")
            speak(query)
            print(e)

    #opens youtube
    elif 'open' in query and 'youtube' in query:
        try:
            speak("Opening Youtube")
            msg("Opening Youtube")
            wb.open('https://www.youtube.com/')
            last_task.config(text="Open Youtube")
        except Exception as e:
            print(e)
            speak("Due to some problem, I am not able to open")

    #opens google
    elif 'open' in query and 'google' in query:
        try:
            speak("Opening Google")
            msg("Opening Google")
            wb.open('https://www.google.com/')
            last_task.config(text="Open Google")
        except Exception as e:
            print(e)
            speak("Due to some problem, I am not able to open")

    #opens VS Code
    elif 'open vs code' in query or 'open code' in query:
        path = "C:\\Users\\raghav\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        speak("Opening VS Code. Enjoy your coding time")
        msg("Opening VS Code. Enjoy your coding time")
        os.startfile(path)
        last_task.config(text="Open VS Code")

    #tells joke
    elif 'joke' in query:
        joke = pyjokes.get_joke()
        msg(joke)
        root.update_idletasks()
        root.update()
        speak(joke)
        last_task.config(text="Joke")

    #terminate from program
    elif 'quit' in query:
        speak('It was nice to help you')
        speak('Dude out!!!')
        msg('It was nice to help you')
        msg('Dude out!!!')
        exit()

    #tells weather
    elif 'weather' in query or 'temperature' in query:
        wolfram(query)
        last_task.config(text="Weather")

    #calculate the value
    elif 'calculate' in query:
        wolfram(query)
        last_task.config(text="Calculate")

    #search for value in google
    elif 'search' in query and 'for' in query:
        try:
            last_task.config(text="Search")
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
        root.update_idletasks()
        root.update()
        speak("I am DUDE, virtual artificial intelligence made by Raghav")

    elif 'how are you' in query:
        msg("I am fine sir")
        root.update_idletasks()
        root.update()
        speak("I am fine sir")

    elif 'fine' in query or 'good' in query:
        speak('Thats Great')

    #play video in youtube and also can download it!
    elif 'video on' in query:
        try:
            last_task.config(text="Video on " + str(query))
            query = query.replace('play video on ', '')
            query = query.replace(' ', '+')
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + query)
            video = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            speak("Enjoy the video on " + query)
            wb.open("https://www.youtube.com/watch?v=" + video[0])
            time.sleep(10)
            msg("Do you want to download this song")
            msg("If yes then press Y else press N")
            root.update_idletasks()
            root.update()
            speak("Do you want to download this song")
            speak("If yes then press Y else press N")
            value = root2()
            top.destroy()
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

    elif 'play' in query and 'song' in query:
        path = "C:\\Users\\raghav\\Music\\Playlists"
        speak("Playing a song. Please wait")
        msg("Playing a song. Please wait")
        root.update_idletasks()
        root.update()
        song = os.listdir(path)
        value = random.choice(song)
        os.startfile(os.path.join(path, value))
        last_task.config(text="Played Song")

    elif 'track' in query and 'phone' in query:
        try:
            speak("Tracking your Phone")
            msg("Tracking your phone")
            root.update_idletasks()
            root.update()
            number = '9953181244'
            client = Client(acc_id, acc_token)
            call = client.calls.create(
                    twiml='<Response><Say>I am DUDE, virtual artificial intelligence made by Raghav</Say></Response>',
                    to = '+91'+number,
                    from_ = '+19138082981'
            )
            speak("Calling your Phone")
            last_task.config(text="Phone Track")
        except Exception as e:
            print(e)
            speak("Due to some problem, I am not able to call")

    elif 'message' in query:
        try:
            msg("Enter the number whom you want to send message")
            root.update_idletasks()
            root.update()
            speak("Enter the number whom you want to send message")
            number = root2()
            top.destroy()
            msg("What message you want to send")
            root.update_idletasks()
            root.update()
            speak("What message you want to send")
            message = root2()
            top.destroy()
            client = Client(acc_id, acc_token)
            message_no = client.messages.create(
                    body = message,
                    from_ = '+19138082981',
                    to = '+91'+number
            )
            print(message_no.sid)
            speak("Messaging")
            msg("Messaging")
            last_task.config(text="Sending Message")
        except Exception as e:
            print(e)
            speak("Due to some problem, I am not able to send message")

    elif 'wait' in query:
        speak("Ok. I am going to sleep for 10 seconds")
        msg("Ok. I am going to sleep for 10 seconds")
        root.update_idletasks()
        root.update()
        time.sleep(10)

    elif 'sleep' in query:
        speak("Ok, I am going to sleep. If you want to activate again then spell the magical wordS... 'ACTIVATE DUDE'")
        msg("Ok, I am going to sleep. If you want to activate again then spell the magical wordS... 'ACTIVATE DUDE'")
        active()

    elif 'time' in query:
        hours = str(datetime.datetime.now().hour)
        minutes = str(datetime.datetime.now().minute)
        msg("The time is "+hours+":"+minutes)
        root.update_idletasks()
        root.update()
        speak("The time is "+hours+":"+minutes)
        last_task.config(text="Time")

    elif 'date' in query or 'day' in query:
        day = str(datetime.datetime.now().day)
        month = str(datetime.datetime.now().month)
        year = str(datetime.datetime.now().year)
        msg(month + ", " + day + " " + year)
        root.update_idletasks()
        root.update()
        speak(month + ", " + day + " " + year)
        last_task.config(text="Date")     

    elif 'send' in query and 'mail' in query:
        msg("Who do you want to send email")
        root.update_idletasks()
        root.update()
        speak("Who do you want to send email")
        to = root2()
        top.destroy()
        msg("what message you want to send")
        root.update_idletasks()
        root.update()
        speak("what message you want to send")
        letter = root2()
        top.destroy()
        email(letter, to)
        last_task.config(text="Send Mail")

    elif 'change' in query and 'voice' in query:
        change_voice()
        last_task.config(text="Voice Change")

    elif 'change' in query and 'background' in query:
        change_color()
        last_task.config(text="Background Change")

    elif 'screen' in query and 'record' in query:
        speak("Starting screen recorder")
        msg("Starting screen recorder")
        root.update_idletasks()
        root.update()
        width = GetSystemMetrics(0)
        height = GetSystemMetrics(1)
        time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        file_name = f'{time_stamp}.mp4'
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

        while True:
            img = ImageGrab.grab(bbox=(0, 0, width, height))
            img_np = np.array(img)
            img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            cv2.imshow('Secret Capture', img_final)
            captured_video.write(img_final)
            if cv2.waitKey(10) == ord('q'):
                break
        last_task.config(text="Record Screen")
    
    elif 'notes' in query:
        speak("What should i write")
        msg("What should i write")
        root.update_idletasks()
        root.update()
        note = root2()
        top.destroy()
        speak("What should i name the file")
        msg("What should i name the file")
        root.update_idletasks()
        root.update()

        file_names = root2()
        top.destroy()
        file = open(str(file_names) + '.txt', 'w')
        speak("Should i include date and time")
        msg("Should i include date and time")
        root.update_idletasks()
        root.update()
        snfm = root2()
        top.destroy()
        
        if 'yes' in snfm or 'sure' in snfm:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            file.write(strTime)
            file.write(" :- ")
            file.write(note)
        
        else:
            file.write(note)
        
        speak("File Created")
        msg("File Created")
        root.update_idletasks()
        root.update()
        last_task.config(text="Notes")
    
    elif 'open' in query and 'file' in query:
        open_file = filedialog.askopenfilename(initialdir='/image', title="Select A File")
        speak("Opening file")
        msg("Opening file")
        os.startfile(open_file)
        last_task.config(text="Open a file")

    elif 'news' in query:
        news_url = "https://news.google.com/news/rss"
        speak("Ok, i am telling you top 5 news")
        msg("Ok, i am telling you top 5 news")
        root.update_idletasks()
        root.update()
        client = urllib.request.urlopen(news_url)
        xmlpage = client.read()
        client.close()
        page = soup(xmlpage, "html.parser")
        list = page.findAll("item")
        for i in range(5):
            lists = list[i]
            msg("News " + str(i+1) + ":" + lists.title.text)
            root.update_idletasks()
            root.update()
            speak("News " + str(i+1) + ":" + lists.title.text)
        last_task.config(text="News")

root = Tk()

root.title("Dude - Virtual Voice Assistant")
root.attributes('-fullscreen', True)
root.configure(bg='black')
#root.wm_attributes("-transparentcolor", 'black')

#add menu bar
menubar = Menu(root)
setting = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Setting', menu = setting)
setting.add_command(label ='Change Background', command = change_color)
setting.add_command(label ='Change Voice', command = change_voice)
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

im6 = Image.open('image/send_2x_white.png')
im6 = im6.resize((50, 50), Image.ANTIALIAS)
photo6 = ImageTk.PhotoImage(im6)

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

heading = Label(root, text="Last Task", fg="white", bg="#04223e", font=("MV Boli", 14))
heading.place(x=155, y=450)

last_task = Label(root, text="None", fg="white", bg="#04223e", font=("MV Boli", 14))
last_task.place(x=155, y=500)

#chatting space
global box
box = LabelFrame(root, bg="#04223e", fg="white", width=450)
box.pack(side = RIGHT, fill = Y)
box.pack_propagate(False)
box.bind('<Enter>', lambda x : msg("How can I help you?"))

querys = Entry(box, font=("MV Boli", 11), width=35)
querys.pack(anchor="w", side="bottom", ipady=8, pady=5)
querys.bind('<Return>', chating)

submit = Button(box, image=photo6, command=chating, bg="#04223e", activebackground="#04223e", borderwidth=0)
submit.place(x=395, y=585)

timer()

if __name__ == '__main__':
    #active()
    wish()

mainloop()