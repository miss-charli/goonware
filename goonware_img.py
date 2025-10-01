import tkinter as tk #GUI
import random #Randomization Library
import os #File system handling
from PIL import Image, ImageTk

DEFAULT_PICTURE_DIRECTORY = "media/pics"
loaded_images = []

# Function to load and display images
def canvas_load_images(canvas, images):
    # Clear the canvas
    canvas.delete("all")

    image_files = images

    image_choice = random.randint(0, (len(image_files)-1))

    # Load and display each image
    image_path = os.path.join(DEFAULT_PICTURE_DIRECTORY, image_files[image_choice])
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

def show_popup_image(window,images, image_count):
    popup = tk.Toplevel(window)

    def trapclose():
        global image_count
        print("Closing Image...")
        popup.destroy()
        image_count -= 1

    popup.title("IMAGE Window")
    popup.geometry("200x200")

    canvas = tk.Canvas(popup)

    canvas.pack(anchor="center", padx=0, pady=0)
    canvas_load_images(canvas, images)

    popup.update()

    popup.protocol("WM_DELETE_WINDOW", trapclose)

    popup.geometry(str(str(canvas["width"]) + "x" + str(canvas["height"])))
    print(canvas["width"], canvas["height"])