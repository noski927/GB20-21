# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

import json


firm = {}
average = []
with open ('task7_text.txt', ) as f:
    lines=f.readlines()

for l in lines:
    name,form,profit,minus = l.split(' ')
    pr_pr = int(profit)-int(minus)
    firm[name]=profit
    if pr_pr>0:
        average.append(pr_pr)

average=sum(average)/len(average)

full_info = [firm,{'average':average}]

with open('task7.json', 'w') as f_json:
    json.dump(full_info, f_json)

