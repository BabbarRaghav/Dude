'''
import os
import random
import datetime
import smtplib

path = "C:\\Users\\raghav\\Music\\Playlists"
song = os.listdir(path)
value = random.choice(song)
os.startfile(os.path.join(path, value))
date = str(datetime.datetime.now().day)
month = str(datetime.datetime.now().month)
year = str(datetime.datetime.now().year)
print(date)
print(month)
print(year)
print("And date is " + date + "/" + month + "/" + year)

def email_alert(subject, body, to):
    user = "babbarraghav44@gmail.com"
    password = "fsepzqpcpccrfgkd"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(user, password)
    server.sendmail(user, to, body)
    server.close()

from tkinter import *
from PIL import Image, ImageTk
import wikipedia as wiki
import datetime
import random

date = str(datetime.datetime.now().day)
month = str(datetime.datetime.now().month)
year = str(datetime.datetime.now().year)
day = date + "-" + month + "-" + year
new=Tk()
width= new.winfo_screenwidth()               
height= new.winfo_screenheight()               
new.geometry("%dx%d" % (width, height))
#new.attributes('-fullscreen', True)
new.configure(bg='black')
#new.wm_attributes("-transparentcolor", 'black')

def h():
    l=Label(labelframe,text='Hello guys, This is inside Label Frame')          
    l.pack()
    msg("xyz")
    msg("hh")
    l.after(2000, lambda : l.destroy())

labelframe = LabelFrame(new) #adding a labelframe to the window
labelframe.pack()              #organizing the widget into frame

button = Button(labelframe, text="hello", command=h)
button.pack()

button1 = Button(new, text = "Quit", anchor = W)
button1.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
button1.pack()

photo = PhotoImage(file = 'image/center.gif', format="gif -index 95")
label_test = Label(new, image=photo)
label_test.place(x=25, y=75)

im = Image.open('image/text_border.png')
im = im.resize((175, 75), Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(im)
test = Label(new, image=photo1, width = 155, height = 50)
test.place(x=115, y=145)

days = Label(new, text=day, fg="blue")
days.place(x=165, y=165)

def msg(message):
    label1 = Label(labelframe, text=message, bg="#04223e", font=("MV Boli", 11),wraplength=800, justify="left")
    label1.pack(anchor=W)
    label1.after(5000, lambda : label1.destroy())

labelframe.bind('<Enter>', msg)


def change_color():
    hexa = "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    new.configure(bg=hexa)
    box.configure(bg=hexa)

def msg(message):
    label1 = Label(box, text=message, bg="#04223e", font=("MV Boli", 11),wraplength=500, justify="left")
    label1.pack(anchor=W)
    #label1.after(15000, lambda : label1.destroy())

def message():
	text = querys.get()
	return text

def chating():
    q = message()
    task(q)

def task(query):
    if 'wikipedia' in query:
        print("1")
        #speak('Searching for wikipedia query...')
        try:
            print("2")
            result = wiki.summary(query, sentences=2)
            print("3")
            #speak("According to Wikipedia")
            msg(result)
            print("4")
            #speak(result)
        except Exception as e:
            speak("Due to some problem, I am not able to access wikipedia regarding")
            speak(query)
            print(e)

global box
box = LabelFrame(new, bg="#04223e", fg="white", width=450)
box.pack(side = RIGHT, fill = Y)
box.pack_propagate(False)
box.bind('<Enter>', lambda x : msg("How can I help you?"))

querys = Entry(box, font=("MV Boli", 11), width=30)
querys.pack(anchor="w", side="bottom", ipady=8)

submit = Button(box, text="hello", width=14, command=chating)
submit.place(x=335, y=615)

change = Button(box, text="change color", command=change_color)
change.pack()

mainloop()

import datetime

from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics

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
'''
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url = "https://news.google.com/news/rss"
client = urlopen(news_url)
xmlpage = client.read()
client.close()
page = soup(xmlpage, "html.parser")
list = page.findAll("item")
for i in range(10):
    lists = list[i]
    print(i+1)
    print(lists.title.text)
    #print(lists.pubDate.text)
    print("-"*60)