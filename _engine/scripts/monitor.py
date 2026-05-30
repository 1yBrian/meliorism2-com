#!/usr/bin/env python3
"""monitor.py — Live-site verification + daily heartbeat.

Runs at 4:15 AM PT (after the 4 AM release cron). Fetches https://meliorism2.com/,
extracts the featured slug from the hero CTA href, compares to today's expected slug
from archive/. If they match: heartbeat success. If not: failure alert.

Either way, sends a Telegram message — daily heartbeat is non-negotiable.

Telegram token: $TELEGRAM_BOT_TOKEN (env or ~/.config/meliorism2/telegram-bot-token)
Chat ID: 8497163817 (Brian's @Zendo13btastic_bot)

Usage:
    python3 _engine/scripts/monitor.py
"""
import os, re, sys, pathlib, urllib.request, urllib.parse, urllib.error
from datetime import datetime, timezone

REPO = pathlib.Path(__file__).resolve().parents[2]
LIVE_URL = "https://meliorism2.com/"
CHAT_ID = "8497163817"

def get_token() -> str | None:
    tok = os.environ.get("TELEGRAM_BOT_TOKEN")
    if tok: return tok.strip()
    p = pathlib.Path.home() / ".config" / "meliorism2" / "telegram-bot-token"
    if p.exists():
        return p.read_text().strip()
    return None

def send_telegram(text: str) -> bool:
    tok = get_token()
    if not tok:
        print("WARN: no Telegram token; printing instead:")
        print(text)
        return False
    url = f"https://api.telegram.org/bot{tok}/sendMessage"
    data = urllib.parse.urlencode({"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}).encode()
    try:
        urllib.request.urlopen(urllib.request.Request(url, data=data), timeout=10)
        return True
    except Exception as e:
        print(f"WARN: Telegram send failed: {e}")
        return False

def expected_slug() -> tuple[str, str] | None:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    matches = sorted((REPO / "archive").glob(f"{today}-*.html"))
    matches = [m for m in matches if re.match(r"\d{4}-\d{2}-\d{2}-.+\.html$", m.name)]
    if not matches: return None
    p = matches[0]
    content = p.read_text()
    title_m = re.search(r"<!-- meliorism2:title: (.+?) -->", content)
    title = title_m.group(1).strip() if title_m else p.stem[11:].replace("-", " ").title()
    return p.name, title

def live_featured() -> tuple[str | None, str | None]:
    try:
        req = urllib.request.Request(LIVE_URL, headers={"User-Agent": "Meliorism2-Monitor/1.0", "Cache-Control": "no-cache"})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode("utf-8", errors="ignore")
    except Exception as e:
        return None, f"FETCH_ERROR: {e}"
    href = re.search(r'<a href="([^"]+)" class="hero-cta">', html)
    title = re.search(r'<h2 class="featured-title">([^<]+)</h2>', html)
    return (
        (href.group(1).split("/")[-1] if href else None),
        (title.group(1).strip() if title else None),
    )

def main():
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    exp = expected_slug()
    live_slug, live_title = live_featured()
    if exp is None:
        msg = f"⚠️ Meliorism2 {today}: no archive file prepared. Site likely showing yesterday."
        send_telegram(msg)
        sys.exit(1)
    expected_filename, expected_title = exp
    if live_slug == expected_filename:
        msg = f"✅ Meliorism2 {today}: <b>{expected_title}</b> is live."
        send_telegram(msg)
        sys.exit(0)
    msg = (
        f"❌ Meliorism2 {today}: live site stale.\n"
        f"Expected: <b>{expected_title}</b> ({expected_filename})\n"
        f"Live shows: <b>{live_title}</b> ({live_slug})\n"
        f"Check Cloudflare deploy and GitHub Actions runs."
    )
    send_telegram(msg)
    sys.exit(1)

if __name__ == "__main__":
    main()
