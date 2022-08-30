from tkinter import *
from easy import easy_level
from medium import medium_level
from hard import hard_level
def game_levels():
    window = Tk()
    window.title("Hangman")
    window.geometry("200x100")
    label = Label(window,bg='pink')
    label.place(x=0, y=0, relwidth=1, relheight=1)
    window.resizable(False, False)

    def difficulty(value):
        level=options.get()
        if level=='EASY':
            window.destroy()
            easy_level()
        if level =='MEDIUM':
            window.destroy()
            medium_level()
        if level =='HARD':
            window.destroy()
            hard_level()

    list1 = ["EASY", "MEDIUM", "HARD"]
    options = StringVar(window)
    options.set('LEVELS')
    om1 = OptionMenu(window, options, *list1,command=difficulty)  # command=difficulty will save the users selected option
    om1.place(relx=0.95, rely=0.3, anchor='ne')  # place method is used to place the label in correct position
    lbl = Label(window, text='select level:', font=('Constantia bold', 13), fg='black', bg='pink')
    # lbl label for user convenience understanding to select the theme from option menu
    lbl.place(relx=0.52, rely=0.32, anchor='ne')
    window.mainloop()