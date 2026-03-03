import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

def main():
    number_of_picks = int(input("How many quick picks? "))
    for _ in range(number_of_picks):
        quick_pick = []
        while len(quick_pick) < NUMBERS_PER_PICK:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            if number not in quick_pick:
                quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{num:2}" for num in quick_pick))

if __name__ == "__main__":
    main()
