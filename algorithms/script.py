# -*- coding: utf-8 -*-

def get_min_value(numbers):
    """
    Returns int, which has minimal value in list.
    """
    min_number = numbers[0]
    for i in numbers:
        if i < min_number:
            min_number = i
    return min_number


def get_max_value(numbers):
    """
    Returns int, which is max value in the list.
    """
    max_number = numbers[0]
    for n in numbers:
        if n > max_number:
            max_number = n
    return max_number


def get_max_value_index(numbers):
    """
    Returns int, which is index of max value of the list.
    """
    max_index = 0
    max_number = numbers[0]
    for i,j in enumerate(numbers):
        if j > max_number:
            max_number = j
            max_index = i
    return max_index


def sort_desc(numbers):
    """
    Returns list sorted descending.
    """
    sorted_list = []
    for i in range(len(numbers)):
        sorted_list.append(numbers.pop(get_max_value_index(numbers)))
    return sorted_list


def get_min_value_index(numbers):
    """
    Returns int, which is index of minimal value of the list.
    """
    min_number = numbers[0]
    counter = 0
    for i in numbers:
        if i < min_number:
            min_number = i
            counter += 1
    return counter


def sort_asc(numbers):
    """
    Returns list sorted ascending.
    """
    sorted_list = []
    for i in range(len(numbers)):
        sorted_list.append(numbers.pop(get_min_value_index(numbers)))
    return sorted_list

# if __name__ == '__main__':
#     print sort_desc([456,123,987,543])
