
def mod_exp(x, y, m):
    if y == 0:
        # print(x,y)
        return 1
    else:
        z = mod_exp(x, int(y/2), m)
        # print(x, y, z)
        if y % 2 == 0:
            return (z * z) % m
        else:
            return (x * z * z) % m


def print_mod_exp(x, y, m):
    print(x, '^', y, 'mod(', m, ') =',
          mod_exp(x, y, m))


def extended_gcd(x, y):
    if y == 0:
        return x, 1, 0
    else:
        (d, a, b) = extended_gcd(y, x % y)
        return d, b, a - int(x / y) * b


def print_gcd(x, y):
    (d, a, b) = extended_gcd(x, y)
    print('Greatest common divisor of: ',
          x, 'and', y, 'is', d, '\nand it can be written as: ',
          a, '*', x, '+', b, '*', y)

# 2a)
# a_range = range(0, 100)
#
# for a in a_range:
#     print(a, ': ')
#
#     x = 7*a + 3
#     y = 5*a + 2
#     print_gcd(x, y)
#     print('--------------')

# 2b)
# x = 3
# y = 48
# m = 11
#
# print_mod_exp(x, y, m)
# print()

# 2c)
# x_range = range(0, 100)
# for x in x_range:
#
#     print(x, ':')
#     print(x % 4 == 1 or x % 4 == 2)
#     print((x**2 + x) % 4)
#     print('--------------')


# 2d)
# x_range = range(0, 1000)
# m = 7
# for x in x_range:
#     # print(x, ':')
#     # print(3 * (mod_exp(x, 12, 7)) + 5 * (mod_exp(x, 2, 7)) == 0)
#     # print('--------------')
#     if 3 * (mod_exp(x, 12, 7)) + 5 * (mod_exp(x, 7, 7)) - 6 == 0:
#         print(x, ':')
#         for i in range(1,8):
#             print(x, '%', i, '=', x%i)
#         print('-----------')

# 2e)

