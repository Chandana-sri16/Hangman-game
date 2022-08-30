"""
   Welcome to Hangman Game...
   coded using Tkinter library to run the game on GUI interface.
   This makes the user more interactive towards the game
   Get started with Hangman game....
"""
from tkinter import *
from tkinter import messagebox
from levels import game_levels
from game_rules import rules
from keys import *

def hangman_game():
    # displays root window
    window = Tk()
    window.title("Hangman version 6.4.2")
    window.geometry("600x360")
    window.resizable(False,False)     # disables maximizing option
    # Background picture
    bg=PhotoImage(file="horrible bg.png")
    # label
    label = Label(window, image=bg,bg='sky blue')
    label.place(x=0, y=0, relwidth=1, relheight=1)

    heading = Label(window, text='  ULTIMATE \n   HANGMAN  ', bg='sky blue',fg='black', font=('Constantia bold', 40))
    heading.place(relx=0.79, rely=0.29, anchor='ne')
    caption=Label(window,text='- Alert , He  Hangs  You !!',bg='grey11',fg='white',font=('Constantia',13))
    caption.place(relx=0.71, rely=0.79, anchor='ne')
    
    # button which starts the game
    run = True

    def start():
        global run
        answer = messagebox.askyesno('Hangman','ARE YOU READY..??')
        if answer is True:
            run = False
            window.destroy()
            game_levels()
    start_img = PhotoImage(file="play-btn-2-modified.png")
    start_btn = Button(window, command=lambda: start(),image=start_img,bg='royal blue')
    start_btn.place(relx=0.96, rely=0.78, anchor='ne')

    # button to exit from the game

    def exit():
        global run
        answer = messagebox.askyesno('Exit', 'REALLY ??\nDO YOU WANT TO EXIT THE GAME ?')
        if answer is True:
            run = False
            window.destroy()
    exit_img = PhotoImage(file="9exit.png")
    exit_btn = Button(window, bd=0, bg='grey12', command=lambda: exit(), font=10, image=exit_img)
    exit_btn.place(relx=0.14, rely=0.86, anchor='ne')

    def hangman_rules():
        messagebox.showinfo('HANGMAN', 'HELP...!!')
        window.destroy()
        rules()
        hangman_game()
    rules_img = PhotoImage(file="rules.png")
    rules_btn = Button(window, bd=0, bg='grey12', command=lambda: hangman_rules(), font=10,image=rules_img)
    rules_btn.place(relx=0.96, rely=0.06, anchor='ne')

    # define a music_button func for music:
    def music_but():
        def on():
            music_play()
            tog.configure(file="music_on btn.png")
            tog_button.configure(command=off)

        def off():
            music_of()
            tog.configure(file="music_off btn.png")
            tog_button.configure(command=on)

        tog = PhotoImage(file='music_off btn.png')
        tog_button = Button(image=tog, command=on)
        tog_button.place(x=25, y=25)

    # calling music func:
    music_but()
    # runs tkinter eventloop
    window.mainloop()
hangman_game()

