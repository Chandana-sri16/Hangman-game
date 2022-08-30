# This module runs the complete hangman game...

import time
from string import ascii_uppercase
from tkinter import *
from tkinter import messagebox
import random
from pygame import mixer

def medium_level():
    # displays root window
    window = Tk()
    # window appearance settings
    window.title("Hangman version 6.4.2")
    window.geometry("800x500+120+100")
    window.resizable(False, False)
    label = Label(window, bg='pink')
    label.place(x=0, y=0, relwidth=1, relheight=1)

    img = PhotoImage(file="icon.png")
    window.iconphoto(False, img)

    l1 = Label(window, text='Hangman game', font=('Arial Black', 20), bg='pink')
    l1.place(relx=0.61, rely=0.02, anchor='ne')

# function to select theme
    x=[]
    def choice(value):
        global x
        selected_theme = options.get()                   # selected theme is stored here
        if selected_theme == 'Fruits':                   # if user option in fruits it will check this condition and run into the list
            x = ['GOOSEBERRY','BLACKBERRY','JACKFRUIT','TAMARIND','CUSTARDAPPLE','DRAGONFRUIT','MULBERRY','RASPBERRY','MUSKMELON','PEAR']
            newgame(x)
        if selected_theme == 'Animals':
            x = ['SQUIRREL','RACCOON','IGUANA','HAWK','EMU','KOALABEAR','OTTER','JACKAL']
            newgame(x)
        if selected_theme == 'Clothes':
            x = ['SKIRT','BIKINI','TOP','WINTERCOAT','HOODIE','COAT','SHORTS']
            newgame(x)
        if selected_theme == 'Colours':
            x = ['BLUSH','CRIMSON','AMBER','APRICOT','AQUAMARINE','BABY BLUE','BRONZE','ERIN','IVORY']
            newgame(x)
        if selected_theme == 'Body_Parts':
            x = ['MUSCLE','BONE','LUNG','KIDNEY','HEART','LIVER','MUSTACHE','BEARD','SKULL','EYEBROW']
            newgame(x)
        if selected_theme == 'Sports':
            x = ['SOCCER','BASKETBALL','TENNIS','BASEBALL','GOLF','RUNNING','VOLLEYBALL','BADMINTON','SWIMMING','BOXING','TABLETENNIS']
            newgame(x)
        if selected_theme == 'Relations':
            x = ['NEPHEW','STEPBROTHER','STEPFATHER','FRIEND']
            newgame(x)
        if selected_theme == 'Birds':
            x = ['CANARY','CORMORANT','HEN','CROW','CUCKOO','DOVE','OWL','PARROT','WOODPECKER','GOLDFINCH']
            newgame(x)
        if selected_theme == 'Things':
            x = ['CUPBOARD','PILLOW','COFFEEMAKER','BEDSPOON','BLANKET','KNIFE','STOVE','SINK','WASHINGMACHINE','POT',
               'FRIDGE','SOFA','STOOL','CUP','FORK','GLASS']
            newgame(x)
        if selected_theme == 'Musical_Instruments':
            x = ['GRANDPIANO','GUITAR','KEYBOARD','BASSDRUM', 'BASSGUITAR', 'CONGA', 'CORNET', 'DOUBLEBASS',
               'DRUMS', 'ELECTRICGUITAR', 'FLUTE', 'HARP']
            newgame(x)

    # creating option menu widget
    list1 = ["Fruits", "Animals", "Clothes", "Colours", "Body_Parts", "Sports", "Relations", "Birds", "Things", "Musical_Instruments"]
    options = StringVar(window)
    options.set('Themes')
    dropdown = OptionMenu(window, options, *list1,command=choice)
    # positioning widget
    dropdown.place(relx=0.9, rely=0.2, anchor='ne')
    dropdown.configure(bg='grey16',fg='white')
    lbl = Label(window, text='Click to select one among :', font=('Constantia bold', 13), bg='pink', fg='black')
    lbl.place(relx=0.95, rely=0.1, anchor='ne')

    # images of hangman
    photos = [PhotoImage(file="2hang.png"),PhotoImage(file="3hang.png"), PhotoImage(file="4hang.png"),
                  PhotoImage(file="5hang.png"), PhotoImage(file="6hang.png"),PhotoImage(file="7hang.png")]

    # function that makes the game to run again
    def newgame(x):
        global word_with_spaces
        global numberOfGuesses
        numberOfGuesses = 0
        img_lbl.config(image=photos[0])
        the_word = random.choice(x)
        word_with_spaces = " ".join(the_word)
        lblWord.set(" ".join("_" * len(the_word)))
        img_lbl.config(image=photos[6])
        newgame(x)

    def guess(letter):
        global numberOfGuesses
        if numberOfGuesses < 6:
            txt = list(word_with_spaces)
            guessed = list(lblWord.get())
            if word_with_spaces.count(letter) > 0:
                for r in range(len(txt)):
                    if txt[r] == letter:
                        guessed[r] = letter
                    lblWord.set("".join(guessed))
                    if lblWord.get()==word_with_spaces:
                        mixer.music.load('success-fanfare.mp3')     # plays a sound when man wins the game
                        mixer.music.play()
                # shows a messagebox on the panel
                        messagebox.showinfo("Hangman","Well Done🥳\nYou guessed it!")
                        choice(x)
            else:
                numberOfGuesses += 1
                img_lbl.config(image=photos[numberOfGuesses])
                mixer.music.load('sound-funny.mp3')                  # plays sound when the guess is wrong
                mixer.music.play()
                time.sleep(0.5)
                if numberOfGuesses == 5:
                    mixer.music.load('studio-roar.mp3')              # plays sound when the man is hanged
                    mixer.music.play()
                    txt =word_with_spaces
                    lblWord.set("".join(txt))
                # shows warning box when chances are over
                    messagebox.showwarning("Hangman", "Game Over😞")
                    choice(x)

    # label to display hangman images
    img_lbl= Label(window)
    img_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=40)

    # setting Variable
    lblWord = StringVar()
    Label(window, textvariable=lblWord, font='consoles 24 bold',bg='pink').grid(row=0, column=3, columnspan=6, padx=10)

    # onscreen Keyboard to give input
    n=0
    for r in ascii_uppercase:
        Button(window, text=r, command=lambda r=r: guess(r), font="helvetica 18", width=4,bg="black",fg="pink").grid(row=4+n//9,column=4+n % 9)
        n+=1
    # button to get new word
    Button(window, text="New\nWord", command=lambda: choice(x), font=("Helvetica 10 bold"), width=7,bg="black",fg="pink").grid(row=6, column=12)
    newgame(x)

    # function to exit the game
    run = True
    def close():
        global run
        answer = messagebox.askyesno('Exit', 'REALLY ??\nDO YOU WANT TO EXIT THE GAME?')
        if answer is True:
            run = False
            window.destroy()
    e1 = PhotoImage(file='9exit.png')
    ex = Button(window, bd=0, command=lambda: close(), bg='black', font=10, image=e1)
    ex.grid(row=7, column=12)

    # runs tkinter eventloop
    window.mainloop()
