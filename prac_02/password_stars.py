

MIN_LENGTH = 8


def main():

    password = get_password()
    print_stars(password)


def get_password():

    password = input(f"Enter password (min {MIN_LENGTH} characters): ")
    while len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long.")
        password = input(f"Enter password (min {MIN_LENGTH} characters): ")
    return password


def print_stars(password):

    print('*' * len(password))


main()