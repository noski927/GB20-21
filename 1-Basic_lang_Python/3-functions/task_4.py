# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.


### первый вариант

def my_func():
    try:
        x, y = int (input ('действительное положительное число')), int (input ('целое отрицательное число'))
        if y>0:
            raise Exception (f'number {y} after zero') # оно работает ,но красивее не получилось
    except ValueError:
        return
    mf=x**y
    return mf

print(my_func())


### второй вариант


# def my_func(x,y):
#     #return (map(lambda x: x*y*y ,x))
#
# x=int(input())
# y = int (input ())
# func=my_func(x,y)
# print(func)
#
# def my_func(x,y):
