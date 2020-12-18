# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func():
    a_1,a_2,a_3=int(input()),int(input()),int(input())
    var=[a_1,a_2,a_3]
    var.sort()
    print(sum(var[1:]))
my_func()