my_list = [6, 3, 15, -4, 11, 1, 9, 23, 4]
new_list = [el for el in my_list if el > my_list[my_list.index(el) - 1]]
print(new_list)