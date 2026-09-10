"""
grade_classifier.py

Asks the user for an exam score and reports the letter grade.

Grading scale:
    A : 80 - 100
    B : 70 - 79
    C : 60 - 69
    D : 50 - 59
    F : below 50

Any score outside the valid 0-100 range is rejected before grading.
"""


def get_score():
    """Prompt the user for a score and safely convert it to an int.

    Keeps asking until the user types something that can actually be
    turned into a whole number, so the program never crashes on bad
    input like letters or blank text.
    """
    while True:
        raw_value = input("Enter a score between 0 and 100: ").strip()
        try:
            return int(raw_value)
        except ValueError:
            print(f'"{raw_value}" is not a whole number. Please try again.\n')


def classify_grade(score):
    """Return the letter grade for a score that is already known to be 0-100."""
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


def main():
    score = get_score()

    # Step 1: validate the score BEFORE trying to grade it.
    if score < 0 or score > 100:
        print(f"Error: {score} is not a valid score. Please enter a value from 0 to 100.")
        return  # stop here - an out-of-range score is never graded

    # Step 2: the score is valid, so work out the grade.
    grade = classify_grade(score)
    print(f"A score of {score} earns grade: {grade}")


if __name__ == "__main__":
    main()