# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# ]

name = str (input ('название: '))
price = int (input ('цена: '))
amount = int (input ('количество: '))
num = str (input ('eд: '))

#while True:


f = { "название": '', 'цена': '', 'количество': '', 'eд': '' }
a = { 'название': [], 'цена': [], 'количество': [], 'eд': [] }





print(a)