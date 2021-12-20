def countFood():
    a = int(input())
    b = int(input())
    print("Всего", a+b, "шт.")

print ("Сколко бананов и ананасов для обезьян?")
countFood ()

print ("Сколко жуков и червей для ежей?")
countFood ()

print ("Сколко рыб и моллюсков для выдр?")
countFood ()

#
def rectangle ():
    a = float(input("Ширина: "))
    b = float(input("Высота: "))
    print ("Площадь: %.2f" % (a*b))

def triangle():
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    print("Площадь: %.2f" % (0.5 * a * h))

def circle():
    r = float(input("Радиус: "))
    print("Площадь: %.2f" % (3.14 * r**2))

figure = input("1-прямоугольник, 2-треугольник, 3-круг: ")
if figure == '1':
    rectangle()
elif figure == '2':
    triangle()
elif figure == '3':
    circle()
else:
    print("Ошибка ввода")
"""
#
result = 0

def rectangle():
    a = float(input('Ширина: '))
    b = float(input('Высота: '))
    result = a*b

def triangle():
    a = float(input('Основание: '))
    h = float(input('Высота: '))
    result = 0.5 * a * h

figure = input('1-прямоугольник, 2-треугольник: ')
if figure == '1':
    rectangle()
elif figure == '2':
    triangle()

print('Площадь: %.2f' % result)
"""
#
result = 0

def rectangle():
    a = float (input("Ширина: "))
    b = float (input("Высота: "))
    global result
    result = a*b

def triangle():
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    global result
    result = 0.5 * a * h

figure =input("1-прямоугольник,2-треугольник:")
if figure =='1':
    rectangle()
elif figure =='2':
    triangle()

print("Площадь: %.2f" % result)

#
def exchange(usd_rate, money):
    result = round(money/usd_rate, 2)
    return result

result1 = exchange (60, 30000)
print(result1)
result2 = exchange (56,30000)
print(result2)
result3 = exchange (65,30000)
print(result3)

#
def create_default_user():
    name = "Tom"
    age = 33
    return name, age

user_name, user_age = create_default_user()
print("Name:", user_name, "\t Age:", user_age)

#
def cylinder():
    r = float(input())
    h = float(input())
    side = 2*3.14*r*h
    circle = 3.14*r**2
    full = side+2*circle
    return full
square = cylinder()
print(square)

#
def cylinder():
    r = float(input())
    h = float(input())
    side = 2*3.14*r*h
    circle = 3.14*r**2
    full = side + 2*circle
    return side,full
sCyl,fCyl = cylinder()
print("Площадь боковой поверхности %.2f" % sCyl)
print("Полная площадь %.2f" % fCyl)

#
def cylinder (h,r=1):
    side=2*3.14*r*h
    circle=3.14*r**2
    full=side+2*circle
    return full
figure1 = cylinder(4,3)
figure2 = cylinder(5)
print(figure1)
print(figure2)

#
def main():
    say_hello("Tom")
    usd_rate = 56
    money = 30000
    result = exchange(usd_rate,money)
    print("К выдаче", result, "долларов")
def say_hello(name):
    print("Hello,",name)
def exchange(usd_rate,money):
    result = round(money/usd_rate,2)
    return result
main()
