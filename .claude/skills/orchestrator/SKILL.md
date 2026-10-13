---
name: orchestrator
description: Router for the influencer-os affiliate campaign. Use at the start of any task on this repo to pick the right tool - which skill saves tokens, which finds skills, which scrapes Instagram, which remembers delivered CSVs. Use when unsure which skill or tool to use.
---

# Orchestrator: which tool, when

Read this first. Pick the FIRST row that matches. Cheapest option wins. Ali is not a coder: do the technical work, explain simply.

## 1. Memory: never forget what was delivered (graphify + ledger)
| When | Use |
|---|---|
| Before ANY creator output | Check `influencer-os/data/seen.csv` AND `influencer-os/data/delivered.csv` AND Ali's Google Sheet. Never output a handle twice. |
| After giving Ali ANY csv | Append one row to `influencer-os/data/delivered.csv` (date, file, rows, purpose, notes) and the handles to `seen.csv`. Same turn, no exceptions. |
| Question about the project, past files, "what did you give me" | `graphify` skill: `graphify query/explain/path` on `graphify-out/` if it exists; otherwise read `delivered.csv` and `log.md` only. |
| After adding/changing project files | `graphify update influencer-os` (code is free, no LLM). Docs/CSVs need the full `/graphify influencer-os` pass: ask Ali first, it costs tokens. |

## 2. Scraping and discovery (Instagram creators)
| When | Use |
|---|---|
| Normal daily scraping, public IG pages, JS-rendered or blocked pages | `scrapling-official` (Scrapling): write a script in `influencer-os/scripts/`; scripts scrape, Claude reads output only. |
| Quick lookup of one profile/URL, hashtags, cross-platform research (Reddit, YouTube, TikTok-style discussions about a brand) | `agent-reach`. Run `agent-reach doctor` first; Instagram channel may need setup. |
| Finding similar/outlier IG accounts | VidIQ MCP tools (`vidiq_ig_profile`, `vidiq_ig_profile_reels`, `vidiq_ig_accounts_from_outliers`) if connected. |
| Finding lookalike brands or competitor ad angles | `competitive-ads-extractor` |
| Company/lead style research (brands, agencies) | `lead-research-assistant` |
| Vetting rules | `influencer-os/commands.md`, `criteria.md`, `scoring.md` (mandatory, read commands.md first) |

Rules: public data only, no logins/cookies in files, respect rate limits, never store anything about minors.

## 3. Token saving (use in this order)
| When | Use |
|---|---|
| Any coding/script task | `ponytail` (smallest change that works). `lean-build` for new features, `surgical-patch` for bug fixes. |
| Long chats or Ali wants short replies | `caveman` (say "caveman mode"; "normal mode" to stop). Never use it inside CSV/file contents or client-facing text. |
| Big memory files (CLAUDE.md etc.) getting long | `caveman-compress` (keeps backup). |
| Reading the repo | `graphify` query first, `caveman-explore`/`cavecrew` for searches, then read only the files needed. |
| Commit messages / reviews | `caveman-commit`, `caveman-review`, `ponytail-review` |
| Scoring creators | Follow `influencer-os/tokens.md`: code first, free API batch, Sonnet for final check, Opus only for hard debugging. ONE batch per day. |
| Proof of done, no extras | `verify-and-stop` |

## 4. Finding more skills
| When | Use |
|---|---|
| Need a capability not listed | `SearchSkills` / `SuggestSkills` tools, then `skill-creator` to build one. |
| Browse what exists | awesome-claude-skills (ComposioHQ) on GitHub; installed ones live in `.claude/skills/`. |
| Installing anything new | Read its code first for unknown servers and install scripts (tokens.md rule). Install in a virtual env. |

## 5. Do not use
`caveman-setup/discover/manage/optimize/learn/evidence-review` (need Caveman Cloud account), `skill-share`, `langsmith-fetch`, `video-downloader` unless Ali asks.

## Output reminder
Every run ends with: short summary + update `delivered.csv` + one line in `log.md` if something broke.
