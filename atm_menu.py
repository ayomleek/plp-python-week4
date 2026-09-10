"""
atm_menu.py

A tiny simulated ATM.

    1. Ask for a 4-digit PIN.
    2. Wrong PIN -> print an error and stop.
    3. Correct PIN -> ask for a withdrawal amount.
    4. Inside that decision: withdraw if funds allow it,
       otherwise report insufficient funds.
"""

CORRECT_PIN = "4321"   # change this to whatever PIN you want
balance = 1000          # starting balance


def get_pin():
    """Ask for a 4-digit PIN, re-prompting until the format is correct."""
    while True:
        pin = input("Enter your 4-digit PIN: ").strip()
        if pin.isdigit() and len(pin) == 4:
            return pin
        print("A PIN must be exactly 4 digits. Please try again.\n")


def get_withdrawal_amount():
    """Ask for a withdrawal amount, re-prompting until it's a positive number."""
    while True:
        raw_value = input("Enter the amount you want to withdraw: ").strip()
        try:
            amount = float(raw_value)
        except ValueError:
            print(f'"{raw_value}" is not a valid amount. Please try again.\n')
            continue

        if amount <= 0:
            print("Please enter an amount greater than 0.\n")
            continue

        return amount


def main():
    global balance

    pin = get_pin()

    # Decision 1: is the PIN correct?
    if pin != CORRECT_PIN:
        print("Incorrect PIN")
        return  # stop the program right here

    print("PIN accepted.\n")
    amount = get_withdrawal_amount()

    # Decision 2 (nested inside the "PIN correct" branch):
    # can the account actually afford this withdrawal?
    if amount <= balance:
        balance -= amount
        print(f"Withdrawal successful. New balance: {balance:.2f}")
    else:
        print("Insufficient funds")


if __name__ == "__main__":
    main()