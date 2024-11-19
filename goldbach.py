import math


def get_circle_area(radius):
    area = math.pi * radius ** 2
    return area


def is_prime(value):
    result = False
    if value == 2:
        return True
    else:
        for num in range(2, value):
            if value % num == 0:
                result = False
                break
            else:
                result = True
    return result


def get_primes(value):
    my_list = []
    for num in range(2, value):
        if is_prime(num):
            my_list.append(num)
    return my_list


def goldbach_conjeture(value):
    primes_list = get_primes(value)
    goldbach_list = []
    for num1 in primes_list:
        for num2 in primes_list:
            if num1 + num2 == value:
                goldbach_list.append([num1, num2])
    return goldbach_list


value = 10
print(is_prime(value))
print(get_primes(value))
print(goldbach_conjeture(value))
