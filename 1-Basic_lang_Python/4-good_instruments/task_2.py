#Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
#Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
#Для формирования списка использовать генератор


mylist=[300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
mylist.sort()
print(mylist)
n_li=[i for i in range(len(mylist)) if mylist[i]>mylist[i-1]]
print(n_li)
