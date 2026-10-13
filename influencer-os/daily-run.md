# Daily run

1. Script loads Ali's Google Sheet (all tabs) and data/seen.csv, scrapes, filters numbers in code, writes data/daily/raw-YYYY-MM-DD.csv.
2. Claude reads commands.md, criteria.md, scoring.md and the raw CSV only.
3. Remove duplicates again (Sheet + seen.csv).
4. Apply hard gates, then score all remaining creators in ONE batch (free-API first pass allowed, see tokens.md).
5. Keep the best 110-120 following the country mix in commands.md: qualified first, "maybe" only to fill.
6. Write data/daily/YYYY-MM-DD.csv and data/daily/sheet-paste-YYYY-MM-DD.csv.
7. Append every output handle to data/seen.csv.
8. Short summary to Ali: counts, country mix, engagement threshold used, top 5, problems.
9. One line to log.md if anything broke or changed.

## Keep usage low
No browsing during scoring. Fresh session each run. Read only the files above. Cheaper model for daily scoring; stronger model only to fix scripts.
