# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.

from functools import reduce

num=[i for i in range (100,1001,2)]
mlt=reduce((lambda i,k : i*k),num)
print(mlt)