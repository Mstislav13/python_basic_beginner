result_dict = {}

with open('file_6.txt', 'r', encoding='UTF-8') as my_file:
    line_number = 1
    for line in my_file:
        try:
            tmp = line.index(':')
            item_name = line[:tmp]
            result_dict[item_name] = 0
            new_list = line[tmp + 1:].split(' ')
            for el in new_list:
                if el.find('(') != -1:
                    result_dict[item_name] += int(el[:el.find('(')])
        except ValueError:
            print(f'Ошибка.')

        finally:
            line_number += 1
new_dict = result_dict
print(f'Общее количество часов по предметам :\n{new_dict}')