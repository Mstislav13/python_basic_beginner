firm = {'Иванов': 18000, 'Петров': 21000, 'Сидоров': 25000, 'Быков': 15000}
try:
    file_obj = open("file_3.txt", 'w')
    for last_name, salary in firm.items():
        file_obj.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print('Произошла ошибка ввода-вывода!')
finally:
    file_obj.close()
summa = 0
count = 0
persons = []
with open('file_3.txt', 'r') as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 20000:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f'Сотрудники с окладом меньше 20000: {persons}')
print(f'Средняя зарплата всех сотрудников: {result}')