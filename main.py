import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import math
import tkinter as tk
import sys
from tkinter import colorchooser
from tkinter import Tk, Frame, Button, BOTH, SUNKEN
from tkinter import colorchooser


# def start_drawing(event):
#     global prev_x, prev_y
#     prev_x, prev_y = event.x, event.y

flagDot = False
flagSegment = False
flagPolygon = False
flagMakePolygon = False
points = []

def draw(event):
    global points, flagDot, flagSegment, flagPolygon, flagMakePolygon

    if flagDot:
        x, y = event.x, event.y
        canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill="black", outline='white')
        flagDot = False

    if flagSegment:
        x, y = event.x, event.y
        canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill="black", outline='white')
        points.append((x, y))
        if len(points) == 2:
            draw_segment()
            points.clear()
            flagSegment = False

    if flagPolygon:
        x, y = event.x, event.y
        canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill="black", outline='white')
        points.append((x, y))
        # if flagMakePolygon:
        #     draw_edges()
        #     points.clear()
        #     flagMakePolygon = False

def fDot():
    global flagDot
    flagDot = True

def fSegment():
    global flagSegment
    flagSegment = True

def fPolygon():
    global flagPolygon
    flagPolygon = True

def fMakePolygon():
    global flagMakePolygon
    flagMakePolygon = True

def draw_segment():
    global points
    dot1 = points[0]
    dot2 = points[1]
    canvas.create_line(dot1[0], dot1[1], dot2[0], dot2[1], fill="black", width=1)

def draw_edges():
    global points, flagPolygon
    # for i in range(-1, len(points)):
    #     dot1 = points[i]
    #     dot2 = points[i + 1]
    #     canvas.create_line(dot1[0], dot1[1], dot2[0], dot2[1], fill="black", width=1)
    for i in range(len(points)-1):
        dot1 = points[i]
        dot2 = points[i + 1]
        canvas.create_line(dot1[0], dot1[1], dot2[0], dot2[1], fill="black", width=1)
    canvas.create_line(points[0][0], points[0][1], points[-1][0], points[-1][1], fill="black", width=1)
    points.clear()
    flagPolygon = False

def clean():
    global canvas
    canvas.delete("all")

# def on_button_click():
#     global fill1
#     (rgb, hx) = colorchooser.askcolor(title="палитра цветов")
#     frame.config(bg=hx)
#     #fill1 = hx
#     #print(hx, rgb, rgb[0], rgb[1], rgb[2])
#     # frame.config(bg=hx)
#     fill1 = rgb
#     # return color_code



root = tk.Tk()
root.title("lab4")

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

vertexes = []

canvas.bind("<Button-1>", draw)  # Нажатие левой кнопки мыши

btn1 = Button(root, text="Задать точку")
btn1.config(command=fDot)
btn1.pack(side="left")

btn2 = Button(root, text="Задать отрезок")
btn2.config(command=fSegment)
btn2.pack(side="left")

btn3 = Button(root, text="Задать полигон")
btn3.config(command=fPolygon)
btn3.pack(side="left")

btn3 = Button(root, text="Отрисовать полигон")
btn3.config(command=draw_edges)
btn3.pack(side="left")

btn4 = Button(root, text="Очистка")
btn4.config(command=clean)
btn4.pack(side="left")


root.mainloop()
