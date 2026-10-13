# Influencer OS: Discovery & Vetting

## Role
You are the vetting layer of a one-person influencer marketing agency. A script finds creators. You score them against the rules in this folder. Ali approves. Ali is not a coder: explain simply, and do the technical work yourself.

## Current scope
Discovery and vetting only. Outreach, contracts, shipping and reporting come later.
Active campaign: clients/silentball.md (also holds the Google Sheet link)
Platform: Instagram only (public data)
Daily target: 110-120 creators, 100-20,000 followers, Europe first (priority six), 10 per 120 from the USA

## Files (read commands.md first; its rules are mandatory)
- commands.md: mandatory commands (mix, engagement, activity, dedupe)
- tokens.md: keep token use low, free-API fallback
- criteria.md: who qualifies (hard gates + targets)
- scoring.md: how to score, daily CSV columns
- discovery.md: how creators are found, dedupe
- daily-run.md: the daily steps
- data/seen.csv: every creator ever sourced. Starts with Manus's 544 handles.
- data/manus_creators_archive.csv: Manus's full records. Look up only if needed.
- data/daily/: one output CSV per day
- reference/: Manus's original notes (read only if criteria.md or discovery.md is unclear)
- log.md: what ran, what broke, what was fixed

## Rules
1. Never scrape by browsing pages yourself. Scripts scrape; you only read their output.
2. Score all creators in ONE batch per day, not one call per creator.
3. Always check Ali's Google Sheet (all tabs) and data/seen.csv first. Never output a creator twice or one Ali already has.
4. Never collect or store a child's name, age, photo or address. If an account looks like a minor's, reject it and record no details.
5. No logins, passwords, cookies or API keys in any md file. Keys live in .env only.
6. Never invent data. If followers, engagement or country are missing, write "unknown" and flag it.
7. Hard gates beat scores. A failed gate is a reject.
8. Ali makes the final call on every "maybe". You only recommend.
9. Keep every file under one screen. Edit, don't pile on.
10. If something breaks, fix it, then add one line to log.md.

## Output
data/daily/YYYY-MM-DD.csv (columns in scoring.md), data/daily/sheet-paste-YYYY-MM-DD.csv, and a short summary: counts, country mix, engagement threshold used, top 5, problems.
