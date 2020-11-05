def my_func(num1, num2):
    try:
        z = num1 / num2
        return z
    except ZeroDivisionError:
        return "Делитель не может быть 0"

print(my_func(int(input("Введите делимое число = ")), int(input("Введите делитель числа = "))))