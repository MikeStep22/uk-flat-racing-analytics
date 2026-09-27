"""
group1_winners.py

Every completed 2026 UK Group 1 flat race, with the winner's starting
price and whether that winner was the betting favourite.

Source: thestatsdontlie.com's 2026 Group 1 schedule/results page, cross-
checked against individual race reports for the four York races the page
still had listed as "upcoming" (they'd actually already run).
As of: 23 August 2026 — the season continues through October, so this
percentage will keep moving as more Group 1s are run.
"""

group1_results_2026 = [
    {"race": "2000 Guineas",                       "course": "Newmarket", "date": "2026-05-02", "winner": "Bow Echo",           "sp": "9/2",   "favourite": False},
    {"race": "1000 Guineas",                       "course": "Newmarket", "date": "2026-05-03", "winner": "True Love",          "sp": "5/1",   "favourite": False},
    {"race": "Lockinge Stakes",                    "course": "Newbury",   "date": "2026-05-16", "winner": "Notable Speech",     "sp": "2/1F",  "favourite": True},
    {"race": "Oaks Stakes",                        "course": "Epsom",     "date": "2026-06-05", "winner": "Thundering On",      "sp": "5/1",   "favourite": False},
    {"race": "Coronation Cup",                     "course": "Epsom",     "date": "2026-06-06", "winner": "Bay City Roller",    "sp": "17/2",  "favourite": False},
    {"race": "Derby Stakes",                       "course": "Epsom",     "date": "2026-06-06", "winner": "Christmas Day",      "sp": "7/1",   "favourite": False},
    {"race": "Queen Anne Stakes",                  "course": "Ascot",     "date": "2026-06-16", "winner": "Ten Bob Tony",       "sp": "50/1",  "favourite": False},
    {"race": "King Charles III Stakes",            "course": "Ascot",     "date": "2026-06-16", "winner": "Mission Central",    "sp": "14/1",  "favourite": False},
    {"race": "St James's Palace Stakes",           "course": "Ascot",     "date": "2026-06-16", "winner": "Bow Echo",           "sp": "5/6F",  "favourite": True},
    {"race": "Prince of Wales's Stakes",           "course": "Ascot",     "date": "2026-06-17", "winner": "Ombudsman",          "sp": "11/10F","favourite": True},
    {"race": "Gold Cup",                           "course": "Ascot",     "date": "2026-06-18", "winner": "Scandinavia",        "sp": "11/8F", "favourite": True},
    {"race": "Commonwealth Cup",                   "course": "Ascot",     "date": "2026-06-19", "winner": "Venetian Sun",       "sp": "11/8F", "favourite": True},
    {"race": "Coronation Stakes",                  "course": "Ascot",     "date": "2026-06-19", "winner": "Precise",            "sp": "8/13F", "favourite": True},
    {"race": "Queen Elizabeth II Jubilee Stakes",  "course": "Ascot",     "date": "2026-06-20", "winner": "Almeraq",            "sp": "25/1",  "favourite": False},
    {"race": "Eclipse Stakes",                     "course": "Sandown",   "date": "2026-07-04", "winner": "Constitution River", "sp": "8/11F", "favourite": True},
    {"race": "Falmouth Stakes",                    "course": "Newmarket", "date": "2026-07-10", "winner": "Blue Bolt",          "sp": "85/40", "favourite": False},
    {"race": "July Cup",                           "course": "Newmarket", "date": "2026-07-11", "winner": "Comanche Brave",     "sp": "11/1",  "favourite": False},
    {"race": "King George VI & Queen Elizabeth Stakes", "course": "Ascot","date": "2026-07-25", "winner": "Kalpana",            "sp": "13/2",  "favourite": False},
    {"race": "Goodwood Cup",                       "course": "Goodwood",  "date": "2026-07-28", "winner": "Scandinavia",        "sp": "6/5F",  "favourite": True},
    {"race": "Sussex Stakes",                      "course": "Goodwood",  "date": "2026-07-29", "winner": "Bow Echo",           "sp": "10/11F","favourite": True},
    {"race": "Nassau Stakes",                      "course": "Goodwood",  "date": "2026-07-30", "winner": "Diamond Necklace",   "sp": "4/6F",  "favourite": True},
    {"race": "International Stakes",               "course": "York",      "date": "2026-08-19", "winner": "Item",               "sp": "10/1",  "favourite": False},
    {"race": "Yorkshire Oaks",                     "course": "York",      "date": "2026-08-20", "winner": "Kalpana",            "sp": "10/11F","favourite": True},
    {"race": "Nunthorpe Stakes",                   "course": "York",      "date": "2026-08-21", "winner": "Bacio",              "sp": "3/1",   "favourite": True},
    {"race": "City of York Stakes",                "course": "York",      "date": "2026-08-22", "winner": "Notable Speech",     "sp": "9/4",   "favourite": True},
]

print(f"{len(group1_results_2026)} completed Group 1 races for 2026 to date\n")

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
