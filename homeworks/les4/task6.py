from itertools import count

for el in count(int(input('Введите начальное число - '))):
    print(el)  #Бесконечный цикл

from itertools import cycle

new_list = [17, 85, 0, False, True, -6]
for el in cycle(new_list):
    print(el)   #Бесконечный цикл