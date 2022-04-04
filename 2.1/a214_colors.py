import tkinter as tk

root = tk.Tk()
root.wm_geometry("500x500")

frame_blue = tk.Frame(root, background="Blue")
frame_blue.grid(row=0, column=0)
frame_blue.config(width=350, height=250)

frame_green = tk.Frame(root, background="Lime")
frame_green.grid(row=0, column=1)
frame_green.config(width=150, height=250)

frame_red = tk.Frame(root, background="Red")
frame_red.grid(row=1, column=0)
frame_red.config(width=350, height=250)

frame_yellow = tk.Frame(root, background="Yellow")
frame_yellow.grid(row=1, column=1)
frame_yellow.config(width=150, height=250)

root.mainloop()