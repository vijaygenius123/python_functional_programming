def double(x):
    return x * 2

def triple(x):
    return x * 3

def quadraple(x):
    return x * 4



def create_multiplier(a):
    def multiplier(x):
        return x * a
    
    return multiplier

double_func = create_multiplier(2)
triple_func = create_multiplier(3)
quadraple_func = create_multiplier(4)

r = 10
dia = double(r)
print(dia)
dia_func = double_func(r)
print(dia_func)