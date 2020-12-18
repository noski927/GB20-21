# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


from sys import argv
if 'h' in argv:
    print("""-=HELP=- 
          script calcultes of salary
          1) production in hours
          
          2) rate per hour
          
          3) premium
          
          (production in hours * rate per hour) + premium   
          """)
else:
    print('Start program')
    production_in_hours,rate_per_hour,premium = argv[1:]
    production_in_hours=int(production_in_hours)
    rate_per_hour =int(rate_per_hour)
    premium=int (premium)
    salary= (production_in_hours*rate_per_hour)+premium
    print(salary)
    print('end')




# =int(input())
