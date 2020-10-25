proceeds = int(input('Введите выручку вашей фирмы (в рублях): '))
cost = int(input('Введите издержки вашей фирмы (в рублях): '))

if proceeds > cost:
    print('Ваша фирма прибыльна.')
elif proceeds == cost:
    print('Ваша фирма работает в 0.')
else:
    print('Ваша фирма убыточна.')

profit = proceeds - cost
profitability = f"Рентабельность фирмы составляет: {(profit/proceeds) * 100} %"
print(profitability)

personnel = int(input('Введите численность сотрудников вашей фирмы: '))
income = f"Прибыль фирмы в расчёте на одного сотрудника составит: {profit/personnel} рублей."
print(income)


