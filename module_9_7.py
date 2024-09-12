
def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 2:
            print("Составное")
        else:
            is_prime = True
            for i in range(2, int(result**0.5) + 1):
                if result % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print("Простое")
            else:
                print("Составное")
        return result
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)















# def null_decorator(func):
#     return func
#
#
# def greet():
#     return "Привет"
#
# greet = null_decorator(greet)
#
# print(greet())



# def null_decorator(func):
#     return func
#
#
# @null_decorator
# def greet():
#     return "Привет"
#
# print(greet())



# def uppercase(func):
#     def wrapper():
#         original_result = func()
#         modified_result = original_result.upper()
#         return modified_result
#     return wrapper
#
#
#
# @uppercase
# def greet():
#     return "Hello"
#
# print(greet())



# import time
# import sys
#
#
# def time_track(func):  # Функция подсчитывает затраченное время
#     def surrogate(*args, **kwargs):
#         started_at = time.time()
#
#         result = func(*args, **kwargs)
#
#         ended_at = time.time()
#         elapsed = round(ended_at - started_at, 4)
#         print(f'Функция работает {elapsed} секунд(ы)')
#         return result
#     return surrogate
#
#
# @time_track  # Умножает и подсчитывает количество символов строки
# def digits(*args):
#     total = 1
#     for number in args:
#         total *= number ** 5000
#     return len(str(total)), total

#
# sys.set_int_max_str_digits(100000)
#
# result = digits(3141,5926,2718, 2818)
# print(result)


















