from tkinter import *
import tkinter.messagebox
from tkinter import filedialog as fd
from pygame import mixer
import os

bg_color = "#313244"
window = Tk()
window.geometry("400x400")
window.title("Music :3")
icon_image = tkinter.PhotoImage(file="images/icon.png")
window.iconphoto(False, icon_image)
window.configure(background = bg_color)


mixer.init()
mainframe = Frame (
height= 200,
width= 300
)
mainframe.place(relx=0.5, rely=0.5, anchor=CENTER)
def open_window():
    filename = fd.askopenfilename()
    mixer.music.load(filename)
    mixer.music.set_volume(0.3)
    
def play():
    mixer.music.play()
def pause():
    mixer.music.pause()
small_button = tkinter.Button(
    text="Open File", 
    font=("Arial", 10),  
    padx=0.5,         
    pady=2,             
    command=open_window,
    
)

small_button.pack(anchor=NW)
play_button = tkinter.Button(
    mainframe,
    text="Play", 
    font=("Arial", 10),  
    padx=2,         
    pady=2,             
    command=play,
    
)
play_button.pack(side=LEFT, padx=2)

pause_button = tkinter.Button(
    mainframe,
    text="Pause", 
    font=("Arial", 10),  
    padx=2,         
    pady=2,             
    command=pause,
    
)
pause_button.pack(side=RIGHT, padx=2)


window.mainloop()

#things ill need later for this/will implement once i get the buttons working/in there, compiled here so that i dont have to spend hours looking at docs every time i need to figure something like this out
#pygame.mixer.pause() self explanatory
#pygame.mixer.unpause() same as above
#pygame.mixer.fadeout(time) oooh, fancy stopping! ill make this an optional thingy with a little settings checkbox. maybe also to switch between songs once theyre in the last few seconds...?
