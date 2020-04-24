from functools import reduce

numbers_list = [0,1,2,3,4,5]

sum = reduce(lambda acc, x: acc + x, numbers_list)
print(sum)