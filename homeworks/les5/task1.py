my_text = open('new.txt', 'w', encoding='UTF-8')
line = input('Введите текст: \n')
while line:
    my_text.writelines(line)
    line = input('Введите текст: \n')
    if not line:
        break

my_text.close()
my_text = open('new.txt', 'r')
content = my_text.readlines()
print(content)
my_text.close()