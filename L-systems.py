def get_data(n):
    with open('fractals.txt', 'r') as file:
        L = 5
        lines = list(map(str.rstrip, file.readlines()))
        axiom = lines[L * n]
        rules = dict(zip(lines[L * n + 1].split(), lines[L * n + 2].split()))
        nums = list(map(int, lines[L * n + 3].split()))
        params = list(map(int, lines[L * n + 4].split()))
        return axiom, rules, nums, params


from turtle import *

"""Настроим окно рисования. Выставим большие размеры окна и зададим свои систему координат."""
screensize(10000, 10000, "#faebd7")
#setworldcoordinates(0, 0, 100, 100)(своя система координат)
bgcolor("#faebd7")

shape('turtle')
delay()
speed(0)
tracer(10000)

n = int(input())
m = int(input())
axiom, rules, nums, params = get_data(n)
L = axiom
L_dop = ''
for i in range(m):
    for j in L:
        L_dop += rules[j]
    L = L_dop
    L_dop = ''
print(L)

pensize(1)
stack = []
for i in L:
    if i == '+':
        right(nums[0])
    elif i == '-':
        left(nums[1])
    elif i == 'F':
        forward(nums[2]*params[0]**(3-m))
    elif i == 'f':
        forward(nums[3]*params[0]**(3-m))
    elif i == '[':
        stack.append((xcor(), ycor(), heading()))
    elif i == ']':
        penup()
        x, y, ang = stack[-1]
        stack.pop()
        setheading(ang)
        setx(x)
        sety(y)
        pendown()
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
