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
            if (points_dinamic[0] >  points_dinamic[2]):
                canvas.create_window(70, 200, window=label2)
            else:
                canvas.create_window(70, 200, window=label1)
        if x_calc - 3 > prev_x and x_calc + 3 > prev_x:
            if (points_dinamic[0] >  points_dinamic[2]):
                canvas.create_window(70, 200, window=label1)
            else:
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
        print(x, y)
        # if ( points)
        tx1 = (x - points[0]) / (points[2] - points[0])
        ty1 = (y - points[1]) / (points[3] - points[1])

        tx2 = (x - points_dinamic[2]) / (points_dinamic[0] - points_dinamic[2])
        ty2 = (y - points_dinamic[3]) / (points_dinamic[1] - points_dinamic[3])

        print(tx1, ty1, tx2, ty2)
        print(tx1 + tx2)
        if (0 <= tx1 <= 1 and 0 <= ty1 <= 1 and 0 <= tx2 <= 1 and 0 <= ty2 <= 1):
            canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="red", outline='black')
        print(y == (m1 * x + c1) and y == (m2 * x + c2))

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

# Для определения пересечения двух отрезков через параметрические уравнения вы можете выполнить следующие шаги:
#
# Представьте каждый отрезок в виде параметрического уравнения, которое описывает его путь вдоль прямой. Обычно параметрическое уравнение отрезка имеет следующий вид:
#
# Для отрезка 1:
#
# x1 = x01 + t1 * (x02 - x01)
# y1 = y01 + t1 * (y02 - y01)
# Для отрезка 2:
#
# x2 = x03 + t2 * (x04 - x03)
# y2 = y03 + t2 * (y04 - y03)
# Где (x01, y01) и (x02, y02) - координаты начальной и конечной точек отрезка 1, а (x03, y03) и (x04, y04) - координаты начальной и конечной точек отрезка 2. t1 и t2 - параметры, которые определяют положение точек на отрезках.
#
# Решите систему уравнений для t1 и t2, чтобы найти точку пересечения. Это можно сделать путем приравнивания x1 и x2, а также y1 и y2:
#
# x01 + t1 * (x02 - x01) = x03 + t2 * (x04 - x03)
# y01 + t1 * (y02 - y01) = y03 + t2 * (y04 - y03)
#
# Решите систему уравнений для t1 и t2. Если система имеет решение, это означает, что отрезки пересекаются. Если система не имеет решения или решение находится вне интервала [0, 1] для t1 и t2, то отрезки не пересекаются.
#
# Если вы найдете решение в интервале [0, 1] для обоих t1 и t2, то пересекающаяся точка находится на обоих отрезках, и вы можете вычислить ее координаты.
#
# Это общий метод для определения пересечения отрезков с использованием параметрических уравнений. Вы можете применить этот метод к вашим отрезкам, заменив координаты отрезков и решив систему уравнений для t1 и t2.