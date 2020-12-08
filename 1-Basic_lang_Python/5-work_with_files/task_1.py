# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


w = open ('test.txt', 'w')
while True:
    inp = str (input ())
    with open ('test.txt', 'a+') as w:
        w.write (inp + '\n')
        txt = w.read ()
        print (txt)
    if inp == '':
        break
