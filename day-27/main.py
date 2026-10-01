from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = Label(text="I am a Label", font=('Arial', 24, 'bold'))
my_label.grid(column=0, row=0)
my_label.config(padx=10, pady=10)

my_label['text'] = "New Text"
# or
my_label.config(text="New Text")


# buttons
def button_clicked():
    my_label.config(text=entry.get())


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="No Click Me")
new_button.grid(column=3, row=0)

# entry
entry = Entry(width=10)
entry.grid(column=4, row=3)
entry.get()


window.mainloop()
