#this code follows only a little bit of logic because who needs readability
#Real programmers just do random shit, add almost no helpful notes, forget their code exists for like a year and then improvise even more random stuff to figure out what the hell any of their magic runes mean.
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
from PIL import Image
import random

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
shufflebutton= PhotoImage(file="images/shuffle.png")
bigshuffle = shufflebutton.zoom(3)
ghost= PhotoImage (file="images/ghostnomusic.png")
ghost_bigger = ghost.zoom(5)
current_saved_volume = 30
songlength= 0
playlist = []
paused = False
songname = "Nothing rn"
progress= 0 # to show position later if i have time to implement that
fontcolorset= tkinter.StringVar()
bgcolorset = tkinter.StringVar()
accentcolorset = tkinter.StringVar()
queueueueueue = 0 #and the worst word in the english language goes tooooo.... whatever this bullshittery is. Only way to make queue acceptable to use is by adding progressively more ue to it. Trust.
songs_in_queueueueuuuuuuuuu = [None] * 100
add_song_here_in_queueuue_ueueu_euue = 0
running= True
songhasbeenplayed =False
themes= ["catppuccin mocha", "dracula", "hacker", "halloween"]
selected_theme = StringVar(value="None")
frames = 13
gifframes = []
loop = None
script_dir = Path(__file__).resolve().parent
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
    global bg_color, font_color, accent_color1, current_saved_volume, gifframes
    file = open("save.txt","r")
    file_list = eval(file.read())
    file.close()
    bg_color, font_color, current_saved_volume, accent_color1= file_list
    window.configure(background=bg_color) 
    menuframe.configure(background=bg_color)
    mainframe.configure(background=bg_color)
    nowplaying.configure(background=bg_color)
    small_button.configure(background=bg_color, activebackground=bg_color)
    settings_button.configure(background=bg_color, activebackground=bg_color)
    queue_button.configure(background=bg_color, activebackground=bg_color)
    lowerframe.configure(background=bg_color)
    nowplaying.configure(foreground=font_color, activeforeground=accent_color1)
    small_button.configure(foreground=font_color, activeforeground=accent_color1)
    settings_button.configure(foreground=font_color, activeforeground=accent_color1)
    queue_button.configure(foreground=font_color, activeforeground=accent_color1)
    folder_button.configure(foreground=font_color, activeforeground=accent_color1)
    folder_button.configure(background=bg_color, activebackground=bg_color)
    window.after(1000, musicqueueue) 
    for i in range(frames):
        obj = tkinter.PhotoImage(file = "images/ghostmusict.gif", format = f"gif -index {i}")
        bigger_obj = obj.zoom(5)
        gifframes.append(bigger_obj)
 

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
    global queueueueueue, songname, songhasbeenplayed, filename, add_song_here_in_queueuue_ueueu_euue, paused
    if not mixer.music.get_busy() and queueueueueue >=2 and songhasbeenplayed and not paused:
       
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
       add_song_here_in_queueuue_ueueu_euue-=1
       window.update()
    if songs_in_queueueueuuuuuuuuu[0]==None and queueueueueue >=2:
        songs_in_queueueueuuuuuuuuu.pop(0)
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
    animation()
    update_progress_bar()


def pause():
    global paused, notjustpaused
    mixer.music.pause()
    paused = True
    stop_animation()


def skip_back():
    global position, songhasbeenplayed
    mixer.music.rewind()
    position = 0
    print (position) 
    progressbar.set(position)
    mixer.music.play()
    songhasbeenplayed = False


def skip_ahead():
    global position, songhasbeenplayed
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
    file.write(str([bg_color,font_color, current_saved_volume, accent_color1]))
    file.close()


