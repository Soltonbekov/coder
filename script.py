# coding: utf-8


def fizz_buzz(number):
    """
    Функция принимает int.
    Возвращает:
    * Fizz если параметр делится на 3
    * Buzz если параметр делится на 5
    * FizzBuzz если параметр делится и на 3 и на 5
    """
    if number <= 0:
        return 'SmallInt'
    
    if number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'