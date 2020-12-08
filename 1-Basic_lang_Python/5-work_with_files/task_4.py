# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

ru=['один','два','три','четыре']
with open('task4_text.txt','r',encoding='utf-8') as f:
    li = f.readlines()
    print(li)

with open('task4_newtext.txt','w+', encoding='utf-8') as f:
    for i in li:
        if '1' in i:
            a = i.replace('One',ru[0])
            print(a)
        elif '2' in i:
            a = i.replace('Two', ru[1])
            print(a)
        elif '3' in i:
            a = i.replace('Three', ru[2])
            print(a)
        else:
            a = i.replace ('Four', ru[3])
        f.write(a)
#
#



