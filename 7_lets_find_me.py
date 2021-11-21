import random
def list_random(range_list=10):  # создание списк рандомных наутральных чисел
    i = 1
    l = []
    while i <= range_list:
        l.append(random.randint(0, 9))
        i = i + 1
    return l
def find_me(find_num, range=10):  # поиск числа в списке и вывод его индекса
    l = list_random(range)
    print(l)
    for i in l:
        if i == find_num:
            return l.index(i)
    return False
range = int(input('Input range of list: '))
x = int(input('Input number to find in list: '))
list_of_random_numbers = (list_random(range))
find = find_me(x, range)
if find != False:
    print('First entry of number', x, 'into the list', find)
else:
    print('Number', x, 'not found in the list')