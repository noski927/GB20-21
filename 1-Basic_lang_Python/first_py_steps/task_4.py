# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


num = int(input("Enter your number "))

i = -1
while num > 10:
    d = num % 10
    num //= 10
    if d > i:
        i = d
print(i)

# i = 0
# while i < N- 1:
#     a = 0
#     while a < N - 1 - i:
#         if num[a] > num[a + 1]:
#             num[a], num[a + 1] = num[a + 1], num[a]
#     a += 1
# i += 1

# print(a)
