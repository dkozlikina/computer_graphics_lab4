import math
import tkinter as tk

flagDot = False
flagPolygon = False
points = []
flagPolygon_copy = False
points_check = []

def draw(event):
    global points, flagPolygon, canvas, flagDot

    if flagDot:
        x, y = event.x, event.y
        canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill="black", outline='white')
        points.append((x, y))
        flagDot = False
        check_point(x, y)

    if flagPolygon:
        x, y = event.x, event.y
        canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill="black", outline='white')
        points.append((x, y))

def fDot():
    global flagDot
    flagDot = True

def fPolygon():
    global flagPolygon
    flagPolygon = True

def draw_edges():
    global points, flagPolygon, canvas, points_check, flagPolygon_copy
    if len(points) != 0:
        points_check = points.copy()
        for i in range(len(points)-1):
            dot1 = points[i]
            dot2 = points[i + 1]
            canvas.create_line(dot1[0], dot1[1], dot2[0], dot2[1], fill="black", width=1)
        canvas.create_line(points[0][0], points[0][1], points[-1][0], points[-1][1], fill="black", width=1)
        flagPolygon_copy = flagPolygon
        points.clear()
        flagPolygon = False
def is_convex(points):
    n = len(points)
    if n < 3:
        return False

    def dot_product(v1, v2):
        return v1[0] * v2[0] + v1[1] * v2[1]

    prev_angle = None
    for i in range(n):
        p1 = points[i]
        p2 = points[(i + 1) % n]
        p3 = points[(i + 2) % n]

        v1 = (p2[0] - p1[0], p2[1] - p1[1])
        v2 = (p3[0] - p2[0], p3[1] - p2[1])

        cross_product = v1[0] * v2[1] - v1[1] * v2[0]

        angle = math.atan2(cross_product, dot_product(v1, v2))

        if prev_angle is None:
            prev_angle = angle
        else:
            if angle * prev_angle < 0:
                return False
            prev_angle = angle

    return True

def is_inside(x, y, polygon):
    n = len(polygon)
    inside = False

    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
        p1x, p1y = p2x, p2y

    return inside

def check_point(x, y):
    global points_check, result_label, flagPolygon_copy

    if flagPolygon_copy:
        if len(points_check) >= 3:
            pol_inside = is_inside(x, y, points_check)
            pol_convex = is_convex(points_check)
            if pol_convex:
                if pol_inside:
                    result_label.config(text="Точка принадлежит выпуклому многоугольнику")
                else:
                    result_label.config(text="Точка не принадлежит выпуклому многоугольнику")
            else:
                if pol_inside:
                    result_label.config(text="Точка принадлежит невыпуклому многоугольнику")
                else:
                    result_label.config(text="Точка не принадлежит невыпуклому многоугольнику")
    else:
        result_label.config(text="Сначала задайте полигон")

def clean():
    global canvas, points, flagPolygon_copy, flagDot, flagPolygon, points_check
    canvas.delete("all")
    points = []
    points_check = []
    flagPolygon = False
    flagPolygon_copy = False
    flagDot = False

root = tk.Tk()
root.title("lab4")

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

canvas.bind("<Button-1>", draw)  # Нажатие левой кнопки мыши

# Фрейм для размещения кнопок снизу окна
button_frame = tk.Frame(root)
button_frame.pack(side="bottom")

btn3 = tk.Button(button_frame, text="Задать полигон", command=fPolygon)
btn3.pack(side="left")

btn3 = tk.Button(button_frame, text="Отрисовать полигон", command=draw_edges)
btn3.pack(side="left")

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(side="top")

check_button = tk.Button(button_frame, text="Проверить принадлежность точки", command=fDot)
check_button.pack(side="left")

btn4 = tk.Button(button_frame, text="Очистка", command=clean)
btn4.pack(side="left")

root.mainloop()
