# modules needed for the program
from tkinter import *
import pathlib

# The function to handle the submit button


def Onclick():
    listbox.insert(END, newEntry.get())
    db = open('close.txt', 'a')
    db.write(newEntry.get())
    db.close

# function to handle the clear button


def clear():
    listbox.delete(END)


# variables
width = 400
heigth = 300
# Main window
app = Tk()
# app.geometryn and title('500*500')
app.title('Trying out tkinter')
app.geometry(f'{width}x{heigth}')

# Name
name = Label(app, text='Enter a TODO task here: ', font='tahoma')
name.grid(row=0, column=0, pady=20)

# Entry: To enter and store the user input
value = StringVar()  # To hold the user input in a variable
newEntry = Entry(app, textvariable=value)  # Define the entry
newEntry.grid(row=1, column=1)

# submitButton
submit = Button(app, width='6', text='submit', command=Onclick)
submit.grid(row=0, column=2)

# clearButton
clear = Button(app, width='6', text='clear', command=clear)
clear.grid(row=1, column=2, padx='10')

# Listbox
listbox = Listbox(app, height='20', width='50')
listbox.grid(row=2, pady=120)

db = open(
    'C:\\Users\\kemzzy\\Documents\\My python files\\Completed projects\\close.txt', 'r')
listbox.insert(END, db.readlines())
db.close()

# Mainloop
app.mainloop()
