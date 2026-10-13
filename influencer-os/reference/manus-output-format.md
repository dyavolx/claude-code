# output-format.md

## Historical Sheet1 columns

The creator table header in Sheet1 is:

```text
Creator Name, Profile Link / Handle, Platform, Niche, Country, Follower Count, Leads Finding Date, Outreach Status, 1st Message Sent, 1st Msg Date, 2nd Msg Sent, 2nd Msg Date, Follow-up Notes, Will Post + Ordered (order #), Order Date, Days Since Order, Traking link, Traking date, Commnet, Notes
```

Campaign overview fields above the table are: Compensation, Target Geo, Niches, and Requirements. The requirement text is: **5–100K followers, genuine engagement, active on IG/TikTok/YT, willing to grant ad rights**. USA creators are also included per the user’s instruction.

## Claude Code discovery output

For creator discovery, retain these normalized fields:

```text
handle, profile_url, platform, followers, median_views_last_10, engagement_rate, country, niche, contact_route, why_qualified, evidence_urls, dedup_status, ad_rights_status, source, discovery_date
```

The historical sheet does not consistently contain median views over the last 10 posts, ER, contact route, ad-rights status, or source attribution; write **unknown** when absent. Do not include child names, ages, or other child-identifying information from Notes.

## Five sample rows from the sheet-backed output

| handle | profile_url | followers | median_views_last_10 | engagement_rate | country | niche | contact_route | why_qualified |
|---|---|---:|---|---|---|---|---|---|
| @kindofsporty_ | https://www.instagram.com/kindofsporty_/ | 10K+ | unknown | unknown | United Kingdom | Basketball coach/trainer and parent creator | public contact/site route mentioned | basketball coaching, beginner/return-to-basketball content, recent reels |
| @marsodo | https://www.instagram.com/marsodo/ | 9453 | unknown | unknown | Italy | Basketball coach/trainer | none recorded | Italian U18 head coach; youth camp/player-development evidence |
| @coach_maitland | https://www.instagram.com/coach_maitland/ | 39.1K | unknown | unknown | United Kingdom | NBA/global skills trainer | public commercial/brand route mentioned | London youth academy/school programs and recent basketball reels |
| @_coachserrano_ | https://www.instagram.com/_coachserrano_/ | 28.6K | unknown | unknown | Spain | Basketball player-development coach | public registration route mentioned | youth camp, recent training reels, player-development fit |
| @basketball_dad33 | https://www.instagram.com/basketball_dad33/ | 1617 | unknown | unknown | US | Parent creator / active-family content | none recorded | Group 8 fast-pass: public profile, dedup check, active-child/basketball evidence, product-fit note |

## Open questions

- Confirm whether `why_qualified` should preserve full evidence prose or a compact summary.
- Exact ER and last-10 median-view thresholds remain unknown.
- Ad-rights status is required by the campaign overview but is not consistently populated in the historical rows.
