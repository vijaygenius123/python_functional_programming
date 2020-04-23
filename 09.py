
numbers_list = [0,1,2,3,4,5]

even_list = list(filter(lambda x: x %2 == 0, numbers_list))
doubled_list = list(map(lambda x: x * 2, numbers_list))
print(even_list)
print(doubled_list)