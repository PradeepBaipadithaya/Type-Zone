
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title ('iMedic')

photo = tk.PhotoImage(file = "Dark_theme_logo_c.png")

frame = ttk.Frame(root, relief = tk.RAISED)
frame.grid(row = 0, column = 0, sticky = tk.NSEW)
label = tk.Label(
    frame, image=photo, compound = tk.CENTER,
    font = "Helvetica 40 bold",
    foreground = "yellow", text = "Welcome")
label.grid(row = 0, column = 0, sticky = tk.NSEW)

root.mainloop()
