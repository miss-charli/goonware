import tkinter as tk #GUI
import random #Randomization Library
import os #File system handling
import goonware_img #Image Popup Spawner
import goonware_vid #Video Popup Spawner
import goonware_aud #Audio Player Spawner
import goonware_settings_gui #Settings GUI Initilizer

##TODO AUDIO LIBRARY IMPORT

#General Settings
cooldownTime = 10000
images = [] # List to store the PhotoImage objects
videos = [] # List to store Videos
audios = [] # List to store audio files
max_image_count = 1
image_count = 0
max_video_count = 1
video_count = 0
max_audio_count = 1
audio_count = 0
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
    global video_count
    global image_count
    global audio_count
    global max_image_count
    global max_video_count
    global max_audio_count
    VideoQ = random.randint(0,100)
    ImageQ = random.randint(0, 100)
    AudioQ = random.randint(0, 100)
    if VideoQ < (video_chance * 100) and video_count < max_video_count:
        #Use audio enabled video player
        pass
    else:
        #Use silent mode video player
        goonware_vid.show_silent_popup_video(window=window,videos=videos,video_count=video_count)
        video_count += 1
        pass
    if ImageQ < (image_chance * 100) and image_count < max_image_count:
        goonware_img.show_popup_image(window=window,images=images,image_count=image_count)
    if AudioQ < (audio_chance * 100) and audio_count < max_audio_count:
        goonware_aud.show_popup_audio()
        pass

def update():
    #spawn new windows_locale
    random_choice()
    window.after(cooldownTime, update)

load_images()
load_videos()

window = tk.Tk()
window.title("Control Panel")

window.cooldownTime = cooldownTime
goonware_settings_gui.settings_widgets_init(window)

window.after(cooldownTime, update)
window.mainloop()
