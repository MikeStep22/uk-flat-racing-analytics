"""
group1_winners.py

Reads completed 2026 UK Group 1 flat race results from Data/group1_results_2026.csv
and prints which winners started as the betting favourite.

Why a separate CSV file instead of typing the data into this script?
Because the data changes (a new Group 1 gets run roughly every week or two
through October) but the logic below it doesn't. Keeping them apart means
updating results is just editing a spreadsheet-like file, never the code.

How to get this up to date when new Group 1s have been run:
  Ask Claude, e.g. "check thestatsdontlie.com's Group 1 page for any UK
  Group 1 races completed since <date> and add them to
  Data/group1_results_2026.csv" — Claude can look the results up and
  append rows for you. Or add a race yourself without hand-editing the
  file: run add_race.py and answer its prompts, or call add_race()
  directly from your own code. Then just re-run this script; nothing
  else needs to change.
"""

import csv
from pathlib import Path

DATA_FILE = Path(__file__).parent / "Data" / "group1_results_2026.csv"
FIELDNAMES = ["date", "course", "race", "winner", "sp", "favourite", "distance", "going", "runners"]


def load_results(path=DATA_FILE):
    """Read the CSV into a list of dictionaries, one per race."""
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        races = list(reader)
    # The CSV stores "True"/"False" as plain text; convert to a real boolean.
    for race in races:
        race["favourite"] = race["favourite"] == "True"
    return races


def add_race(date, course, race, winner, sp, favourite,
             distance="", going="", runners="", path=DATA_FILE):
    """
    Append one new race to the CSV without hand-editing it.

    Example:
        add_race("2026-10-03", "Newmarket", "Sun Chariot Stakes",
                  "Some Horse", "7/2", False)

    `favourite` should be a real True/False, not the string "True"/"False".
    distance/going/runners are the month-3 placeholder columns — leave
    them blank for now unless you already know the values.
    """
    new_row = {
        "date": date,
        "course": course,
        "race": race,
        "winner": winner,
        "sp": sp,
        "favourite": str(bool(favourite)),  # stored as text, same convention as the rest of the file
        "distance": distance,
        "going": going,
        "runners": runners,
    }
    with open(path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow(new_row)
    print(f"Added: {date}  {race} — {winner} ({sp})")


group1_results_2026 = load_results()

if __name__ == "__main__":
    print(f"{len(group1_results_2026)} completed Group 1 races for 2026 to date "
          f"(from {DATA_FILE.name})\n")

    # --- Print every race, marking which winners started favourite ---
    print("All results:")
    for race in group1_results_2026:
        tag = "FAVOURITE" if race["favourite"] else "not favourite"
        print(f"  {race['date']}  {race['race']:<38} {race['winner']:<17} ({race['sp']:>6})  — {tag}")

    # --- Now just the ones that started favourite ---
    favourites_that_won = [r for r in group1_results_2026 if r["favourite"]]

    print(f"\nWinners that started as favourite ({len(favourites_that_won)} of {len(group1_results_2026)}):")
    for race in favourites_that_won:
        print(f"  {race['winner']} won the {race['race']} at {race['sp']}")

    # --- The headline stat ---
    share = len(favourites_that_won) / len(group1_results_2026) * 100
    print(f"\nFavourites have won {share:.0f}% of this season's Group 1 races so far "
          f"({len(favourites_that_won)}/{len(group1_results_2026)}).")
