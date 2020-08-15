from tkinter import *

root =Tk()

new_canvas = Canvas(root, width=200, height=100)
new_canvas.pack()

new_line = new_canvas.create_line(0, 0, 50, 100)
new_line2 = new_canvas.create_line(10, 10, 100, 100, fill='Red')


root.mainloop()
