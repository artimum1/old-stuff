from tkinter import *
import string
import random

root = Tk()

root.title("Password Generator")
root.configure(bg='#d07fdd')

def generate() :
    length = e.get()
    all = string.ascii_lowercase + string.ascii_uppercase + string.digits
    e1.delete(0, END)
    for i in range(int(length)) :
        r = random.randint(0, 61)
        v = all[r]
        e1.insert(0, v)

label = Label(root, text='Type the length of your password', bg='#d07fdd')
label1 = Label(root, text='You password is : ', bg='#d07fdd')
space = Label(root, text=' \n', bg='#d07fdd')
space1 = Label(root, text=' \n \n', bg='#d07fdd')
e = Entry(root)
e1 = Entry(root, width=60)
quit_button = Button(root, text='Quit', command=quit, bg='#bc46ce', padx= 200, bd=4)
button = Button(root, text='Generate', command= generate, bg='#bc46ce', padx= 20, pady= 5, bd= 4)

label.pack()
e.pack()
button.pack()
space.pack()
label1.pack()
e1.pack()
space1.pack()
quit_button.pack()

root.mainloop()