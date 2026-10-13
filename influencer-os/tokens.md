# Token saving

Order of work, cheapest first:
1. Code (free): scraping, dedupe, numeric filters (followers, posts/reels count, recency, engagement, country).
2. Free-tier LLM API (fallback, first pass only): scores borderline creators in ONE batch when Claude usage is low. It never makes final calls alone.
3. Claude Sonnet: final check of top picks and "maybe" rows, and fixing broken scripts.
4. Claude Opus: only for hard debugging.

Rules
- Send LLMs only compact public fields: handle, followers, engagement, posts/reels count, bio text, 3 recent captions. Never children's details, never Ali's private data.
- API keys live in a .env file (already in .gitignore). Never put keys in md files, chats or scripts.
- Provider config lives in scripts/llm_config (provider, model, daily limit). If a provider hits its limit or errors, move to the next. Log which one was used in log.md.
- Free tiers have rate limits, and some terms allow training on inputs. Check each provider's terms. Public creator fields only.
- Quality check: after any switch to a free model, Claude spot-checks 10 random rows before the file is accepted.
- Savers: batch calls, compact CSV, fresh session each run, no re-reading folders, cache results so the same creator is never scored twice.
- Any GitHub repo or skill added to cut tokens: Claude reads the code first, checks for calls to unknown servers and install scripts, then installs it in a virtual environment.
