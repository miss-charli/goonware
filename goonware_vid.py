import tkinter as tk
import random
import os
import cv2
import tkvideo

DEFAULT_VIDEO_DIRECTORY = "media/videos"

def player_video_path(videos):
    video_files = videos
    video_choice = random.randint(0, (len(video_files) - 1))
    # Load and display each image
    video_path = os.path.join(DEFAULT_VIDEO_DIRECTORY, video_files[video_choice])
    print(video_path)
    return video_path

def show_silent_popup_video(window, videos):

    #TODO: CREATE A POPUP THAT PLAYS A VIDEO FROM DIRECTORY media/videos
    popup = tk.Toplevel(window)

    def trapclose():
        print("Closing Video...")
        popup.destroy()
    popup.title("VIDEO Window")
    popup.geometry("200x200")
    label = tk.Label(popup)
    label.pack()
    video_path = player_video_path(videos)
    vid = cv2.VideoCapture(video_path)
    ##TODO Create a video player with sound
    if int(vid.get(cv2.CAP_PROP_FRAME_WIDTH)) > (popup.winfo_screenwidth() * 0.5) or int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT)) > (popup.winfo_screenheight() * 0.5):
        player = tkvideo.tkvideo(video_path,label, loop=1, size=(int(vid.get(cv2.CAP_PROP_FRAME_WIDTH) * 0.25),int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT) * 0.25)))
        popup.geometry(
            str(str(int(vid.get(cv2.CAP_PROP_FRAME_WIDTH) * 0.25 )) + "x" + str(int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT) * 0.25))))
    else:
        popup.geometry(
            str(str(int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))) + "x" + str(int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT)))))
        player = tkvideo.tkvideo(video_path, label, loop=1, size=(int(vid.get(cv2.CAP_PROP_FRAME_WIDTH)), int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))))
    player.play()
    popup.update()
    popup.protocol("WM_DELETE_WINDOW",trapclose)
    pass