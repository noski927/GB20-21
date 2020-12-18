# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random
import math

def generate_num():
    num = math.trunc (random.gauss (899, 100))
    return num
with open ('task5_text.txt', 'w') as f:
    a=['{}'.format(generate_num()) for _ in range(10)]
    f.write(str(a))





