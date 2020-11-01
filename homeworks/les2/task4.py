user_str = input("Введите несколько слов: ")
word = user_str.split(' ')
for i, element in enumerate(word, 1):
    if len(element) > 10:
        element = element[0:10]
    print(f"{i}. {element}")