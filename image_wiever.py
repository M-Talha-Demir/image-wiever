from tkinter import *
from PIL import ImageTk, Image
import os
root = Tk()

root.title('TKINTER')
root.iconbitmap('eclipse-windows.ico')

dir_list = os.listdir("image")
num_image = 0


def fwrd_image():
    global num_image
    global my_label
    global dir_list
    num_image += 1
    path = "./image/" + dir_list[num_image]
    my_img = ImageTk.PhotoImage(Image.open(path))
    my_label.config(image=my_img)
    my_label.photo = my_img


def back_image():
    global num_image
    global my_label
    global dir_list
    num_image -= 1
    path = "./image/" + dir_list[num_image]
    my_img = ImageTk.PhotoImage(Image.open(path))
    my_label.config(image=my_img)
    my_label.photo = my_img


path = "./image/" + dir_list[num_image]
my_img = ImageTk.PhotoImage(Image.open(path))
my_label = Label(root, image=my_img)
my_label.grid(row=0, column=0, rowspan=3, columnspan=3)

button_next = Button(root, text=">>", command=fwrd_image)
button_next.grid(row=4, column=2)

button_pre = Button(root, text="<<", command=back_image)
button_pre.grid(row=4, column=0)

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.grid(row=5, column=1)


root.mainloop()