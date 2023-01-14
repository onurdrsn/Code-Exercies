#apt install python3-tk
#python3 -m pip install --upgrade pip setuptools
#pip3 install PyDictionary

from tkinter import *
from PyDictionary import PyDictionary

#Create Dictionary
dicti = PyDictionary()
root = Tk()

#set geometry
root.geometry("1000x450")

def dict():
    meaning.config(text=dicti.meaning(word.get())['Noun'][0])
    synonym.config(text=dicti.synonym(word.get()))
    antonym.config(text=dicti.antonym(word.get()))

#Add labels, button and frames
Label(root, text="Only English Dictionary", font=("Helvetica 20 bold"), fg="Green").pack(pady = 10)

#Frame1
frame = Frame(root)
Label(frame, text="Type Word: ", font=("Helvetica 15 bold")).pack(side=LEFT)
word = Entry(frame, font=("Helvetica 15 bold"))
word.pack()
frame.pack(pady=10)

#Frame2
frame1 = Frame(root)
Label(frame1, text="Anlamı: ", font=("Helvetica 10 bold")).pack(side=LEFT)
meaning = Label(frame1, text="", font=("Helvetica 10"))
meaning.pack()
frame1.pack(pady=10)

#Frame3
frame2 = Frame(root)
Label(frame2, text="Eş Anlamı: ", font=("Helvetica 10 bold")).pack(side=LEFT)
synonym = Label(frame2, text="", font=("Helvetica 10"))
synonym.pack()
frame2.pack(pady=10)

#Frame4
frame3 = Frame(root)
Label(frame3, text="Zit Anlamı: ", font=("Helvetica 10 bold")).pack(side=LEFT)
antonym = Label(frame3, text="", font=("Helvetica 10 bold"))
antonym.pack(side=LEFT)
frame3.pack(pady=10)

Button(root, text="Submit", font=("Helvetica 10 bold"), command=dict).pack()

root.mainloop()
