user_number = int(input('Введите целое положительное число: '))
max = user_number % 10
while user_number >= 1:
    user_number = user_number // 10
    if user_number % 10 > max:
        max = user_number % 10
    if user_number > 9:
        continue
    else:
        print("Максимальная цифра в числе ", max)
        break