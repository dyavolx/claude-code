# Log
(date: what ran, what broke, what was fixed)
2026-10-13: installed skills (scrapling, agent-reach, caveman, ponytail, awesome-claude-skills, graphify), added orchestrator skill and data/delivered.csv
2026-10-13: 10-creator run found 0 qualified. IG blocks anonymous access (302 login wall / 401 API); VidIQ has no country; web search weak. Used ~80 of 150 VidIQ credits.
2026-10-13: parents-only retry (EU+UK): 0 found. 4 multilingual web searches + 1 VidIQ outlier search returned US parent-basketball accounts only; only EU/UK parent hit (olacurtis.uk) is soccer, not basketball. Need IG login scraper or Ali-supplied handles.
2026-10-13: IG login OK (code step needed once). Hashtag run: 5 EN tags -> 135 new candidates, almost all US/AU/shops. Profile API returns 429 even at 8-14s pacing (stopped after 3). Checked 8 likely-EU via VidIQ: 0 qualify (AU, US, club/page, empty, UK sports-mum w/o basketball). Next: local-language tags, wait for throttle to clear.
2026-10-13: #basketmamma (SE/NO) tag works. Verified 22 profiles by page view (ig_verify.py): 1 qualifies. Rest: personal accounts with one-off basketball hashtag, or inactive >90d.
