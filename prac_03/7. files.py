
name = input("Enter your name: ")
out_file = open("name.txt", 'w')
out_file.write(name)
out_file.close()


in_file = open("name.txt", 'r')
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")


with open("numbers.txt", 'r') as in_file:
    num1 = int(in_file.readline())
    num2 = int(in_file.readline())
    print(num1 + num2)


total = 0
with open("numbers.txt", 'r') as in_file:
    for line in in_file:
        total += int(line.strip())
print(total)