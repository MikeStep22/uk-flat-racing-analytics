# UK Flat Racing Ontology Project

A 6-month learning project: vibe coding, semantic web (RDF/OWL/SPARQL), and
ontology-based data analytics, applied to UK Group 1 flat racing — working
towards a backtested prediction model by the end of month 6.

Full background and the month-by-month plan live in
`UK-Flat-Racing-Ontology-Project-Plan.docx` (and the matching `.md`).

## What's here

| File | What it does |
|---|---|
| `Data/group1_results_2026.csv` | The dataset — every completed 2026 UK Group 1 flat race, with winner, starting price, and favourite status. `distance`, `going`, and `runners` columns exist as placeholders for month 3. |
| `group1_winners.py` | Reads the CSV and prints every race, which winners started favourite, and the season's favourites-win percentage so far. |
| `group1_upsets.py` | Same data, but prints only the races where the favourite *didn't* win. |
| `add_race.py` | Run this to add a new completed race to the CSV by answering a few prompts — no hand-editing the file required. |
| `UK-Flat-Racing-Month1-Checklist.xlsx` / `Month2-Checklist.xlsx` | Detailed task checklists for months 1 and 2. |
| `UK-Flat-Racing-Architecture.pptx` | Print-ready wall diagram of the project's toolbox and pipeline, plus a glossary. |

## How to run it

1. Open this folder in VS Code.
2. Open a terminal (Terminal → New Terminal).
3. Run:
   ```
   python group1_winners.py
   ```
   or, for just the upsets:
   ```
   python group1_upsets.py
   ```

## Keeping the data current

Two ways to add a newly completed Group 1 race:

- **Ask Claude** — e.g. "check thestatsdontlie.com's Group 1 page for any UK Group 1 races completed since \<date\> and add them to Data/group1_results_2026.csv."
- **Run it yourself** — `python add_race.py` and answer the prompts.

Either way, nothing in `group1_winners.py` or `group1_upsets.py` needs to change — they just re-read the CSV next time they run.

## Where the data comes from

Results and starting prices are sourced from
[thestatsdontlie.com's 2026 Group 1 schedule/results page](https://www.thestatsdontlie.com/horse-racing/flat/group-1/),
spot-checked against individual race reports.

## Project status

Month 1 complete — see the decisions log in the project plan doc for the
reasoning behind key choices made along the way (Timeform Timefigures as
the model's time-adjusted feature, the Class 1–6 correction, keeping the
ontology's `hasGoing` as a simple property for now, and keeping the
dataset 2026-only until month 3's proper ETL pipeline).
