LOWER = 33
UPPER = 127


char = input("Enter a character: ")
print(f"The ASCII code for {char} is {ord(char)}")


while True:
    try:
        num = int(input(f"Enter a number between {LOWER} and {UPPER}: "))
        if LOWER <= num <= UPPER:
            print(f"The character for {num} is {chr(num)}")
            break
        else:
            print(f"Number must be between {LOWER} and {UPPER}")
    except ValueError:
        print("Please enter a valid integer.")


print("\nASCII Table:")
for i in range(LOWER, UPPER + 1):
    print(f"{i:3}  {chr(i)}")