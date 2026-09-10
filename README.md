# Grades, Eligibility & Smart Decisions

Week 4 assignment: three small Python programs that practice multi-way
decisions (`if` / `elif` / `else`), combining conditions with
`and` / `or` / `not`, input validation, and nested conditionals.

## Files

| File | Description |
|---|---|
| `grade_classifier.py` | Validates a score (0-100), then classifies it into a letter grade (A-F) using `if` / `elif` / `else`. |
| `eligibility_checker.py` | Decides whether an applicant qualifies for a coding club based on age and, where required, parental consent, using `and` / `or` / `not`. |
| `atm_menu.py` | Simulates an ATM: checks a 4-digit PIN, then nests a withdrawal decision (sufficient vs. insufficient funds) inside the "PIN correct" branch. |

## Running the programs

Each file is self-contained and runs with:

```bash
python grade_classifier.py
python eligibility_checker.py
python atm_menu.py
```

## Screenshots

The `screenshots/` folder contains run examples for each program:

* `grade_classifier` — a valid score, an invalid score, and a boundary score.
* `eligibility_checker` — an adult, a 15-year-old with consent, and a 15-year-old without consent.
* `atm_menu` — a wrong PIN, a successful withdrawal, and a withdrawal larger than the balance.

## When is `elif` better than several separate `if` statements?

`elif` is the right choice whenever the conditions are mutually exclusive
alternatives of the *same* decision — only one branch should ever run, and
once a match is found there's no reason to keep checking the rest. Using
separate `if` statements instead means Python evaluates every single
condition even after one has already matched, which is both wasteful and
risky: two "independent" `if` blocks can accidentally both fire (or a later
one can overwrite the result of an earlier one) if their conditions aren't
perfectly non-overlapping. `elif` chains make that mutual exclusivity
explicit, short-circuit as soon as a match is found, and read top-to-bottom
as one clear decision instead of several unrelated checks.