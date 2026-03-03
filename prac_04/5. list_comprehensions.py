numbers = [1, 2, 3, 4, 5]
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers)

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
first_letters = [name[0] for name in names]
print(first_letters)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

names = ["Bob", "Angel", "Jimi", "Alan", "Ada", "Steve"]
long_names = [name for name in names if len(name) > 3]
print(long_names)


squares = [num*num for num in range(10)]
print(squares)


even_numbers_0_9 = [num for num in range(10) if num % 2 == 0]
print(even_numbers_0_9)


lowercase_names = [name.lower() for name in names]
print(lowercase_names)


names_with_a = [name for name in names if 'a' in name.lower()]
print(names_with_a)