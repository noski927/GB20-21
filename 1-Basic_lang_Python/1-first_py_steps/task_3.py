# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

n = int(input('введите число: '))

n = str(n)
nn = n + n
nnn = n + n + n
numbers = int(n) + int(nn) + int(nnn)
print(numbers)
