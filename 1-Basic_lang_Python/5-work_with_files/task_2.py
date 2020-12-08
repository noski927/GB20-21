# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.



with open('uncle.txt') as unc:
    aa=unc.read()
    aa_n=aa.split('\n')
    for i in range(1,len(aa_n)):
        aa_sep = aa_n[i].split(' ')
        line_len = (len(aa_sep))
        print (f'количество слов в строке {i} = {line_len}')

print (f'количесво строк: {len (aa_n)}')






