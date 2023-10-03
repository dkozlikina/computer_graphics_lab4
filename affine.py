import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import math
import tkinter as tk
import sys
from tkinter import colorchooser
from tkinter import Tk, Frame, Button, BOTH, SUNKEN
from tkinter import colorchooser
from collections import namedtuple

flagDot = False
flagSegment = False
flagPolygon = False
flagMakePolygon = False
flagPolygonExist = False
points = []


def draw(event):
    global points, flagDot, flagSegment, flagPolygon, flagMakePolygon, canvas

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
        points.append([x, y])


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
    global points, canvas
    dot1 = points[0]
    dot2 = points[1]
    canvas.create_line(dot1[0], dot1[1], dot2[0], dot2[1], fill="black", width=1)


def draw_edges():
    global points, flagPolygon, canvas, flagPolygonExist
    if len(points) != 0:
        for i in range(len(points) - 1):
            dot1 = points[i]
            dot2 = points[i + 1]
            canvas.create_line(dot1[0], dot1[1], dot2[0], dot2[1], fill="black", width=1)
        canvas.create_line(points[0][0], points[0][1], points[-1][0], points[-1][1], fill="black", width=1)
        #points.clear()
        flagPolygon = False
        flagPolygonExist = True


def clean():
    global canvas, flagPolygonExist
    flagPolygonExist = False
    points.clear()
    canvas.delete("all")

# def winClose():
#     global dx, dy, window
#     window.destroy
#     print("dddddd", dx, dy)

def clickMove():
    global dx, dy#, window
    if (flagPolygonExist):
        # global canvas
        window = Tk()
        x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2 + 200
        y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2 - 100
        # root.geometry('600x400+200+100')
        window.wm_geometry("+%d+%d" % (x, y))
        window.grab_set()
        window.resizable(False, False)
        window.title("Сместить")
        window.geometry("200x100")
        label = tk.Label(window, text="Введите смещение:")

        text_dx = tk.IntVar()
        text_dy = tk.IntVar()

        entry_dx = tk.Entry(window, textvariable=text_dx)
        entry_dy = tk.Entry(window, textvariable=text_dy)
        # entry_dx.var = tk.IntVar()
        # entry_dy.var = tk.IntVar()
        #text_dx = name_var
        #self.var.trace("w", self.show_message)
        btn = tk.Button(window, text="Готово", command=window.destroy)

        label.grid(row=0, columnspan=2)
        tk.Label(window, text="dx:").grid(row=1, column=0)
        tk.Label(window, text="dy:").grid(row=2, column=0)
        entry_dx.grid(row=1, column=1)
        entry_dy.grid(row=2, column=1)
        btn.grid(row=3, columnspan=2)
        # dx = int(entry_dx.get())
        # dy = int(entry_dy.get())
        dx = int(text_dx.get())
        dy = int(text_dy.get())
        #print(dx, dy)

def move():
    global points, dx, dy
    #rotated_points = [(0,0)] * len(points)
    for i in range(len(points)):
        x = points[i][0]
        y = points[i][1]
        # rotated_points[i][0] = x * math.cos(a) + y * math.sin(a)
        # rotated_points[i][1] = (-1) * x * math.sin(a) + y * math.cos(a)
        points[i][0] = x + dx
        points[i][1] = y + dy
    #clean()
    draw_edges()

def rotate():
    global points, a
    #rotated_points = [(0,0)] * len(points)
    for i in range(len(points)):
        x = points[i][0]
        y = points[i][1]
        # rotated_points[i][0] = x * math.cos(a) + y * math.sin(a)
        # rotated_points[i][1] = (-1) * x * math.sin(a) + y * math.cos(a)
        points[i][0] = x * math.cos(a) + y * math.sin(a)
        points[i][1] = (-1) * x * math.sin(a) + y * math.cos(a)
    #clean()
    draw_edges()

def resize():
    global points, k
    #rotated_points = [(0,0)] * len(points)
    for i in range(len(points)):
        x = points[i][0]
        y = points[i][1]
        # rotated_points[i][0] = x * math.cos(a) + y * math.sin(a)
        # rotated_points[i][1] = (-1) * x * math.sin(a) + y * math.cos(a)
        points[i][0] = x // k
        points[i][1] = y // k
    #clean()
    draw_edges()


root = tk.Tk()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 - 250
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 250
root.wm_geometry("+%d+%d" % (x, y))
root.resizable(False, False)
root.title("lab4")

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

a = 30
k = 2
dx, dy = 50, -20

canvas.bind("<Button-1>", draw)  # Нажатие левой кнопки мыши
#window = Tk()

btn1 = Button(root, text="Задать точку")
btn1.config(command=fDot)
btn1.pack(side="left")

btn3 = Button(root, text="Задать полигон")
btn3.config(command=fPolygon)
btn3.pack(side="left")

btn3 = Button(root, text="Отрисовать полигон")
btn3.config(command=draw_edges)
btn3.pack(side="left")

btn2 = Button(root, text="Сместить")
btn2.config(command=move)#clickMove)
btn2.pack(side="left")

btn2 = Button(root, text="Повернуть")
btn2.config(command=rotate)
btn2.pack(side="left")

btn2 = Button(root, text="Масштабировать")
btn2.config(command=resize)
btn2.pack(side="left")

btn4 = Button(root, text="Очистка")
btn4.config(command=clean)
btn4.pack(side="left")



root.mainloop()
