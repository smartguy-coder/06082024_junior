from typing import Callable

admin = {
    'login': '1',
    'password': '1234'
}

# n = 111
#
# print(id(n))
#
#
# alternative = print
#
# print(alternative)
# print(print)
#
# alternative(5555)


def log_decorator(func: Callable):
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)
        # print(func.__name__, result)
        with open('logs', mode='a', encoding='utf-8') as file:
            file.write(f'{func.__name__}{result}\n')

        return result

    return wrapper


def permission_decorator(func: Callable):
    def wrapper(*args, **kwargs):
        user_login = input('Enter login: ')
        user_password = input('Enter password: ')

        if user_login == admin['login'] and user_password == admin['password']:
            result = func(*args, **kwargs)
            return result

        print('PERMISSION DENIED')


    return wrapper


@permission_decorator
@log_decorator
def add_two_numbers(number_1: float, number_2: float) -> float:
    result = number_1 + number_2
    return float(result)



#
# add_two_numbers(5, 6)
# add_two_numbers(5, number_2=6)
# # add_two_numbers(5, number_1=6)
# add_two_numbers(number_2=5, number_1=6)
# # add_two_numbers(    **{'m':5, 'n': 6}   )

@log_decorator
def add_three_numbers(number_1: float, number_2: float, number_3: float) -> float:
    result = number_1 + number_2 + number_3
    return float(result)



# add_two_numbers = decorator(add_two_numbers)

res = add_two_numbers(555, 55555)
print(res)
add_three_numbers(2, 5, 9)

pass

# wrapper(add_two_numbers, 2.6, number_2=88)
# wrapper(add_three_numbers, 2.6, 88, number_3=0.69)
#
# add_two_numbers = wrapper(add_two_numbers)
# add_three_numbers = wrapper(add_three_numbers)

#
# res = add_two_numbers(2.5, number_2=3.6)
# res = add_three_numbers(2.5, number_2=3.6, number_3=9)
# pass
#

















