from tkinter import Tk, Canvas
from PIL import Image, ImageTk
import os

# Initialize the main window
root = Tk()
root.title("Interactive Image Canvas")

# Create a canvas
canvas = Canvas(root, width=800, height=600, bg="white")
canvas.pack()

# Load an image
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
image_path = os.path.join(desktop, "#pixil-frame-0.png")
try:
    img = Image.open(image_path)
    img = img.resize((200, 200))  # Resize if needed
    photo = ImageTk.PhotoImage(img)

# Run the tkinter event loop
root.mainloop()
