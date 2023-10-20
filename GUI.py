from tkinter import  *
from tkinter.scrolledtext import ScrolledText
from DES import *

T = Tk()
T.geometry("940x700")
T.title("DES Algorithm")
T.configure(background="lightblue")

#================================= CREATE THE NECESSARY WIDGETS HERE ==============================

Label1 = Label(T, text="Key", font="Calibri", bg="lightblue").place(x=60, y=60)
ED_Key = Entry(T, textvariable=mainKey, font="Calibri", width="50").place(x=60, y=100)


Label2 = Label(T, text="The Plain Text", font="Calibri", bg="lightblue").place(x=140, y=160)
clearBtn1 = Button(T, text="Clear", width="8", font="Calibri", command=clear1).place(x=180, y=310)


Label3 = Label(T, text="The Cipher Text", font="Calibri", bg="lightblue").place(x=560, y=160)
clearBtn2 = Button(T, text="Clear", width="8", font="Calibri", command=clear2).place(x=670, y=310)


encBtn = Button(T, text="Encrypt", width="8", font="Calibri", command=Encrypt).place(x=435, y=205)
decBtn = Button(T, text="Decrypt", width="8", font="Calibri", command=Decrypt).place(x=435, y=250)


plainText = ScrolledText(T, height=5, width=40)
cipherText = ScrolledText(T, height=5, width=40)
plainText.grid(row=1, column=1)
cipherText.grid(row=1, column=1)
plainText.place(x=60, y=200)
cipherText.place(x=540, y=200)

#Define a function to close the window
def close_win():
   T.destroy()


T.mainloop()