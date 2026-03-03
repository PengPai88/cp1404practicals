
numbers = []
for i in range(5):
    number = int(input(f"   Number: "))
    numbers.append(number)

print(f"   The first number is {numbers[0]}")
print(f"   The last number is {numbers[-1]}")
print(f"   The smallest number is {min(numbers)}")
print(f"   The largest number is {max(numbers)}")
print(f"   The average of the numbers is {sum(numbers)/len(numbers):.1f}")


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
             'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
             'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter your username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")


numbers_extended = []
count = 1
while True:
    try:
        number = int(input(f"Number {count}: "))
        if number < 0:
            break
        numbers_extended.append(number)
        count += 1
    except ValueError:
        print("Please enter a valid integer.")

if numbers_extended:
    print(f"First number: {numbers_extended[0]}")
    print(f"Last number: {numbers_extended[-1]}")
    print(f"Average: {sum(numbers_extended)/len(numbers_extended):.1f}")