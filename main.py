#this code follows no logic because who needs readability
#Real programmers just do random shit, add no helpful notes, forget their code exists for like a year and then improvise even more random stuff to figure out what the hell any of their magic runes mean.
# have i mentioned that im also deeply unfunny?
#you WILL get eyecancer from my notes/sense of "humor"
# :D



#this could have been a multiline comment instead of multiple one line ones actually. I may be incompetent

#imports
from tkinter import *
from pathlib import Path
import tkinter.messagebox
from tkinter import filedialog as fd
from pygame import mixer
import os
import time

#assigning things/base values of stuff (obviously)
bg_color = "#313244"
font_color= "#cdd6f4"
accent_color1= "#cba6f7"
window = Tk()
window.geometry("400x400")
window.title("Music :3")
icon_image = tkinter.PhotoImage(file="images/icon.png")
window.iconphoto(False, icon_image)
window.configure(background = bg_color)
playbutton= PhotoImage(file="images/pause.png")
bigplaybutton= playbutton.zoom(3)
pausebutton= PhotoImage(file="images/play.png")
bigpausebutton= pausebutton.zoom(3)
skip1button= PhotoImage(file="images/skip1.png")
bigskip1button = skip1button.zoom(3)
skip2button= PhotoImage(file="images/skip2.png")
bigskip2button = skip2button.zoom(3)
current_saved_volume = 30
songlength= 0
playlist = []
paused = False
songname = "Nothing rn"
progress= 0 # to show position later if i have time to implement that
fontcolorset= tkinter.StringVar()
bgcolorset = tkinter.StringVar()
queueueueueue = 0 #and the worst word in the english language goes tooooo.... whatever this bullshittery is. Only way to make queue acceptable to use is by adding progressively more ue to it. Trust.
songs_in_queueueueuuuuuuuuu = [None] * 100
add_song_here_in_queueuue_ueueu_euue = 0
running= True
songhasbeenplayed =False
mixer.init()
mainframe = Frame (
    bg= bg_color
)
menuframe = Frame (
    bg = bg_color
)
menuframe.place(relx=0.5,anchor=N)
mainframe.place(relx=0.5, rely=0.5, anchor=CENTER)
lowerframe = Frame (
    bg = bg_color
)
lowerframe.place(relx=0.5, rely=0.3 , anchor=S)






#functions
def initstuff():
    global bg_color, font_color
    file = open("save.txt","r")
    file_list = eval(file.read())
    file.close()
    bg_color, font_color, current_saved_volume= file_list
    window.configure(background=bg_color) 
    menuframe.configure(background=bg_color)
    mainframe.configure(background=bg_color)
    nowplaying.configure(background=bg_color)
    small_button.configure(background=bg_color, activebackground=bg_color)
    lowerframe.configure(background=bg_color)
    settings_button.configure(background=bg_color, activebackground=bg_color)
    nowplaying.configure(foreground=font_color)
    small_button.configure(foreground=font_color)
    settings_button.configure(foreground=font_color)
    window.after(1000, musicqueueue) 
 

def open_window():
    global songname, songlength, queueueueueue, add_song_here_in_queueuue_ueueu_euue, songs_in_queueueueuuuuuuuuu
    if queueueueueue == 0:
        filename = fd.askopenfilename()
        mixer.music.load(filename)
        mixer.music.set_volume(current_saved_volume)
        songname =os.path.basename(filename)
        music= mixer.Sound(filename)
        songlength= music.get_length()
        print(songlength)
        progressbar.config(to=songlength)
        nowplaying.config(text = songname)
        window.update() 
        queueueueueue +=2
    else:
        tempsavingfilename = fd.askopenfilename()
        songs_in_queueueueuuuuuuuuu[add_song_here_in_queueuue_ueueu_euue]= tempsavingfilename #my favorite line in this whole file :DD
        print(songs_in_queueueueuuuuuuuuu)
        add_song_here_in_queueuue_ueueu_euue +=1
        print (add_song_here_in_queueuue_ueueu_euue)
        queueueueueue +=1


def musicqueueue():
    global queueueueueue, songname, songhasbeenplayed, filename
    if not mixer.music.get_busy() and queueueueueue >=2 and songhasbeenplayed:
       
       filename= songs_in_queueueueuuuuuuuuu[0]
       mixer.music.load(filename)
       songname =os.path.basename(filename)
       music= mixer.Sound(filename)
       songlength= music.get_length()
       print(songlength)
       progressbar.config(to=songlength)
       queueueueueue -=1
       nowplaying.config(text = songname)
       songs_in_queueueueuuuuuuuuu.pop(0)
       print(songs_in_queueueueuuuuuuuuu)
       songhasbeenplayed= False
       mixer.music.play()
       window.update() 
    window.after(1000, musicqueueue)
    
   
def update_progress_bar():
    global paused
    if paused == False:
        position = mixer.music.get_pos() / 1000
        print (position) #
        progressbar.set(position)
        window.after(1000, update_progress_bar)
    
       
def play():
    global songname, paused, songhasbeenplayed
    if paused == False :
        mixer.music.play(),
        nowplaying.config(text = songname)
        window.update() 
        songhasbeenplayed = True
    else:
        mixer.music.unpause()
        paused = False
        songhasbeenplayed = True
    update_progress_bar()


