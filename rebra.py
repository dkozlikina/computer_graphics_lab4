import tkinter as tk
import math

flagSegment = False
flagSegment2 = False
flagSegment3 = False
points = []
points_dinamic = []
rotated_segments = []
current_segment_id = None  # Идентификатор текущего отрезка на холсте
start_x, start_y, end_x, end_y = None, None, None, None
def draw(event):
    global points, points_dinamic, canvas, current_segment_id, flagSegment, start_x, start_y, end_x, end_y, flagSegment2, prev_x, prev_y, flagSegment3
    if flagSegment:
        x, y = event.x, event.y
        points.append((x, y))

        if len(points) == 2:
            draw_segment()
            flagSegment = False
    if flagSegment2:
        points_dinamic.clear()
        start_x, start_y = event.x, event.y
        end_x, end_y = None, None
    if flagSegment3:
        prev_x, prev_y = event.x, event.y
        canvas.create_oval(prev_x - 3, prev_y - 3, prev_x + 3, prev_y + 3, fill="blue", outline='red')
        m = (points_dinamic[3] - points_dinamic[1]) / (points_dinamic[2] - points_dinamic[0])
        c = points_dinamic[1] - m * points_dinamic[0]
        y_calc = round(m * prev_x + c)
        x_calc = round((prev_y - c) / m)
        print(prev_x, prev_y)
        print(x_calc, y_calc)
        if x_calc - 3 < prev_x and x_calc + 3 < prev_x:
            canvas.create_window(70, 200, window=label1)
        if x_calc - 3 > prev_x and x_calc + 3 > prev_x:
            canvas.create_window(75, 250, window=label2)
        if x_calc - 3 <= prev_x <= x_calc + 3:
            canvas.create_window(75, 100, window=label3)
        flagSegment3 = False

def update_edge(event):
    global end_x, end_y, start_x, start_y
    if flagSegment2:
        if start_x and start_y:
            end_x, end_y = event.x, event.y
            canvas.delete("edge")  # Удалить предыдущее ребро
            canvas.create_line(start_x, start_y, end_x, end_y, fill="black", tags="edge")

def stop_drawing(event):
    global start_x, start_y, end_x, end_y, flagSegment2
    if flagSegment2:
        if start_x and start_y and end_x and end_y:
            canvas.create_line(start_x, start_y, end_x, end_y, fill="black")
        for now in start_x, start_y, end_x, end_y:
            points_dinamic.append(now)
        start_x, start_y, end_x, end_y = None, None, None, None
        flagSegment2 = False

def fSegment():
    global current_segment_id, points, flagSegment, flagSegment2
    current_segment_id = None  # Сбрасываем идентификатор текущего отрезка
    flagSegment2 = False
    points.clear()
    flagSegment = True

def clean():
    global canvas, rotated_segments, current_segment_id, flagSegment, prev_x, prev_y, flagSegment2
    canvas.delete("all")
    prev_x, prev_y = -1, -1
    rotated_segments.clear()
    current_segment_id = None
    flagSegment = False
    flagSegment2 = False

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

def dinamic_rebro():
    global flagSegment2
    flagSegment2 = True


def my_point():
    temp = points.copy()
    points.clear()
    for now in temp:
        for now1 in now:
            points.append(now1)

    print(points, points_dinamic)
    m1 = (points[3] - points[1]) / (points[2] - points[0])
    m2 = (points_dinamic[3] - points_dinamic[1]) / (points_dinamic[2] - points_dinamic[0])
    if m1 == m2:
        canvas.create_window(200, 150, window=label)
    else:
        c1 = points[1] - m1 * points[0]
        c2 = points_dinamic[1] - m2 * points_dinamic[0]
        x = (c2 - c1) / (m1 - m2)
        y = m1 * x + c1
        canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="red", outline='black')
        print(x, y)


# m1 * x + c1 = m2 * x + c2
# x = (c2 - c1) / (m1 - m2)
# y = m1 * x + c1

def classification():
    global flagSegment3
    flagSegment3 = True

    # if y_calc > prev_y:
    #     print("Выше ")
    # if y_calc < prev_y:
    #     print("Ниже")
    # if min(points_dinamic[0], points_dinamic[2]) > prev_x:
    #     print("Левее ")
    # if max(points_dinamic[0], points_dinamic[2]) < prev_x:
    #     print("Правее ")
    # if min(points_dinamic[1], points_dinamic[3]) > prev_y:
    #     print("Ниже ")
    # if max(points_dinamic[1], points_dinamic[3]) < prev_y:
    #     print("Выше ")
    # if points_dinamic[0] < prex_x < points_dinamic[0]
root = tk.Tk()
root.title("lab4")

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

label = tk.Label(canvas, text="Ребра параллельны и не пересекаются")
label1 = tk.Label(canvas, text="Точка находится правее")
label2 = tk.Label(canvas, text="Точка находится левее")
label3 = tk.Label(canvas, text="Точка находится на прямой")
canvas.bind("<Button-1>", draw)
canvas.bind("<B1-Motion>", update_edge)
canvas.bind("<ButtonRelease-1>", stop_drawing)

btn2 = tk.Button(root, text="Задать отрезок", command=fSegment)
btn2.pack(side="left")

btn3 = tk.Button(root, text="Повернуть на 90 градусов", command=rotate_segment)
btn3.pack(side="left")

btn4 = tk.Button(root, text="Очистка", command=clean)
btn4.pack(side="left")

btn5 = tk.Button(root, text="Задать отрезок динамически", command=dinamic_rebro)
btn5.pack(side="left")

btn6 = tk.Button(root, text="Точка пересечения ребер", command=my_point)
btn6.pack(side="left")

btn7 = tk.Button(root, text="Классификация точки", command=classification)
btn7.pack(side="left")

root.mainloop()