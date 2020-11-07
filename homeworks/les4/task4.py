my_list = [5, 3, 8, 8, 13, 9, 7, -5, 1, 1, 1, 46, 24]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)