"""
group1_upsets.py

Every completed 2026 UK Group 1 flat race where the betting favourite
did NOT win, drawn from the same results as group1_winners.py.

Source: thestatsdontlie.com's 2026 Group 1 schedule/results page, cross-
checked against individual race reports for the four York races the page
still had listed as "upcoming" (they'd actually already run).
As of: 23 August 2026 — the season continues through October, so this
percentage will keep moving as more Group 1s are run.
"""

from group1_winners import group1_results_2026

upsets = [r for r in group1_results_2026 if not r["favourite"]]

print(f"{len(upsets)} of {len(group1_results_2026)} completed Group 1 races in 2026 "
      f"were won by a non-favourite\n")

print("Races where the favourite didn't win:")
for race in upsets:
    print(f"  {race['date']}  {race['race']:<38} {race['winner']:<17} ({race['sp']:>6})")

share = len(upsets) / len(group1_results_2026) * 100
print(f"\nNon-favourites have won {share:.0f}% of this season's Group 1 races so far "
      f"({len(upsets)}/{len(group1_results_2026)}).")
