"""
add_race.py

Interactively add one new Group 1 result to Data/group1_results_2026.csv,
so you never have to hand-edit the CSV to keep it current.

Run it with:  python add_race.py
Answer each prompt, and it appends a correctly-formatted row to the file.
"""

from group1_winners import add_race


def ask(prompt, default=""):
    value = input(f"{prompt}{f' [{default}]' if default else ''}: ").strip()
    return value or default


def ask_yes_no(prompt):
    while True:
        value = input(f"{prompt} (y/n): ").strip().lower()
        if value in ("y", "yes"):
            return True
        if value in ("n", "no"):
            return False
        print("Please answer y or n.")


if __name__ == "__main__":
    print("Add a new Group 1 result\n")

    date = ask("Date (YYYY-MM-DD)")
    course = ask("Course")
    race = ask("Race name")
    winner = ask("Winner")
    sp = ask("Starting price (e.g. 7/2 or 5/6F)")
    favourite = ask_yes_no("Did the winner start favourite?")
    distance = ask("Distance (optional, leave blank for now)")
    going = ask("Going (optional, leave blank for now)")
    runners = ask("Number of runners (optional, leave blank for now)")

    add_race(date, course, race, winner, sp, favourite, distance, going, runners)
    print("\nDone — re-run group1_winners.py to see it included.")
