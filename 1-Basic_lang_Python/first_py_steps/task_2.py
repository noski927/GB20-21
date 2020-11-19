# Пользователь вводит время в секундах. 
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. 
# Используйте форматирование строк.

time = int(input('введите количество секунд: '))

if time <= 60:
    print(time)
else:
    minutes = time//60
    time = time-(minutes*60)
    hours = minutes//60
    minutes = minutes-(hours*60)

    out = f'{hours}:{minutes}:{time}'
    print(out)
