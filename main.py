from tkinter import *
import tkinter.messagebox
from tkinter import filedialog as fd
from pygame import mixer
import os

bg_color = "#313244"
window = Tk()
window.geometry("400x400")
window.title("Music :3")
#window.iconbitmap("images/wedonthaveiconsyetXD")
window.configure(background = bg_color)


mixer.init()
def open_window():
    filename = fd.askopenfilename()
    mixer.music.load(filename)
    mixer.music.set_volume(0.3)
    mixer.music.play()
small_button = tkinter.Button(
    text="Open File", 
    font=("Arial", 10),  
    padx=0.5,         
    pady=2,             
    command=open_window,
    
)

small_button.pack(anchor=NW)
window.mainloop()

#things ill need later for this/will implement once i get the buttons working/in there, compiled here so that i dont have to spend hours looking at docs every time i need to figure something like this out
#pygame.mixer.pause() self explanatory
#pygame.mixer.unpause() same as above
#pygame.mixer.fadeout(time) oooh, fancy stopping! ill make this an optional thingy with a little settings checkbox. maybe also to switch between songs once theyre in the last few seconds...?
