def add(x,y):
    return x + y

def subtract(x,y):
    return x - y


def combine_2_and_3(func):
    return func(3,2)

print(combine_2_and_3(add))
print(combine_2_and_3(subtract))
