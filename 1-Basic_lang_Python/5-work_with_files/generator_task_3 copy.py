# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.

# создан программно

import random
import math

vowels_lower = 'aeiou'
vowels_upper = vowels_lower.upper()
consonants_lower = "bcdfghjklmnpqrstvwxz"
consonants_upper = consonants_lower.upper()
n = 100

def generate_name():
    name = random.choice(vowels_upper)
    for i in range(random.randint(1, 2)):
        name += random.choice(consonants_lower)
        name += random.choice(vowels_lower)
    return name

def generate_salary():
    salary = math.trunc(random.gauss(20000,10000))
    return salary

with open('task3_text_generator.txt','w+') as nm_sl:
    a = ['{} - {}'.format(generate_name(), generate_salary()) for _ in range(n)]
    nm_sl.write(str(a))
    ns = nm_sl.read()

print(ns)






