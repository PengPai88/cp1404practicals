def do_it(n):
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


print(do_it(5))


def do_something(n):
    if n < 0:
        return
    print(n ** 2)
    do_something(n - 1)


do_something(4)


def calculate_pyramid_blocks(n):
    if n == 0:
        return 0
    return n + calculate_pyramid_blocks(n - 1)


print(calculate_pyramid_blocks(6))


def print_string_outside_in(s):
    if len(s) <= 1:
        if s:
            print(s, end=" ")
        return
    print(s[0], s[-1], end=" ")
    print_string_outside_in(s[1:-1])


print_string_outside_in("123456")