def open_settings():
    global themes, selected_theme
    settings_win = tkinter.Toplevel(
        bg= bg_color,)
    settings_win.title("Settings")
    settings_win.geometry("290x500")
    
    canvas = Canvas(settings_win, background= accent_color1)
    scrollbar = Scrollbar(settings_win, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    canvas.pack(anchor=CENTER, fill=BOTH, expand=True)
    settings_frame = Frame(
    canvas,
    bg=bg_color,
    pady=15,
    padx=15
    )
    

    canvas.configure(yscrollcommand=scrollbar.set)
    

    canvas.create_window((0, 0), window=settings_frame, anchor="nw")
    settings_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    
    idk = tkinter.Label(settings_frame, text="Volume", font=("Arial", 12), fg=font_color, bg= bg_color)
    idk.pack(pady=10)

    volume = Scale(settings_frame, from_ = 0, to = 100, orient=HORIZONTAL, bg = bg_color,
               command = set_volume, fg=font_color)
    volume.pack(pady=15)
    volume.set(current_saved_volume)
    mixer.music.set_volume(current_saved_volume)
    heading1= tkinter.Label(
        settings_frame, text="Themes", font=("Arial", 18), fg=font_color, bg= bg_color
    )
    heading1.pack(pady=15)
    OptionMenu(settings_frame, selected_theme, *themes).pack(pady=10)
    submit4 = tkinter.Button(
        settings_frame,
        text="Update Settings",   
        padx=0.5,         
        pady=2,             
        command=set_theme)
    submit4.pack(pady=5)
    heading2= tkinter.Label(
        settings_frame, text="Custom", font=("Arial", 18), fg=font_color, bg= bg_color
    )
    heading2.pack(pady=15)
    idk2 = tkinter.Label(settings_frame, text="Backgroundcolor (Enter Hexcode)", font=("Arial", 12), fg=font_color, bg= bg_color)
    idk2.pack(pady=10)
    bgentry = tkinter.Entry(settings_frame, textvariable=bgcolorset)
    bgentry.pack(pady=15)
    submit1 = tkinter.Button(
    settings_frame,
    text="Update Settings",   
    padx=0.5,         
    pady=2,             
    command=updatebgcolor,)
    submit1.pack(pady=5)
    idk3 = tkinter.Label(settings_frame, text="Fontcolor (Enter Hexcode)", font=("Arial", 12), fg=font_color, bg= bg_color)
    idk3.pack(pady=10)
    fontcolorentry = tkinter.Entry(settings_frame, textvariable=fontcolorset)
    fontcolorentry.pack(pady=15)
    submit2 = tkinter.Button(
    settings_frame,
    text="Update Settings",   
    padx=0.5,         
    pady=2,             
    command=updatefontcolor)
    submit2.pack(pady=5)

    idk4 = tkinter.Label(settings_frame, text="Accentcolor (Enter Hexcode)", font=("Arial", 12), fg=font_color, bg= bg_color)
    idk4.pack(pady=10)
    accentcolorentry = tkinter.Entry(settings_frame, textvariable=accentcolorset)
    accentcolorentry.pack(pady=15)
    submit3 = tkinter.Button(
    settings_frame,
    text="Update Settings",   
    padx=0.5,         
    pady=2,             
    command=updateaccentcolor)
    submit3.pack(pady=5)


def updatebgcolor():
    global bg_color
    bg_color = bgcolorset.get()
    print(bg_color)
    window.configure(background=bg_color) 
    menuframe.configure(background=bg_color)
    mainframe.configure(background=bg_color)
    nowplaying.configure(background=bg_color)
    lowerframe.configure(background=bg_color)
    folder_button.configure(background=bg_color, activebackground=bg_color)
    small_button.configure(background=bg_color, activebackground=bg_color)
    settings_button.configure(background=bg_color, activebackground=bg_color)
    queue_button.configure(background=bg_color, activebackground=bg_color)
    file = open("save.txt","w")
    file.write(str([bg_color,font_color, current_saved_volume, accent_color1]))
    file.close()
    

def updatefontcolor():
    global font_color
    font_color = fontcolorset.get()
    print(font_color)
    nowplaying.configure(foreground=font_color)
    small_button.configure(foreground=font_color)
    settings_button.configure(foreground=font_color)
    queue_button.configure(foreground=font_color)
    folder_button.configure(foreground=font_color)
    file = open("save.txt","w")
    file.write(str([bg_color,font_color, current_saved_volume, accent_color1]))
    file.close()


def updateaccentcolor():
    global accent_color1
    accent_color1 = accentcolorset.get()
    print(accent_color1)
    nowplaying.configure(activeforeground=accent_color1)
    small_button.configure(activeforeground=accent_color1)
    settings_button.configure(activeforeground=accent_color1)
    queue_button.configure(activeforeground=accent_color1)
    folder_button.configure(activeforeground=accent_color1)
    file = open("save.txt","w")
    file.write(str([bg_color,font_color, current_saved_volume, accent_color1]))
    file.close()


def set_theme():
    global bg_color, font_color, accent_color1, selected_theme
    temptheme= selected_theme.get()
    if temptheme== "catppuccin mocha":
        bg_color= "#1e1e2e"
        accent_color1= "#cba6f7"
        font_color = "#cdd6f4"
    if temptheme== "hacker":
        bg_color= "black"
        accent_color1= "#a6d189"
        font_color = "green"
    if temptheme== "halloween":
        bg_color= "#FF7600"
        accent_color1= "#CD113B"
        font_color = "#52006A"
    if temptheme== "dracula":
        bg_color= "#282A36"
        accent_color1= "#FF5555"
        font_color = "#F8F8F2"
    nowplaying.configure(activeforeground=accent_color1)
    small_button.configure(activeforeground=accent_color1)
    settings_button.configure(activeforeground=accent_color1)
    queue_button.configure(activeforeground=accent_color1)
    folder_button.configure(activeforeground=accent_color1)
    nowplaying.configure(foreground=font_color)
    small_button.configure(foreground=font_color)
    settings_button.configure(foreground=font_color)
    queue_button.configure(foreground=font_color)
    folder_button.configure(foreground=font_color)
    window.configure(background=bg_color) 
    menuframe.configure(background=bg_color)
    mainframe.configure(background=bg_color)
    nowplaying.configure(background=bg_color)
    lowerframe.configure(background=bg_color)
    folder_button.configure(background=bg_color, activebackground=bg_color)
    small_button.configure(background=bg_color, activebackground=bg_color)
    settings_button.configure(background=bg_color, activebackground=bg_color)
    queue_button.configure(background=bg_color, activebackground=bg_color)
    file = open("save.txt","w")
    file.write(str([bg_color,font_color, current_saved_volume, accent_color1]))
    file.close()    
    

def show_queueueueueueue():
    global songs_in_queueueueuuuuuuuuu
    songs = [song for song in songs_in_queueueueuuuuuuuuu if song is not None]
    list_variable = tkinter.Variable(value=songs)
    x= 0
    for i in range(100):
        if songs_in_queueueueuuuuuuuuu[x] == None:
            x = 0
            break
        else:
            print(os.path.basename(songs_in_queueueueuuuuuuuuu[x]))
            x+= 1
    
    queue_win = tkinter.Toplevel(
        bg= bg_color,)
    queue_win.title("Queue")
    queue_win.geometry("250x250")
    queue_display= tkinter.Listbox(queue_win, listvariable=list_variable, height= 200, width=200)
    queue_display.pack(padx=10, pady=10)
    


def open_folder():
    global songhasbeenplayed, add_song_here_in_queueuue_ueueu_euue, songs_in_queueueueuuuuuuuuu, current_saved_volume, filename, queueueueueue, songname, songlength
    
    folder_path = fd.askdirectory(title="Select a Folder")
    folder_contents = os.listdir(folder_path)
    if queueueueueue == 0:
        songname =os.path.basename(folder_contents[0])
        filename = os.path.join(folder_path, songname)
        mixer.music.load(filename)
        mixer.music.set_volume(current_saved_volume)
        music= mixer.Sound(filename)
        songlength= music.get_length()
        print(songlength)
        progressbar.config(to=songlength)
        nowplaying.config(text = songname)
        window.update() 
        queueueueueue +=2
        songhasbeenplayed=False
        for i in folder_contents[1:]:
            songs_in_queueueueuuuuuuuuu[add_song_here_in_queueuue_ueueu_euue] = os.path.join(folder_path, i)
            add_song_here_in_queueuue_ueueu_euue +=1
            queueueueueue +=1
            
    else:
        for i in folder_contents:
            songs_in_queueueueuuuuuuuuu[add_song_here_in_queueuue_ueueu_euue] = os.path.join(folder_path, i)
            add_song_here_in_queueuue_ueueu_euue +=1
            print(songs_in_queueueueuuuuuuuuu[0])
            queueueueueue +=1


def shuffle():
    global songs_in_queueueueuuuuuuuuu
    random.shuffle(songs_in_queueueueuuuuuuuuu)


def animation(current_frame=0):
    global loop
    
    image = gifframes[current_frame]
    companion.configure(image = image)
    current_frame = current_frame + 1
    loop = window.after(120, lambda: animation(current_frame))
    if current_frame == frames:
        current_frame = 0 


def stop_animation():
    window.after_cancel(loop)

    




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
small_button.pack(side= LEFT, padx=20)    


folder_button = tkinter.Button(
    menuframe,
    text="Open Folder", 
    font=("Arial", 10),  
    padx=0.5,         
    pady=2,             
    command=open_folder,
    bg= bg_color,
    bd= 0,
    highlightthickness=0,
    fg= font_color,
    activebackground= bg_color,
    
    activeforeground= accent_color1)
folder_button.pack(side= LEFT, padx=20)    


queue_button = tkinter.Button(
    menuframe,
    text="Print Queue", 
    font=("Arial", 10),  
    padx=0.5,         
    pady=2,             
    command=show_queueueueueueue,
    bg= bg_color,
    bd= 0,
    highlightthickness=0,
    fg= font_color,
    activebackground= bg_color,
    
    activeforeground= accent_color1)
queue_button.pack(side= LEFT, padx=20)  


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
settings_button.pack(side= RIGHT, padx=20)

companion = tkinter.Label(mainframe, image=ghost_bigger)
companion.pack(anchor=S, pady=5)

nowplaying= tkinter.Label(mainframe, text = "Nothing rn", font=(12), fg=font_color, bg=bg_color)
nowplaying.pack(anchor=N)


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
skip2_button.pack(side=LEFT, padx=3)


shuffle_button = tkinter.Button(
    mainframe,
    image= bigshuffle,
    width=50, 
    height=50,
    padx=2,         
    pady=2,             
    command=shuffle,
)
shuffle_button.pack(side=RIGHT, padx=3)







#running init + the main window
initstuff()
window.mainloop()

#things ill need later for this/will implement once i get the buttons working/in there, compiled here so that i dont have to spend hours looking at docs every time i need to figure something like this out

#pygame.mixer.fadeout(time) oooh, fancy stopping! ill make this an optional thingy with a little settings checkbox. maybe also to switch between songs once theyre in the last few seconds...?
