def get_grade(score):
    if 0 <= score <= 100:
        if score >= 71:
            return "A"
        elif score >= 51:
            return "B"
        elif score >= 31:
            return "C"
        elif score >= 30:
            return "D"
        else:
            return "F"
    else:
        return "Unrecognized marks"

try:
    score = float(input("Enter your score: "))
    grade = get_grade(score)
    print("Your grade is:", grade)

except ValueError:
    print("Invalid input. Please enter a numeric score.")
