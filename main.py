import tkinter as tk #GUI
import random #Randomization Library
import os #File system handling
import goonware_img #Image Popup Spawner
import goonware_vid #Video Popup Spawner
import goonware_aud #Audio Player Spawner

##TODO AUDIO LIBRARY IMPORT

#General Settings
cooldownTime = 1000
images = [] # List to store the PhotoImage objects
videos = [] # List to store Videos
default_videos_directory = "media/videos"
default_audios_directory = "media/audios"
silent_mode = True

#Chances
image_chance = 0.5
video_chance = 0.5
audio_chance = 0.0

def load_images():
    global images
    images = [f for f in os.listdir(goonware_img.DEFAULT_PICTURE_DIRECTORY) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

def load_videos():
    global videos
    videos = [f for f in os.listdir(default_videos_directory) if f.endswith(('.mp4', '.mov', '.avi'))]

def random_choice():
    VideoQ = random.randint(0,100)
    ImageQ = random.randint(0, 100)
    AudioQ = random.randint(0, 100)
    if VideoQ < (video_chance * 100) and silent_mode==False:
        #Use audio enabled video player
        pass
    else:
        #Use silent mode video player
        goonware_vid.show_silent_popup_video(window,videos)
        pass
    if ImageQ < (image_chance * 100):
        goonware_img.show_popup_image(window=window,images=images)
    if AudioQ < (audio_chance * 100) and silent_mode==False:
        goonware_aud.show_popup_audio()
        pass

def update():
    #spawn new windows_locale
    random_choice()
    window.after(cooldownTime, update)

def cooldownTimeupdate(value):
    global cooldownTime
    cooldownTime = value
    print("cooldown time:", cooldownTime)

load_images()
load_videos()

window = tk.Tk()
window.title("Control Panel")

scaleLabel = tk.Label(window, text="Spawn Idle Time (Time in between spawning windows)", font=("Arial", 12))
scaleScale = tk.Scale(window, orient="horizontal", from_=1000, to=100000, command=cooldownTimeupdate)
scaleScale.set(cooldownTime)
scaleLabel.pack(pady=20)
scaleScale.pack(pady=20)

window.after(cooldownTime, update)
window.mainloop()
