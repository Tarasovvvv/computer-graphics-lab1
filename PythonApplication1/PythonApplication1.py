# -*- coding: utf-8 -*-
from math import *
from tkinter import *
root = Tk()

r = 200
xc = 202
yc = 202
vertexCount = 3 #Количество вершин
angle = 2 * pi / vertexCount #Дуга окружности между двумя соседними вершинами

#Увеличение вершин
def increase(event): 
    global vertexCount
    vertexCount *= 2
    ceil(vertexCount)
    drawPolygon()

#Уменьшение вершин
def decreasae(event):
    global vertexCount
    if vertexCount > 3:
        vertexCount /= 2
        ceil(vertexCount)
    drawPolygon()
    
#Отрисовка многоугольника
def drawPolygon():
    global angle, vertexCount, canvas, circle, xc, yc, r
    angle = 2 * pi / vertexCount
    canvas.delete("all")
    circle = canvas.create_oval(xc - r, yc - r, xc + r, yc + r, outline="black")
    for i in range(int(vertexCount)):
        canvas.create_line(
            xc + r * cos(angle * i),
            yc - r * sin(angle * i),
            xc + r * cos(angle * (i + 1)),
            yc - r * sin(angle * (i + 1))
        )

canvas = Canvas(root, width=404, height=404)
drawPolygon()
root.bind("<Up>", increase)
root.bind("<Down>", decreasae)
canvas.pack()
root.mainloop()