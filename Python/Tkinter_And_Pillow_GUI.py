from tkinter import Tk, Label, Button
from PIL import Image, ImageTk

# Create the main window
window = Tk()
window.title("Image Viewer")
window.geometry("1920x1080")  # Optional: Adjust window size

# Load the image using Pillow
image = Image.open("pho.jpg")  # 🔁 Replace with your image file
photo = ImageTk.PhotoImage(image)

# Display the image in the window
image_label = Label(window, image=photo)
image_label.pack(pady=20)

# Add a button to close the window
close_button = Button(window, text="Close Window", command=window.destroy)
close_button.pack(pady=10)

# Start the GUI event loop
window.mainloop()
