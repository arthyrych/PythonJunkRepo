print('Homework 5\n')

print('Function 1\n')
# Необходимо создать три словаря и написать функцию,
# которая сможет брать словари и производить их слияние в один

car_1 = {"model": "Model S", "name": 'Tesla', "year": 2017}
car_2 = {"model": "Leaf", "name": 'Nissan', "year": 2019}
car_3 = {"model": "Zoe", "name": 'Renault', "year": 2020}
my_cars = {}


def my_cars_fun():
    my_cars_add = {
        "car_1": car_1,
        "car_2": car_2,
        "car_3": car_3
    }
    my_cars.update(my_cars_add)


print(car_1, '\n', car_2, '\n', car_3)
my_cars_fun()
print('\n', my_cars)

print('Function 2\n')
# Нужно написать функцию, которая позволит Вам конвертировать
# указанное Вами число секунд в формат записи дни:часы:минуты:секунды
