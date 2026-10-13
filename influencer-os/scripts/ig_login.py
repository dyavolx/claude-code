"""One-time Instagram login via Scrapling. Saves the session in .ig-profile/ (gitignored).
Credentials come from .env (IG_USER, IG_PASS). Never printed."""
import os, sys, time, random
from pathlib import Path
from scrapling.fetchers import DynamicFetcher

ROOT = Path(__file__).resolve().parent.parent
env = {}
for line in (ROOT / ".env").read_text().splitlines():
    if "=" in line and not line.startswith("#"):
        k, v = line.split("=", 1)
        env[k.strip()] = v
USER, PW = env["IG_USER"], env["IG_PASS"]
PROFILE = str(ROOT / ".ig-profile")
CHROME = "/opt/pw-browsers/chromium"
result = {}

def act(page):
    page.wait_for_timeout(2500)
    for txt in ("Allow all cookies", "Accept all", "Allow essential and optional cookies", "Decline optional cookies"):
        b = page.get_by_role("button", name=txt)
        if b.count():
            b.first.click(); page.wait_for_timeout(1000); break
    page.fill('input[name="email"]', USER)
    page.wait_for_timeout(random.randint(600, 1400))
    page.fill('input[name="pass"]', PW)
    page.wait_for_timeout(random.randint(600, 1400))
    page.keyboard.press("Enter")
    page.wait_for_timeout(9000)
    if "codeentry" in page.url or "challenge" in page.url:
        # Instagram sent a security code. Wait for it in .ig-code (write the digits there).
        codefile = ROOT / ".ig-code"
        print("WAITING_FOR_CODE", flush=True)
        for _ in range(240):
            if codefile.exists() and codefile.read_text().strip():
                break
            time.sleep(5)
        else:
            result["status"] = "timeout waiting for code"; return
        code = codefile.read_text().strip(); codefile.unlink()
        inp = page.locator('input:visible').first
        inp.fill(code)
        page.wait_for_timeout(800)
        page.keyboard.press("Enter")
        page.wait_for_timeout(9000)
        for txt in ("Save info", "Not now", "Save"):
            b = page.get_by_role("button", name=txt)
            if b.count():
                b.first.click(); page.wait_for_timeout(2000); break
    result["url"] = page.url
    result["title"] = page.title()
    body = page.inner_text("body")[:600].replace("\n", " | ")
    result["body"] = body
    result["cookies"] = sorted({c["name"] for c in page.context.cookies() if "instagram" in c["domain"]})

DynamicFetcher.fetch("https://www.instagram.com/accounts/login/", headless=True, executable_path=CHROME,
                     user_data_dir=PROFILE, page_action=act, network_idle=False, timeout=90000, locale="en-GB")
for k, v in result.items():
    print(k, "=", str(v)[:200])
