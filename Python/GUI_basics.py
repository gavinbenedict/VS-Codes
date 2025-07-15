import tkinter as tk

# Create main window
s = tk.Tk()
s.title("test run")
s.geometry("640x480")

# Add a label
label = tk.Label(s, text="Hello, Tkinter!")
label.pack()

# Run the app
s.mainloop()
