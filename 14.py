def curry_add(x):
    def curry_add_inner(y):
        def curry_add_outer(z):
            return x + y +z
        return curry_add_outer
    return curry_add_inner

add_1 = curry_add(1)
add2 = add_1(2)
add3 = add2(3)

print(add3)

print(curry_add(1)(2)(3))