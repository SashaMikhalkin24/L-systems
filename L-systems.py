"""В файле есть все данные для задания фрактала. Считываем аксиому(начальное состояние строки),
правило построения Л-строки (зипаем словарь), начальные параметры (зипаем с ключами словаря)"""

def get_data(n):
    with open('fractals.txt', 'r') as file:
        L = 5
        lines = list(map(str.rstrip, file.readlines()))
        axiom = lines[L * n]
        rules = dict(zip(lines[L * n + 1].split(), lines[L * n + 2].split()))
        nums = list(map(float, lines[L * n + 3].split()))
        rost = list(map(float, lines[L * n + 4].split()))[0]
        return axiom, rules, nums, rost

"""Импортируем нужные библиотеки"""

from turtle import *
import random

"""Настроим окно рисования. Выставим большие размеры окна, форму черипахи,
и минимизируем задержку рисования больших систем."""

hideturtle()
screensize(10000, 10000, "#faebd7")
setup(width=1600, height=1400, startx=0, starty=0)
bgcolor("#faebd7")
shape('turtle')
tracer(100000)

"""n - выбор фрактала, m - глубина фрактала"""

goto(0, -100)
write("Выберете, какую Л-систему хотите изобразить. Для этого введите число:\n\n" + 40 * " " + "1 - кривая Коха (7);\n" + 40 * " " +
    "2 - кривая Коха* (7);\n" + 40 * " " + "3 - кривая Коха** (7);\n" + 40 * " " + "4 - множество Кантора(10);\n" + 40 * " " +
    "5 - треугольник Серпинского (11);\n" + 40 * " " + "6 - треугольник Серпинского* (8);\n" + 40 * " " + "7 - ковер Серпинского (4)\n" + 40 * " " +
    "8 - кривая дракона (9, 18 - рекомендуемые)\n" + 40 * " " + "9 - дерево Пифагора (15)\n" + 40 * " " + "10 - дерево Пифагора* (14)\n" + 40 * " " +
    "11 - скрещивание\n\n" + 35 * " " + "Далее введите глубину Л-системы.\n" + 27 * " " + "Максимальная глубина указана в скобках.",
    True, align="center", font=("Arial", 20, "normal"))

"""Строим Л-строку глубиной m по правилу номер n"""


n = int(numinput("Номер L-системы", "", default=None, minval=1, maxval=15))
m = int(numinput("Глубина L-системы", "", default=None, minval=1, maxval=20))
axiom, rules, nums, rost = get_data(n-1)
L = axiom
L_dop = ''
for i in range(m):
    for j in L:
        L_dop += rules[j]
    L = L_dop
    L_dop = ''
print(L)

"""Зададим общие команды, которые будут общие для все Л-систем. Далее из них будем конструировать саму систему
Все нужные параметры описаны в документе fractals."""

"""
F - движение вперед;
f - движение вперед;
T - движение вперед;
t - движение вперед;
+ - поворот вправо;
- - поворот влево;
S - скос вправо;
s - скос влево;
[ - сохранение координат черепахи в стек;
] - восстановление координат чеперахи из стека;
R - поворот со случайным сдвигом вправо;
L - поворот со случайным сдвигом влево;
U - поднять перо;
D - опустить перо;
C - рисуем квадрат;
P - перенести черепаху не рисуя линии
p - перенести на полпути
"""

clear()
pensize(1)
stack = []
left(90)
penup()
goto(-300, -300)
pendown()

if n == 1:
    begin_fill()
    for i in L:
        if i == '+':
            right(nums[0])
        elif i == '-':
            left(nums[1])
        elif i == 'F':
            forward(nums[2] * rost ** (-m))
    end_fill()

if n == 2:
    begin_fill()
    for i in L:
        if i == '+':
            right(nums[0])
        elif i == '-':
            left(nums[1])
        elif i == 'F':
            forward(nums[2] * rost ** (-m))
        elif i == 'f':
            forward(nums[2] * rost ** (-m))
    end_fill()

if n == 3:
    p = float(numinput("Доля срезов", "от 0 до 1", default=None, minval=0, maxval=1))
    begin_fill()
    for i in L:
        if i == 'S':
            right(45)
            forward(nums[0] * p * (2 ** 0.5) * rost ** (-m))
            right(45)
        elif i == 's':
            left(45)
            forward(nums[0] * p * (2 ** 0.5) * rost ** (-m))
            left(45)
        elif i == 'F':
            forward(nums[0] * rost ** (-m) * (1 - 2 * p))
    end_fill()

if n == 4:
    pensize(10)
    right(90)
    delta_y = 0
    for j in range(0, m):
        pensize(10 / (j + 1))
        penup()
        delta_y -= 60 / (j + 1)
        goto(-300, delta_y + 100)
        pendown()
        for i in L:
            if i == 'F':
                forward(nums[0] * rost ** (-j))
            elif i == 'f':
                penup()
                forward(nums[0] * rost ** (-j))
                pendown()

