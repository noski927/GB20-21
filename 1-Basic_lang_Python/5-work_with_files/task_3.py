# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

import numpy as np
import math

with open('task3_text.txt') as name_salary:
    a = name_salary.readlines ()
sal=[]
for i in a:
    name,salary=i.split(' - ')
    salary_num=int(salary)
    sal.append(int(salary_num))
    if salary_num < 20000:
        print(i)
print(f'средняя зарплата {math.trunc(np.mean(sal))}')



















