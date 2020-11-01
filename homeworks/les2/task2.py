element_count = int(input('Введите, сколько элементов будет в списке?: '))
new_list = []
i = 0
element = 0
while i < element_count:
    new_list.append(input('Введите букву или цифру?: '))
    i += 1
for elements in range(int(len(new_list)/2)):
    new_list[element], new_list[element + 1] = new_list[element + 1], new_list[element]
    element +=2
print(new_list)