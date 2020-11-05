def my_sum ():
    sum_result = 0
    i = False
    while i == False:
        number = input('Введите числа через пробел или нажмите Q для выхода из программы - ').split()

        res = 0
        for element in range(len(number)):
            if number[element] == 'q' or number[element] == 'Q':
                i = True
                break
            else:
                res = res + int(number[element])
        sum_result = sum_result + res
        print(f'Сумма =  {sum_result}')
    print(f'Ваша итоговая сумма =  {sum_result}')

my_sum()