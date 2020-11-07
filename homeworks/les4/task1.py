def pay():
    try:
        time = float(input('Выработка в часах - '))
        salary = float(input('Ставка (в час) по договору - '))
        bonus = float(input('Премия - '))
        total = time * salary + bonus
        print(f'Заработная плата сотрудника составит - {total}')
    except ValueError:
        return print('Введите число')
pay()