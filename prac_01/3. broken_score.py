def determine_score_status(score):
    if score < 0 or score > 100:
        return "invalid score"
    elif score >= 90:
        return "excellent"
    elif score >= 50:
        return "passable"
    else:
        return "bad"

def main():
    score = float(input("Enter score: "))
    status = determine_score_status(score)
    print(status)

if __name__ == "__main__":
    main()