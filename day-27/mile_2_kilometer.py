from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=350, height=200)
window.config(padx=20, pady=20)

miles = Label(text="Miles", font=('Arial', 16, 'bold'))
miles.grid(column=3, row=0)
miles.config(padx=10, pady=10)

equal = Label(text="is equal to", font=('Arial', 16, 'bold'))
equal.grid(column=0, row=1)
equal.config(padx=10, pady=10)

converted = Label(text="0", font=('Arial', 16, 'bold'))
# converted['text'] = "New Text"
converted.grid(column=1, row=1)
converted.config(padx=10, pady=10)

km = Label(text="Km", font=('Arial', 16, 'bold'))
km.grid(column=2, row=1)
km.config(padx=10, pady=10)

def convert():
    converted.config(text=float(input.get()) * 1.609)

button = Button(text="Click Me", command=convert)
button.grid(column=1, row=2)

input = Entry(width=10)
input.grid(column=1, row=0)

window.mainloop()
