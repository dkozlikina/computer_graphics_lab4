import tkinter as tk
import math

start_segm = False
points = []
rotated_segments = []
current_segment_id = None  # Идентификатор текущего отрезка на холсте

def draw(event):
    global points, canvas, current_segment_id, start_segm

    if start_segm:
        x, y = event.x, event.y
        points.append((x, y))

        if len(points) == 2:
            draw_segment()
            start_segm = False

def fSegment():
    global current_segment_id, points, start_segm
    current_segment_id = None  # Сбрасываем идентификатор текущего отрезка
    points.clear()
    start_segm = True

def clean():
    global canvas, rotated_segments, current_segment_id, start_segm
    canvas.delete("all")
    rotated_segments.clear()
    current_segment_id = None
    start_segm = False

def draw_segment():
    global points, canvas, current_segment_id
    dot1 = points[0]
    dot2 = points[1]
    if current_segment_id:
        # Удаляем текущий отрезок, если он существует
        canvas.delete(current_segment_id)
    current_segment_id = canvas.create_line(dot1[0], dot1[1], dot2[0], dot2[1], fill="black", width=1)
    rotated_segments.append(points[:])  # Сохраняем текущий отрезок

def rotate_segment():
    global points, canvas, current_segment_id
    if len(points) == 2:
        center_x = (points[0][0] + points[1][0]) / 2
        center_y = (points[0][1] + points[1][1]) / 2
        angle = math.radians(90)  # Угол поворота на 90 градусов в радианах

        # Поворачиваем точки относительно центра
        new_points = []
        for x, y in points:
            x -= center_x
            y -= center_y
            new_x = center_x + x * math.cos(angle) - y * math.sin(angle)
            new_y = center_y + x * math.sin(angle) + y * math.cos(angle)
            new_points.append((new_x, new_y))

        # Удаляем текущий отрезок
        if current_segment_id:
            canvas.delete(current_segment_id)

        # Рисуем повернутый отрезок
        current_segment_id = canvas.create_line(new_points[0][0], new_points[0][1], new_points[1][0], new_points[1][1], fill="black", width=1)

        points[:] = new_points  # Заменяем текущие точки на повернутые

root = tk.Tk()
root.title("lab4")

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

canvas.bind("<Button-1>", draw)  # Нажатие левой кнопки мыши

btn2 = tk.Button(root, text="Задать отрезок", command=fSegment)
btn2.pack(side="left")

btn3 = tk.Button(root, text="Повернуть на 90 градусов", command=rotate_segment)
btn3.pack(side="left")

btn4 = tk.Button(root, text="Очистка", command=clean)
btn4.pack(side="left")

root.mainloop()
