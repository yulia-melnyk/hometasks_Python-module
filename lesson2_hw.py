
# 1) написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

str_initial = input('Enter the value: ')
str_digits_separated = ''

for digit in str_initial:
    if digit.isdecimal():
        str_digits_separated += digit
str_digits_separated = ', '.join(str_digits_separated)
# print(str_digits_separated)

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх 
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

str_initial1 = input('Enter the value: ')
str_only_digits = ''

for digit in str_initial1:
    if digit.isdecimal():
        str_only_digits += digit
str_only_digits = ' '.join(str_only_digits)
# print(str_only_digits)


# #################################################################################
# 3)прога, що виводить кількість кожного символа з введеної строки,
# наприклад:
# st = 'as 23 fdfdg544' #введена строка

# 'a' -> 1  #вивело в консолі
# 's' -> 1
# ' ' -> 2
# '2' -> 1
# '3' -> 1
# 'f' -> 2
# 'd' -> 2
# 'g' -> 1
# '5' -> 1
# '4' -> 2
# """

str_some_text = input('Print some text: ')

for symbol in str_some_text:
    symbols_total = str_some_text.count(symbol)
    if symbols_total:
        print(f" '{symbol}' -> {symbols_total}")
        str_some_text = str_some_text.replace(symbol, '')

# 1)есть строка:
greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

greeting_list = [ letter.upper() for letter in greeting]
print(greeting_list)


# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

range_of_numbers = [number ** 2 for number in range(50) if number % 2 != 0]
print(range_of_numbers)

# 3)  есть лист:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# создать новый лист и записать в него 'GT' если элемент в numbers больше 4 и 'LT' если элемент меньше или равен 4
# пример:
# ['LT', 'LT', 'LT', 'LT', 'GT', 'GT', 'GT', 'GT']

gt_lt_list  = ['GT' if number > 4 else 'LT' for number in numbers]
print(gt_lt_list)

# 4) есть два листа:
list1 = [1, 2, 3, 4, 5]
list2 = [-1, 7, 10, -5, -2]

# записать в лист тюплы (x,y) если x+y == 0
# пример:
# [(1, -1), (2, -2), (5, -5)]

tuples_list = [(x, y) for x in list1 for y in list2 if x + y == 0]
print(tuples_list)

