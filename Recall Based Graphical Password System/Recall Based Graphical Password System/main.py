from tkinter import  *
import tkinter as tk
import threading
import imageio
import sqlite3
import cv2
from ffpyplayer.player import MediaPlayer
from PIL import Image, ImageTk
from tkinter import messagebox


# Path to the video file
video_name = "images/bgvd.mkv"

# Create the main window
root = tk.Tk()
root.title("Final Year Project")

# Use imageio to read the video file
video = imageio.get_reader(video_name)
meta_data = video.get_meta_data()
width, height = meta_data['size']

# Set the window size to match the video
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

# Create a canvas widget to display the video
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack(fill="both", expand=True)

def stream():
    try:
        for image in video.iter_data():
            # Convert frame to an image and display it on the canvas
            frame_image = ImageTk.PhotoImage(Image.fromarray(image))
            canvas.create_image(0, 0, anchor=tk.NW, image=frame_image)
            canvas.image = frame_image
            # Delay for frame rate control
            canvas.update_idletasks()
            canvas.update()
            # Control the frame rate
            root.after(int(1000 / meta_data['fps']))
    except RuntimeError:
        # Catch the runtime error when the window is closed
        pass

# Create and start the thread for the video stream
thread = threading.Thread(target=stream)
thread.daemon = True  # Ensure the thread will close when the main window is closed
thread.start()

def oreg():
    root.destroy()
    import register
def olog():
    root.destroy()
    import login
image = Image.open("images/kp.png")
resize_image = image.resize((300, 70))
left2 = ImageTk.PhotoImage(resize_image)

#Let us create a label for button event
img_label= Label(image=left2)
#Let us create a dummy button and pass the image


button= Button(root, image=left2,command=oreg,
borderwidth=0)
button.place(x=800,y=300)

#login
image2 = Image.open("images/kpr.png")
resize_image2 = image2.resize((300, 70))
left3 = ImageTk.PhotoImage(resize_image2)

#Let us create a label for button event
img_label2= Label(image=left3)
#Let us create a dummy button and pass the image
button2= Button(root, image=left3,command=olog,
borderwidth=0)
button2.place(x=500,y=300)


# Start the Tkinter event loop
root.mainloop()
