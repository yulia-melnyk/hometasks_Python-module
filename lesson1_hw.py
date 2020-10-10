# 1)Дан лист:
values = [22, 3,5,2,8,2,-123, 8,23,5]

#   - найти min число в листе
def task1_1(values):
    min_val = values[0]
    for item in values:
        if min_val > item:
            min_val = item
    return min_val

# task1_1_1(values)
#   - удалить все одинаковые значения

def task1_2(values):
    return list(set(values))

#   - заменить каждое четвертое значение на "Х"
def task1_3(values):
    index=3
    while(index < len(values)):
        values[index] = 'X'
        index += 4
    return values

# вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа
# пример:
# [1, 2, 3, 4, 5, 6, 7, 8, 9] => 5
# [-1, -2, 3, 4, 555] => 4
# [5, 5, 5, 5] => 5
# [-10, 5, 5] => 5
# P. S. Функция len() также используется для листов

def task1_4(values):
    avg = sum(values) / len(values)
    diff_list =[]
    for item in values:
        diff_list.append(abs(item - avg))
    min_diff = min(diff_list)
    result_index = diff_list.index(min_diff)
    return values[result_index]


# print(task1_4(values))
  
# # 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:
def task2():
    print('task2')
# # 3) переделать первое задание под меню с помощью цикла

def task3():
    while True:
        print(''''Choose task:
        1 - Task 1
        2 - Task 2
        3 - Task 3
        4 - Task 4
        ''')
        choice = int(input('Enter the number:'))
        if choice == 1:
            print(task1_1(values))
        elif choice == 2:
            print(task1_2(values))
        elif choice == 3:
            print(task1_3(values))
        elif choice == 4:
            print(task1_4(values))
        else:
            break

# # 4) вывести табличку умножения с помощью цикла while
def task4():
    for i in range(1,10):
        for j in range(1,10):
            if (i*j) // 10 != 0:
                print(i*j, end=' ')
            else:
                print(i*j, end='  ')
        print()
task3()