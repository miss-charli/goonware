import random
import tkinter as tk
from tkinter import *
import os
from PIL import Image, ImageTk

#Runs without sounds (Silent Mode?)
import tkvideo

##TODO AUDIO LIBRARY IMPORT

#General Settings
cooldownTime = 1000
images = []  # List to store the PhotoImage objects
loaded_images = []
default_media_directory = "media/pics"
silent_mode = False

#Chances
image_chance = 0.5
video_chance = 0.5
audio_chance = 0.5

def load_images():
    global images
    images = [f for f in os.listdir(default_media_directory) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

# Function to load and display images
def canvas_load_images(canvas):
    # Clear the canvas
    canvas.delete("all")

    global images

    image_files = images

    image_choice = random.randint(0, (len(image_files)-1))
    # Load and display each image
    image_path = os.path.join(default_media_directory, image_files[image_choice])
    print(image_path)

    # Load the image using PIL
    img = Image.open(image_path)

    # Resize the image to fit the canvas
    #
    if img.width > 400 or img.height > 400:
        img = img.resize((int(img.width * 0.2), int(img.height * 0.2)))
        canvas.config(width=img.width, height=img.height)
    else:
        canvas.config(width=img.width, height=img.height)

    # Convert the PIL image to a Tkinter image
    tk_img = ImageTk.PhotoImage(img)

    loaded_images.append(tk_img)

    # Display the image on the canvas
    image_item = canvas.create_image(0, 10, anchor=tk.W, image=tk_img)
    canvas.tag_bind(
        image_item,
        '<Button-2>',
        lambda e: canvas.delete(image_item)
    )

    print(int(canvas["width"]) // 2)
    print(int(canvas["height"]) // 2)

    canvas.coords(image_item, 0, int(canvas["height"]) // 2)


def random_choice():
    VideoQ = random.randint(0,100)
    ImageQ = random.randint(0, 100)
    AudioQ = random.randint(0, 100)
    if VideoQ < (video_chance * 100) and silent_mode==False:
        #Use audio enabled video player
        pass
    else:
        #Use silent mode video player
        pass
    if ImageQ < (image_chance * 100):
        show_popup_image()
    if AudioQ < (audio_chance * 100) and silent_mode==False:
        pass


def show_popup_image():
    popup = tk.Toplevel(window)
    popup.title("Popup Window")
    popup.geometry("200x200")

    canvas = tk.Canvas(popup)

    canvas.pack(anchor="center", padx=0, pady=0)
    canvas_load_images(canvas)


    popup.update()
    popup.geometry(str(str(canvas["width"]) + "x" + str(canvas["height"])))
    print(canvas["width"], canvas["height"])

def show_popup_video():
    #TODO: CREATE A POPUP THAT PLAYS A VIDEO FROM DIRECTORY media/videos
    pass

def show_popup_audio():
    ##TODO: CREATE A POPUP THAT PLAYS AUDIO (MAY PUT THIS IN MAIN WINDOW AUDIO TRACK, TBD) FROM DIRECTORY MEDIA/SOUNDS
    pass

def update():
    #spawn new windows_locale"""
    random_choice()
    window.after(cooldownTime, update)

def cooldowntimeupdate(value):
    global cooldownTime
    cooldownTime = value
    print("cooldown time:", cooldownTime)

load_images()

window = tk.Tk()
window.title("Control Panel")

scaleLabel = tk.Label(window, text="Spawn Idle Time (Time in between spawning windows)", font=("Arial", 12))
scaleScale = tk.Scale(window, orient=tk.HORIZONTAL, from_=1000, to=100000, command=cooldowntimeupdate)
scaleScale.set(cooldownTime)
scaleLabel.pack(pady=20)
scaleScale.pack(pady=20)

window.after(cooldownTime, update)
window.mainloop()
