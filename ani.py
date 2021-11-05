from tkinter import *
from PIL import Image

root = Tk()
root.configure(bg='black')

im = Image.open('image/ani.gif')
test = im.n_frames
print(test)
photo = [PhotoImage(file='image/ani.gif', format=f'gif -index {i}') for i in range(test)]

count = 0
def animation(count):
    im1 = photo[count]
    label.config(image=im1)
    count += 1
    if count == test:
        count = 0

    root.after(20, lambda: animation(count))

global label
label = Label(image="")
label.pack()
animation(count)

mainloop()