def pause():
    global paused
    mixer.music.pause()
    paused = True


def skip_back():
    global position
    mixer.music.rewind()
    position = 0
    print (position) 
    progressbar.set(position)
    mixer.music.play()


def skip_ahead():
    global position
    mixer.music.stop()
    position = 0 
    print (position) 
    progressbar.set(position)
    

def set_volume(val):
    global current_saved_volume
    current_saved_volume = int(val)
    volume= float(val) / 100
    mixer.music.set_volume(volume)
    file = open("save.txt","w")
    file.write(str([bg_color,font_color, current_saved_volume]))
    file.close()


def open_settings():
    settings_win = tkinter.Toplevel(
        bg= bg_color,)
    settings_win.title("Settings")
    settings_win.geometry("250x400")

    idk = tkinter.Label(settings_win, text="Volume", font=("Arial", 12), fg=font_color, bg= bg_color)
    idk.pack(pady=10)

    volume = Scale(settings_win, from_ = 0, to = 100, orient=HORIZONTAL, bg = bg_color,
               command = set_volume, fg=font_color)
    volume.pack(pady=15)
    volume.set(current_saved_volume)
    mixer.music.set_volume(current_saved_volume)

    idk2 = tkinter.Label(settings_win, text="Backgroundcolor (Enter Hexcode)", font=("Arial", 12), fg=font_color, bg= bg_color)
    idk2.pack(pady=10)
    bgentry = tkinter.Entry(settings_win, textvariable=bgcolorset)
    bgentry.pack(pady=15)
    submit1 = tkinter.Button(
    settings_win,
    text="Update Settings",   
    padx=0.5,         
    pady=2,             
    command=updatebgcolor,)
    submit1.pack(pady=1)
    idk3 = tkinter.Label(settings_win, text="Fontcolor (Enter Hexcode)", font=("Arial", 12), fg=font_color, bg= bg_color)
    idk3.pack(pady=10)
    fontcolorentry = tkinter.Entry(settings_win, textvariable=fontcolorset)
    fontcolorentry.pack(pady=15)
    submit2 = tkinter.Button(
    settings_win,
    text="Update Settings",   
    padx=0.5,         
    pady=2,             
    command=updatefontcolor)
    submit2.pack(pady=1)


def updatebgcolor():
    global bg_color
    bg_color = bgcolorset.get()
    print(bg_color)
    window.configure(background=bg_color) 
    menuframe.configure(background=bg_color)
    mainframe.configure(background=bg_color)
    nowplaying.configure(background=bg_color)
    small_button.configure(background=bg_color)
    lowerframe.configure(background=bg_color)
    settings_button.configure(background=bg_color)
    file = open("save.txt","w")
    file.write(str([bg_color,font_color, current_saved_volume]))
    file.close()
    

def updatefontcolor():
    global font_color
    font_color = fontcolorset.get()
    print(font_color)

    nowplaying.configure(foreground=font_color)
    small_button.configure(foreground=font_color)
    
    settings_button.configure(foreground=font_color)
    file = open("save.txt","w")
    file.write(str([bg_color,font_color, current_saved_volume]))
    file.close()
    





#UI elements
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
    
    activeforeground= accent_color1)
small_button.pack(side= LEFT, padx=50)    


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
    activeforeground= accent_color1)
settings_button.pack(side= RIGHT, padx=50)


progressbar = tkinter.Scale (
    mainframe,
    from_=0,
    to= 100,
    orient= HORIZONTAL,
    showvalue=False,
    length= 200
)
progressbar.pack(anchor=N, pady=30)


skip1_button = tkinter.Button(
    mainframe,
    image= bigskip2button,
    width=50, 
    height=50,  
    padx=2,         
    pady=2,             
    command=skip_back,
    )
skip1_button.pack(side=LEFT, padx=3)


play_button = tkinter.Button(
    mainframe,
    image= bigplaybutton,
    width=50, 
    height=50,  
    padx=2,         
    pady=2,             
    command=play,
)
play_button.pack(side=LEFT, padx=3)


pause_button = tkinter.Button(
    mainframe,
    image= bigpausebutton,
    width=50, 
    height=50,
    padx=2,         
    pady=2,             
    command=pause,
)
pause_button.pack(side=LEFT, padx=3)


skip2_button = tkinter.Button(
    mainframe,
    image= bigskip1button,
    width=50, 
    height=50,
    padx=2,         
    pady=2,             
    command=skip_ahead,
)
skip2_button.pack(side=RIGHT, padx=3)


nowplaying= tkinter.Label(lowerframe, text = "Nothing rn", font=(12), fg=font_color, bg=bg_color)
nowplaying.pack(anchor=N)






#running init + the main window
initstuff()
window.mainloop()

#things ill need later for this/will implement once i get the buttons working/in there, compiled here so that i dont have to spend hours looking at docs every time i need to figure something like this out

#pygame.mixer.fadeout(time) oooh, fancy stopping! ill make this an optional thingy with a little settings checkbox. maybe also to switch between songs once theyre in the last few seconds...?
