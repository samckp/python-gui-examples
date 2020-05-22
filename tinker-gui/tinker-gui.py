from tkinter import *
window = Tk()
window.title("Welcome to Tinker GUI App")
window.geometry('350x200')
lbl = Label(window, text="GUI Testing ")
lbl.grid(column=0, row=0)
btn = Button(window, text="Click Me")
btn.grid(column=1, row=0)
window.mainloop()