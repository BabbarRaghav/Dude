from tkinter import *
#from PIL import Image, ImageTk
import datetime

def timer():
    hours = str(datetime.datetime.now().hour)
    minutes = str(datetime.datetime.now().minute)
    seconds = str(datetime.datetime.now().second)
    time = hours+":"+minutes+":"+seconds
    times.config(text=time)
    times.after(1000, timer)

def active():
    global top
    top = Toplevel()
    text=querys.get()
    label_top=Label(top, text=text)
    label_top.grid(row=0, column=0, pady=2)
    global entry
    entry=Entry(top)
    entry.grid(row=0, column=1, pady=2)
    button = Button(top, text="hello", command=deactive)
    button.grid(row=1, column=0, columnspan = 2, pady=2)
    top.mainloop()

def deactive():
    text=entry.get()
    top.destroy()
    label1.config(text=text)

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
'''
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

voice = Button(root, image=photo5, bg="black", activebackground="black", bd=0)
voice.place(x=650, y=600)
'''
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
box = LabelFrame(root, bg="#04223e", fg="white", width=50)
box.pack(side = RIGHT, fill = Y)

label1 = Label(box, text="hello world", bg="#04223e", anchor=W, width=50, font=("MV Boli", 11))
label1.pack()

querys = Entry(box, font=("MV Boli", 11), width=30)
querys.pack(anchor="s", side = "left", ipady=8)

submit = Button(box, text="hello", width=20, command=active)
submit.pack(anchor="s", side = "right", padx=1)

timer()

root.mainloop()