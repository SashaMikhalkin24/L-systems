from turtle import *

"""Настроим окно рисования. Выставим большие размеры окна и зададим свои систему координат."""
screensize(10000, 10000, "#faebd7")
#setworldcoordinates(0, 0, 100, 100)(своя система координат)
bgcolor("#faebd7")

shape('turtle')
delay()
speed(0)
tracer(100)

n = int(input())
axiom = 'F'
rules = {'+': '+', '-': '-', 'F': 'F+F-F-F+F'}
L = axiom
L_dop = ''
for i in range(n):
    for j in L:
        L_dop += rules[j]
    L = L_dop
    L_dop = ''
print(L)

pensize(1)
for i in L:
    if i == '+':
        right(90)
    elif i == '-':
        left(90)
    else:
        forward(2)
update()




exitonclick()













'''axiom = '0'
rule = {'1': '11', '0': '1[0]0', '[': '[', ']': ']'}
L = axiom
L_sl = ''
n = int(input())
for i in range(n):
    for j in L:
        L_sl += rule[j]
    L = L_sl
    L_sl = ''
print(L)'''
