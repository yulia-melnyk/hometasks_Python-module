
# # - створити функцію яка виводить ліст

list = [1,2,3,4,5,6]


def list_func(list):
    for i in list:
        print(f'[{list.index(i)}] -> {i}')


# list_func(list)
       
# - створити функцію яка приймає три числа та виводить та повертає найменьше.

def min_number(*args):
    if len(args) == 3:
        min_value = min(args)
        print('min value ', min_value)
        return min_value
    else:
        print('Must include 3 numbers!')

# min_number(2,5,7)

# - створити функцію яка приймає три числа та виводить та повертає найбільше.

def max_number(*args):
    if len(args) == 3:
        max_value = max(args)
        print('max value ', max_value)
        return max_value
    else:
        print('Must include 3 numbers!')    

# max_number(2,5,7)

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

def min_and_max_numbers(*args):
    print('max value: ', max(args))
    return min(args)

# print('min value: ', min_and_max_numbers(2,5,7))

# - створити функцію яка виводить ліст

def new_list(list_args):
    print(*list_args, ' ')

#new_list([2,54,655,757,344])

# - створити функцію яка повертає найбільше число з ліста

def max_value_from_list(list_args):
    return max(list_args)

# print(max_value_from_list([23,45,67,234]))

# - створити функцію яка повертає найменьше число з ліста

def min_value_from_list(list_args):
    return min(list_args)

# print(min_value_from_list([23,45,67,234]))

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

def sum_of_list_values(list_args):
    return sum(list_args)

# print(sum_of_list_values([2,5,7,2]))

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

def average_value_from_list(list_args):
    return sum(list_args) / len(list_args)

# print(average_value_from_list([2.2,5,7,2.2]))

#   Приклад
#   [1,2,3,4]
#   [2,3,4,5]
#   результат
#   [3,5,7,9]
   
# -функція: 
#  написати декоратор який замінює нижні підчеркування на пробіли і повертає це значення

def decorator(func):
    def wrapper():
        return func().replace('_', ' ')
    return wrapper

@decorator
def pr():
    return 'Hello_boss_!!!'

print(pr())

