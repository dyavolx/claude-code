"""Hashtag discovery + profile check using the saved login (.ig-profile). Slow on purpose. Output: data/raw/ig-raw-<date>.json"""
import json, time, random, re, datetime, sys
from pathlib import Path
from scrapling.fetchers import DynamicFetcher

ROOT = Path(__file__).resolve().parent.parent
TAGS = sys.argv[1].split(",") if len(sys.argv) > 1 else ["basketballmum", "basketballdad", "basketballmama", "basketballfamily", "basketballparents"]
MAX_PROFILES = int(sys.argv[2]) if len(sys.argv) > 2 else 40
seen = set()
for f in [ROOT / "data/seen.csv"]:
    for l in f.read_text().splitlines()[1:]:
        seen.add(l.split(",")[0].lower())
extra = Path("/tmp/claude-0/-home-user-claude-code/9ec51b35-629b-5b27-996e-55152480ab92/scratchpad/dedupe.txt")
if extra.exists(): seen |= set(extra.read_text().split())
out = {"tags": {}, "profiles": {}, "errors": []}

JS = """async (u) => { const r = await fetch(u, {headers:{'x-ig-app-id':'936619743392459','x-requested-with':'XMLHttpRequest'},credentials:'include'}); return {s:r.status, t: await r.text()}; }"""

def get(page, url):
    r = page.evaluate(JS, url)
    time.sleep(random.uniform(3, 6))
    if r["s"] != 200:
        out["errors"].append([url, r["s"], r["t"][:120]]); return None
    try: return json.loads(r["t"])
    except Exception: out["errors"].append([url, "badjson"]); return None

def walk(o, acc):
    if isinstance(o, dict):
        if "user" in o and isinstance(o["user"], dict) and o["user"].get("username") and ("caption" in o or "code" in o):
            cap = (o.get("caption") or {}) or {}
            acc.append({"u": o["user"]["username"], "code": o.get("code"), "cap": (cap.get("text") or "")[:200] if isinstance(cap, dict) else ""})
        for v in o.values(): walk(v, acc)
    elif isinstance(o, list):
        for v in o: walk(v, acc)

def act(page):
    page.wait_for_timeout(3000)
    cands = {}
    for t in TAGS:
        d = get(page, f"https://www.instagram.com/api/v1/tags/web_info/?tag_name={t}")
        acc = []
        if d: walk(d, acc)
        out["tags"][t] = len(acc)
        for a in acc:
            u = a["u"].lower()
            if u in seen: continue
            cands.setdefault(u, a)
    out["candidates"] = len(cands)
    out["cand_list"] = cands
    bad = 0
    for u in list(cands)[:MAX_PROFILES]:
        time.sleep(random.uniform(8, 14))
        d = get(page, f"https://www.instagram.com/api/v1/users/web_profile_info/?username={u}")
        if not d:
            bad += 1
            if bad >= 3: out["errors"].append("stopped: 3 throttled/failed in a row"); break
            continue
        bad = 0
        usr = d.get("data", {}).get("user")
        if not usr: continue
        media = usr["edge_owner_to_timeline_media"]["edges"]
        posts = [{"ts": m["node"]["taken_at_timestamp"], "likes": m["node"]["edge_liked_by"]["count"],
                  "comments": m["node"]["edge_media_to_comment"]["count"], "video": m["node"].get("is_video"),
                  "cap": ((m["node"]["edge_media_to_caption"]["edges"] or [{"node": {"text": ""}}])[0]["node"]["text"])[:160]} for m in media]
        out["profiles"][u] = {"name": usr.get("full_name"), "bio": usr.get("biography"), "followers": usr["edge_followed_by"]["count"],
                              "private": usr.get("is_private"), "business": usr.get("is_business_account"), "cat": usr.get("category_name"),
                              "posts": posts, "found_via": cands[u]["cap"]}

DynamicFetcher.fetch("https://www.instagram.com/", headless=True, executable_path="/opt/pw-browsers/chromium",
                     user_data_dir=str(ROOT / ".ig-profile"), page_action=act, timeout=1500000, locale="en-GB")
Path(ROOT / "data/raw").mkdir(exist_ok=True)
fn = ROOT / f"data/raw/ig-raw-{datetime.date.today()}.json"
fn.write_text(json.dumps(out, ensure_ascii=False))
print("tags", out["tags"], "candidates", out.get("candidates"), "profiles", len(out["profiles"]), "errors", out["errors"][:5])
