def my_cars_fun():
    print('Function 1')
    car_1 = {"model": "Model S", "name": 'Tesla', "year": 2017}
    car_2 = {"model": "Leaf", "name": 'Nissan', "year": 2019}
    car_3 = {"model": "Zoe", "name": 'Renault', "year": 2020}
    print(car_1, '\n', car_2, '\n', car_3)
    my_cars = {}
    my_cars_add = {
        "car_1": car_1,
        "car_2": car_2,
        "car_3": car_3
    }
    my_cars.update(my_cars_add)
    print('My cars:', my_cars)

my_cars_fun()


def time():
    print('Function 2')
    x = int(input('Enter the amount of seconds which will be converted into dd/hh/mm/ss: '))
    dd = x // 86400
    ost = x % 86400
    hh = ost // 3600
    ost = ost % 3600
    mm = ost // 60
    ost = ost % 60
    ss = ost
    print('Time is', dd, 'days', hh, 'hours', mm, 'minutes', 'and', ss, 'seconds')
    
time()


from datetime import timedelta
def convert():
    print('Function 3 and it is the same as the previous one: ')
    x = int(input("Enter seconds: "))
    d = timedelta(seconds=x)
    print(d)

convert()
