import tkinter as tk
import math

def some_function_from_rebra():
    flagSegment = False
    points = []
    povorot_segments = []
    segment_id = None

    def draw(event):
        nonlocal points, canvas, segment_id

        x, y = event.x, event.y
        points.append((x, y))

        if len(points) == 2:
            draw_segment()

    def fSegment():
        nonlocal segment_id, points
        segment_id = None
        points.clear()

    def clean():
        nonlocal canvas, povorot_segments, segment_id
        canvas.delete("all")
        povorot_segments.clear()
        segment_id = None

    def draw_segment():
        nonlocal points, canvas, segment_id
        dot1 = points[0]
        dot2 = points[1]
        if segment_id:
            canvas.delete(segment_id)
        segment_id = canvas.create_line(dot1[0], dot1[1], dot2[0], dot2[1], fill="black", width=1)
        povorot_segments.append(points[:])

    def povorot_segment():
        nonlocal points, canvas, segment_id
        if len(points) == 2:
            center_x = (points[0][0] + points[1][0]) / 2
            center_y = (points[0][1] + points[1][1]) / 2
            angle = math.radians(90)

            new_points = []
            for x, y in points:
                x -= center_x
                y -= center_y
                new_x = center_x + x * math.cos(angle) - y * math.sin(angle)
                new_y = center_y + x * math.sin(angle) + y * math.cos(angle)
                new_points.append((new_x, new_y))

            if segment_id:
                canvas.delete(segment_id)

            segment_id = canvas.create_line(new_points[0][0], new_points[0][1], new_points[1][0], new_points[1][1], fill="black", width=1)

            points[:] = new_points

    root = tk.Tk()
    root.title("Поворот")

    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()

    canvas.bind("<Button-1>", draw)

    btn2 = tk.Button(root, text="Задать отрезок", command=fSegment)
    btn2.pack(side="left")

    btn3 = tk.Button(root, text="Повернуть на 90 градусов", command=povorot_segment)
    btn3.pack(side="left")

    btn4 = tk.Button(root, text="Очистка", command=clean)
    btn4.pack(side="left")

    root.mainloop()

some_function_from_rebra()