if n == 5:
    left(270)
    if m % 2 == 0:
        for i in L:
            if i == '-':
                right(nums[0])
            elif i == '+':
                left(nums[0])
            elif i == 'F':
                forward(nums[1] * rost ** (-m))
            elif i == 'f':
                forward(nums[1] * rost ** (-m))
    else:
        for i in L:
            if i == '-':
                left(nums[0])
            elif i == '+':
                right(nums[0])
            elif i == 'F':
                forward(nums[1] * rost ** (-m))
            elif i == 'f':
                forward(nums[1] * rost ** (-m))

if n == 6:
    right(90)
    l = nums[1] / rost**m
    for i in L:
        if i == '+':
            right(nums[0])
        elif i == '-':
            left(nums[0])
        elif i == 'P':
            penup()
            forward(l)
            pendown()
        elif i == 'p':
            penup()
            forward(l/2)
            pendown()
        elif i == 'C':
            begin_fill()
            forward(l)
            left(90)
            forward(l)
            left(90)
            forward(l)
            left(90)
            forward(l)
            left(90)
            end_fill()

if n == 7:
    right(90)
    l = nums[1] / rost**m
    for i in L:
        if i == '+':
            right(nums[0])
        elif i == '-':
            left(nums[0])
        elif i == 'P':
            penup()
            forward(l)
            pendown()
        elif i == 'C':
            begin_fill()
            forward(l)
            left(90)
            forward(l)
            left(90)
            forward(l)
            left(90)
            forward(l)
            left(90)
            end_fill()

if n == 8:
    penup()
    goto(-250, -100)
    pendown()
    for i in L:
        if i == '+':
            right(nums[0])
        elif i == '-':
            left(nums[0])
        elif i == 'F':
            forward(nums[1] / rost ** m)

if n == 9:
    penup()
    goto(0, -300)
    pendown()
    l = 2 * nums[1] / m / (m + 1)
    for i in L:
        if i == '+':
            right(nums[0]/2)
        elif i == '-':
            left(nums[0]/2)
        elif i == 'F':
            forward(l)
        elif i == 'f':
            forward(l)
        elif i == '2':
            forward(l)
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

if n == 10:
    penup()
    goto(0, -300)
    pendown()
    thick = 16
    pensize(thick)
    pencolor('#654321')
    l = 2 * nums[2] / m / (m + 1)
    for i in L:
        if i == '+':
            right(nums[1]/2 + random.randint(-nums[0], + nums[0]))
        elif i == '-':
            left(nums[1]/2 + random.randint(-nums[0], + nums[0]))
        elif i == 'F':
            if random.randint(0, 10) > 4:
                forward(l)
        elif i == 'f':
            pensize(4)
            r = random.randint(0, 30)
            if r % 3 == 0:
                pencolor('#cd5c5c')
            elif r % 3 == 1:
                pencolor('#e75480')
            else:
                pencolor('#f984e5')
            forward(l)
            pencolor('#654321')
        elif i == '2':
            if random.randint(0, 10) > 4:
                forward(l)
        elif i == '[':
            thick *= 0.75
            pensize(thick)
            stack.append((xcor(), ycor(), heading(), thick))
        elif i == ']':
            penup()
            x, y, ang, thick = stack[-1]
            pensize(thick)
            stack.pop()
            setheading(ang)
            setx(x)
            sety(y)
            pendown()

if n == 11:
    def tree(x, y, H, a1, a2, it, thick, k_thick, p1, p2, col1, col2, col3, col4):
        penup()
        goto(x, y)
        setheading(90)
        pendown()
        pensize(thick)
        pencolor(col1)
        l = 2 * H / it / (it + 1)
        for i in L:
            if i == '+':
                right(a2 / 2 + random.randint(-a1, a1))
            elif i == '-':
                left(a2 / 2 + random.randint(-a1, a1))
            elif i == 'F':
                if random.randint(0, 10) > p1:
                    forward(l)
            elif i == 'f':
                pensize(4)
                r = random.randint(0, 30)
                if r % 3 == 0:
                    pencolor(col2)
                elif r % 3 == 1:
                    pencolor(col3)
                else:
                    pencolor(col4)
                forward(l)
                pencolor(col1)
            elif i == '2':
                if random.randint(0, 10) > p2:
                    forward(l)
            elif i == '[':
                thick *= k_thick
                pensize(thick)
                stack.append((xcor(), ycor(), heading(), thick))
            elif i == ']':
                penup()
                x, y, ang, thick = stack[-1]
                pensize(thick)
                stack.pop()
                setheading(ang)
                setx(x)
                sety(y)
                pendown()
    colormode(255)
    def col(r, g, b):
        return (r, g, b)
    def get_rand():
        return [random.randint(600, 1000), random.randint(5, 40), random.randint(30, 90), m, random.randint(10, 20), random.random() * 0.3 + 0.6,
         random.randint(0, 7), random.randint(0, 7), col(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
         col(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), col(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
         col(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))]
    for it in range(5):
        A = [-1000, 1000 * it, *get_rand()]
        B = [-500, 1000 * it, *get_rand()]
        C = []
        for i in range(len(A)):
            if random.random() < 0.5:
                C.append(A[i])
            else:
                C.append(B[i])
        C[0] = 0
        print(A)
        tree(*A)
        tree(*B)
        tree(*C)



update()
exitonclick()