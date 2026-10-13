# Discovery

Goal: 110-120 NEW creators a day under the rules in commands.md. Qualified first; if short, fill with clearly labeled "maybe" rows. Never fill with rejects.

## Dedupe (first, every run)
Never output anyone already in:
1. Ali's Google Sheet, ALL tabs (Sheet1 rows to 945+, Sheet2, Sheet3). Link in clients/silentball.md.
2. data/seen.csv (Manus's 544 handles plus every past daily output).
Normalize handles first: lowercase, strip @, trailing slash, /reels/ or /tagged/ endings, query strings.
The script reads the Sheet at the start of each run (CSV export URL; needs "Anyone with the link: Viewer"). Fallback: Ali exports each tab to data/sheet-export/ as CSV.

## What Manus actually did
- SocialCrawl discovery while credits lasted (they ran out), then public research and third-party metric sites. Delays, login use, query logs and yield: unknown.
- A fully free Instagram scraper is UNTESTED. Run it, report what is blocked, adjust.
- Prior output: 545 records, mostly small accounts (median about 2.8K followers). Only 30 have a contact route; views and engagement almost always unknown.

## Search lanes (rotate daily, add new ones when yield drops)
- basketball parent / family, active-family, sports parent
- basketball coach / trainer, shooting coach, skills trainer, player development, youth basketball training, basketball academy, women's / beginner basketball
- Hashtags: #basketballtraining, #shootingcoach, #playerdevelopment, #basketballgermany, #baloncesto, #entrenamiento, #tecnificación
- Local-language terms for DE, ES, IT, FI, FR, PT, PL, NL; start with the priority six. Untested.
- Other sources: followers/tagged accounts of club and academy pages, comment sections of basketball pages, creator roundups.

## Script contract
Take commands.md and criteria.md, load dedupe lists, collect public profile data, filter in code (followers, posts/reels in 30 days, last post date, engagement, country), apply the country mix, stop at 120. Random delays, retry logic, no logins on personal accounts. Claude does not scrape.

## When short of 110
Widen keywords, then move from the priority six to the rest of Europe, then lower engagement in the allowed steps. Never relax the other hard gates.

## Compliance
Public data only. No children's data. Respect rate limits.
