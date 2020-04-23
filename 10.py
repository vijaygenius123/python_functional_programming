numbers_list = [0,1,2,3,4,5]


doubled_list = [x * 2 for x in numbers_list]

print(doubled_list)

even_list = [x for x in numbers_list if x % 2 == 0]

print(even_list)