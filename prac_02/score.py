import random
def main():

    score = float(input("Enter score: "))
    result = determine_result(score)
    print(f"User score {score} is {result}")

    if result == "Excellent":
        print("You get a prize!")

    random_score = random.randint(0, 100)
    random_result = determine_result(random_score)
    print(f"Random: {random_score} = {random_result}")


def determine_result(score):

    if score < 0 or score > 100:
        return "Invalid"
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Passable"
    return "Bad"

main()
