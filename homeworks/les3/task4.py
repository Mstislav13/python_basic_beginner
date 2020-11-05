def my_func(x, y):
    return x ** y
print(my_func(int(input('Введите число: ')), int(input('Введите отрицательную степень числа: '))))

def my_func_2(b, c):
    result = 1
    for i in range(abs(c)):
        result *= b
    if c >= 0:
        return result
    else:
        return 1 / result
print(my_func_2(int(input('Введите число: ')), int(input('Введите отрицательную степень числа: '))))