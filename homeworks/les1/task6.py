distance = int(input('Введите вашу начальную дистанцию (км.): '))
distance2 = int(input('Введите желаемую дистанцию (км.): '))

days = 1
while distance < distance2:
    distance *= 1.1
    days += 1
day_x = f"На {days}-й день вы достигните результата - неменее {distance2} км."
print(day_x)