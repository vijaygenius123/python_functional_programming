def create_printer():
    my_favourite_number = 42

    def printer():
        print("My Favourite Number Is {}".format(my_favourite_number))
    
    return printer

my_printer = create_printer()
my_printer()

