for i in range(1, 21):
    if i % 2 == 0 or sum(map(int, str(i))) % 2 == 0:
        print(i**2, 'квадрат числа', i)
    else:
        print(i**3, 'куб числа', i)

# def sum_digits(i):
#     x = 0
#     while i > 0:
#         x += i % 10
#         i = i // 10
#     return x
#
#
# for i in range(1, 21):
#     if i % 2 == 0 or sum_digits(i) % 2 == 0:
#         print(i ** 2, 'квадрат числа', i)
#     else:
#         print(i ** 3, 'куб числа', i)
