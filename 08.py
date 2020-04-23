
numbers_list = [0,1,2,3,4,5]

def check_even(x):
    return x % 2 == 0

even_list = list(filter(check_even, numbers_list))

print(even_list)