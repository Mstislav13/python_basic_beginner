number_set = '17 85 0 2.6 13 78 5 4 -3 2 1 15.9'

with open('file_5.txt', 'w+', encoding='UTF-8') as file_obj:
    file_obj.write(number_set)
with open('file_5.txt', 'r', encoding='UTF-8') as file_obj:
    my_number = map(float, file_obj.read().split())
sum_num = sum(my_number)
print(f'Сумма чисел = {sum_num}')