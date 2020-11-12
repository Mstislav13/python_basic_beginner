my_list = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit,\n' 
           'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n'
           'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n' 
           'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\n' 
           'Excepteur sint occaecat cupidatat non proident,\n' 
           'sunt in culpa qui officia deserunt mollit anim id est laborum.\n']
with open('file_1.txt', 'w+', encoding='UTF-8') as file_obj:
    file_obj.writelines(my_list)
with open('file_1.txt') as file_obj:
    lines = 0
    letters = 0
    num_line = 0
    for line in file_obj:
        lines += line.count('\n')
        num_line += 1
        letters = len(line) - 1
        print(f'{letters} слов в строке № {num_line}')
    print(f'Количество строк : {lines}')