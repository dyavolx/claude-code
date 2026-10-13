"""Verify candidate handles by loading profile + latest posts (page view, no API). Slow, polite.
Usage: ig_verify.py handle1,handle2,...  -> data/raw/ig-verify-<date>.json"""
import json, sys, time, random, datetime
from pathlib import Path
from scrapling.fetchers import DynamicFetcher

ROOT = Path(__file__).resolve().parent.parent
handles = sys.argv[1].split(",")
N_POSTS = 5
out = {}

def act(page):
    page.wait_for_timeout(2500)
    for h in handles:
        rec = {"posts": []}
        try:
            page.goto(f"https://www.instagram.com/{h}/", wait_until="domcontentloaded")
            page.wait_for_timeout(random.randint(4000, 7000))
            m = page.locator('meta[property="og:description"]')
            rec["meta"] = m.first.get_attribute("content") if m.count() else None
            rec["bio_text"] = page.inner_text("header")[:400].replace("\n", " | ") if page.locator("header").count() else ""
            links = page.eval_on_selector_all('a[href*="/p/"],a[href*="/reel/"]', "e=>[...new Set(e.map(x=>x.getAttribute('href')))]")
            rec["n_links"] = len(links)
            for href in links[:N_POSTS]:
                page.goto("https://www.instagram.com" + href, wait_until="domcontentloaded")
                page.wait_for_timeout(random.randint(3500, 6000))
                pm = page.locator('meta[property="og:description"]')
                rec["posts"].append({"href": href, "d": (pm.first.get_attribute("content") if pm.count() else None)})
        except Exception as e:
            rec["error"] = str(e)[:150]
        out[h] = rec
        (ROOT / "data/raw").mkdir(exist_ok=True)
        (ROOT / f"data/raw/ig-verify-{datetime.date.today()}.json").write_text(json.dumps(out, ensure_ascii=False))
        time.sleep(random.uniform(6, 12))

DynamicFetcher.fetch("https://www.instagram.com/", headless=True, executable_path="/opt/pw-browsers/chromium",
                     user_data_dir=str(ROOT / ".ig-profile"), page_action=act, timeout=3000000, locale="en-GB")
print("done", len(out))
