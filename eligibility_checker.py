"""
eligibility_checker.py

Decides whether someone can join the local coding club.

Club rules:
    * You must be 13 or older.
    * If you are under 18, you also need parental consent.
    * Anyone 18 or older does not need consent at all.
"""


def get_age():
    """Ask for the applicant's age and keep asking until it's a valid whole number."""
    while True:
        raw_value = input("Enter your age: ").strip()
        try:
            age = int(raw_value)
        except ValueError:
            print(f'"{raw_value}" is not a whole number. Please try again.\n')
            continue

        # Age validation - reject impossible ages instead of trusting the input blindly.
        if age < 0 or age > 120:
            print("Please enter a realistic age (0-120).\n")
            continue

        return age


def get_consent():
    """Ask a yes/no question and keep asking until the answer is clearly yes or no."""
    while True:
        answer = input("Do you have parental consent? (yes/no): ").strip().lower()
        if answer in ("yes", "y"):
            return True
        elif answer in ("no", "n"):
            return False
        else:
            print('Please answer "yes" or "no".\n')


def check_eligibility(age, has_consent):
    """Work out whether the applicant is eligible, using and / or / not."""

    # An adult (18+) never needs consent, so they are automatically fine here.
    is_adult = age >= 18

    # A minor (under 18) is only fine if they are old enough (13+) AND have consent.
    is_eligible_minor = age >= 13 and has_consent

    # The applicant is eligible if they are an adult, OR they are an eligible minor.
    eligible = is_adult or is_eligible_minor

    # A shorter way to phrase "too young to ever join, regardless of consent":
    # not (age >= 13) means the age rule alone already rules them out.
    too_young = not (age >= 13)

    return eligible, too_young


def main():
    age = get_age()

    has_consent = False
    if age < 18:
        # Consent only matters for people who are not yet adults.
        has_consent = get_consent()

    eligible, too_young = check_eligibility(age, has_consent)

    if too_young:
        print("Sorry, you are not eligible yet.")
    elif eligible:
        print("Welcome to the club!")
    else:
        print("Sorry, you are not eligible yet.")


if __name__ == "__main__":
    main()