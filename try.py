
import tkinter as tk
from tkinter import Toplevel, ttk
from tkinter import Canvas
from PIL import Image, ImageTk
root = tk.Tk()

result_window = Toplevel()
result_window.title("Yay!")
result_window.geometry("370x450")
result_window.config(background="#3C3F41")

bg_image = tk.PhotoImage(file="Result_Images/1.png")

my_canvas = Canvas(result_window,width=370,height=450)
my_canvas.pack(fill="both",expand=True)

my_canvas.create_image(0,0,image = bg_image,anchor="nw")

root.mainloop()
