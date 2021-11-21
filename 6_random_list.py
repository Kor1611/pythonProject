import random


def list_random(range_list=10):
    i = 1
    l = []
    while i <= range_list:
        l.append(random.randint(0, 9))
        i = i + 1
    return l


list_of_random_numbers = (list_random())
print(list_of_random_numbers)
print('Total number of list: ', len(list_of_random_numbers))
