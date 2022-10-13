from tkinter import *
import time

# Functions


def clear_widget(widget):
    widget.destroy()


def calculate():
    try:
        if v.get() == 2:
            ppower = powerInput.get()
            ttime = timeInput.get()
            Intpower = int(ppower)
            Inttime = int(ttime)
            answer = Inttime*Intpower
        elif v.get() == 1:
            ppower = powerInput.get()
            ttime = timeInput.get()
            Intpower = int(ppower)
            powerDivision = Intpower/1000
            Inttime = int(ttime)
            answer = powerDivision*Inttime

        displayAnswer = Label(
            app, text=f'Your power consumption is {answer} Kwh')
        displayAnswer.grid(row=6, column=0, columnspan=2)

    except ValueError:
        displayError = Label(app, text="Please Enter A Value")
        displayError.grid(row=7, column=0)
        time.sleep(1)
        # clear_widget(displayError)


# window
app = Tk()
app.geometry("300x300")
app.title("Unit calculator")

# Main body
powerText = Label(app, text="Input Power(Kw): ")
powerText.grid(row=0, column=0, pady=10)

powerInput = Entry(app)
powerInput.grid(row=0, column=1)

timeText = Label(app, text="Input Time(hrs): ")
timeText.grid(row=2, column=0, pady=5)

timeInput = Entry(app)
timeInput.grid(row=2, column=1, pady=5)

# Make a selection
v = IntVar()
v.set('2')

radioButton = Radiobutton(app, text='W', padx=20, value=1, variable=v)
radioButton.grid(row=1, column=0)
radiobutton2 = Radiobutton(app, text='KW', padx=20, value=2, variable=v)
radiobutton2.grid(row=1, column=1)

# Enter button
enter = Button(app, text="Enter", command=calculate)
enter.grid(row=5, column=1, pady=10)

# Mainloop
app.mainloop()
