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
font_color= "#cdd6f4"
accent_color1= "#cba6f7"

mixer.init()
mainframe = Frame (
    bg= bg_color
)
menuframe = Frame (
    bg = bg_color
)
menuframe.place(relx=0.5,anchor=N)
mainframe.place(relx=0.5, rely=0.5, anchor=CENTER)
def open_window():
    filename = fd.askopenfilename()
    mixer.music.load(filename)
    mixer.music.set_volume(0.3)
    
def play():
    mixer.music.play(),
    
def pause():
    mixer.music.pause()
small_button = tkinter.Button(
    menuframe,
    text="Open File", 
    font=("Arial", 10),  
    padx=0.5,         
    pady=2,             
    command=open_window,
    bg= bg_color,
    bd= 0,
    highlightthickness=0,
    fg= font_color,
    activebackground= bg_color,
    
    activeforeground= accent_color1
    
)

small_button.pack(side= LEFT, padx=50)
current_saved_volume = 30
def set_volume(val):
    global current_saved_volume
    current_saved_volume = int(val)
    volume= float(val) / 100
    mixer.music.set_volume(volume)
def open_settings():
    
    settings_win = tkinter.Toplevel(
        bg= bg_color,
    )
    settings_win.title("Settings")
    settings_win.geometry("250x150")
    idk = tkinter.Label(settings_win, text="Volume", font=("Arial", 12), fg=font_color, bg= bg_color)
    idk.pack(pady=10)
    volume = Scale(settings_win, from_ = 0, to = 100, orient=HORIZONTAL, bg = bg_color,
               command = set_volume, fg=font_color)
    volume.pack(pady=15)
    volume.set(current_saved_volume)
    mixer.music.set_volume(0.3)
    


settings_button = tkinter.Button(
    menuframe,
    text="Settings", 
    font=("Arial", 10),  
    padx=0.5,         
    pady=2,             
    command=open_settings,
    bg= bg_color,
    bd= 0,
    highlightthickness=0,
    fg= font_color,
    activebackground= bg_color,
    
    activeforeground= accent_color1
    
)

settings_button.pack(side= RIGHT, padx=50)

playbutton= PhotoImage(file="images/pause.png")
bigplaybutton= playbutton.zoom(3)
pausebutton= PhotoImage(file="images/play.png")
bigpausebutton= pausebutton.zoom(3)
play_button = tkinter.Button(
    mainframe,
    image= bigplaybutton,
    width=50, 
    height=50,  
    padx=2,         
    pady=2,             
    command=play,
    
)
play_button.pack(side=LEFT, padx=4)

pause_button = tkinter.Button(
    mainframe,
    image= bigpausebutton,
    width=50, 
    height=50,
    padx=2,         
    pady=2,             
    command=pause,
    
)
pause_button.pack(side=RIGHT, padx=4)


window.mainloop()

#things ill need later for this/will implement once i get the buttons working/in there, compiled here so that i dont have to spend hours looking at docs every time i need to figure something like this out
#pygame.mixer.pause() self explanatory
#pygame.mixer.unpause() same as above
#pygame.mixer.fadeout(time) oooh, fancy stopping! ill make this an optional thingy with a little settings checkbox. maybe also to switch between songs once theyre in the last few seconds...?
