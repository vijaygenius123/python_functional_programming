from functools import partial

def add(x,y,z):
    return x + y + z

add_simple = partial(add,1)
print(add_simple(2,3))