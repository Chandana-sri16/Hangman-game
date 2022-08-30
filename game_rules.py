from tkinter import *

def rules():
    window = Tk()
    window.title("Hangman version 6.4.2")
    window.geometry("700x450")
    window.resizable(False, False)  # disables maximizing option
    # Background picture
    bg = PhotoImage(file="12game_rules.png")
    # label
    label = Label(window, image=bg, bg='pink')
    label.place(x=0, y=0, relwidth=1, relheight=1)

    window.mainloop()

