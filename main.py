import tkinter as tk #GUI
import random #Randomization Library
import os #File system handling
import goonware_img #Image Popup Spawner
import goonware_vid #Video Popup Spawner
import goonware_aud #Audio Player Spawner
import goonware_settings_gui #Settings GUI Initilizer

##TODO AUDIO LIBRARY IMPORT

#General Settings
cooldownTime = 100
images = [] # List to store the PhotoImage objects
videos = [] # List to store Videos
audios = [] # List to store audio files
image_popup = [] #Stores the image popups (Important for popup image window max)
video_popup = [] #Stores the video popups (Important for popup video window max)
max_image_count = 1
max_video_count = 1
max_audio_count = 1
audio_count = 0
silent_mode = True

#Chances
image_chance = 0.5
video_chance = 0.5
audio_chance = 0.0

def check_for_closures():
    for index in range(len(image_popup)):
        pass
        print(image_popup[index])
        #print(tk.Canvas)
        if image_popup[index].children == {}:
            image_popup.remove(image_popup[index])
            break
    for index in range(len(video_popup)):
        pass
        print(video_popup[index])
        #print(tk.Canvas)
        if video_popup[index].children == {}:
            video_popup.remove(video_popup[index])
            break


def load_images():
    global images
    images = [f for f in os.listdir(goonware_img.DEFAULT_PICTURE_DIRECTORY) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

def load_videos():
    global videos
    videos = [f for f in os.listdir(goonware_vid.DEFAULT_VIDEO_DIRECTORY) if f.endswith(('.mp4', '.mov', '.avi'))]

def random_choice():
    check_for_closures()
    global video_count
    global audio_count
    global max_image_count
    global max_video_count
    global max_audio_count
    VideoQ = random.randint(0,100)
    ImageQ = random.randint(0, 100)
    AudioQ = random.randint(0, 100)
    if VideoQ < (video_chance * 100) and len(video_popup) < max_video_count:
        video_popup.append(goonware_vid.show_silent_popup_video(window=window,videos=videos))
    if ImageQ < (image_chance * 100) and len(image_popup) < max_image_count:
        image_popup.append(goonware_img.show_popup_image(window,images))
    if AudioQ < (audio_chance * 100) and audio_count < max_audio_count:
        goonware_aud.show_popup_audio()
        pass
    #print(" IMAGE COUNT: " + str(image_count))

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
