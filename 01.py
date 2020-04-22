def say_hello(name):
    print("Hello {}".format(name))

say_hello2 = say_hello

say_hello2('Vijay')

ENVIRONMENT = 'dev'

def fetch_data_real():
    print('Calling API')

def fetch_data_fake():
    print('Returning Fake Data')
    return {
        'name': 'Vijay',
        'age': 26
    }

fetch_data = fetch_data_real if ENVIRONMENT == 'prod' else fetch_data_fake

data = fetch_data()
print(data)