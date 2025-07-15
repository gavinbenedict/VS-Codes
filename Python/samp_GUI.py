import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Tkinter setup — this should come BEFORE using ImageTk
root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg="#111")
root.config(cursor="none")  # Hide cursor

canvas = tk.Canvas(root, bg="#111", highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

# Download the image
url = "https://www.sony.co.in/image/83e724c6b5df327fc96f9c05d3ccc2ce?fmt=jpeg&wid=1200&qlt=43"
response = requests.get(url)
img_data = response.content

# Process image using PIL (after root is created)
img = Image.open(BytesIO(img_data))
img = img.resize((100, 100))
img = ImageTk.PhotoImage(img)  # Now it's safe to use

# Add image to canvas
image_id = canvas.create_image(0, 0, anchor=tk.NW, image=img)

# Update image position with mouse movement
def follow_cursor(event):
    canvas.coords(image_id, event.x, event.y)

canvas.bind("<Motion>", follow_cursor)

# Escape to quit
root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()
