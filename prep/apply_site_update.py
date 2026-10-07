#!/usr/bin/env python3
"""Apply the prepared MedTrack site update (new icon + design fixes) to docs/.

Dry run by default (prints what it would change). Add --write to edit docs/ in place.
See SITE_UPDATE_ICON.md for what each change is and why. Every replacement is anchored to the
current page text and must match exactly the expected number of times, otherwise the script stops
without writing anything.
"""
import base64, datetime, re, sys, urllib.parse
from pathlib import Path

root = Path(__file__).resolve().parent.parent
write = "--write" in sys.argv
APP_STORE_URL = "https://apps.apple.com/us/app/medtrack/id6812911967"

svg = (root / "prep" / "icon.svg").read_text().strip()
compact = re.sub(r">\s+<", "><", svg)
b64 = base64.b64encode(compact.encode()).decode()
favicon = "data:image/svg+xml," + urllib.parse.quote(compact, safe="/:=,;")
inline_icon = compact.replace(
    "<svg ",
    '<svg class="st-icon" role="img" aria-label="MedTrack icon: a coral circle, amber half-disc and mint capsule on an indigo rounded square" ', 1)
today = datetime.date.today()
updated = f"{today.day} {today:%B %Y}"


def once(text, old, new, label, count=1):
    n = text.count(old)
    print(f"{label}: {n} match(es) (expected {count})")
    if n != count:
        sys.exit(f"STOP: {label} — page changed, update this script. Nothing written.")
    return text.replace(old, new)


def rx(text, pattern, new, label, count=1):
    n = len(re.findall(pattern, text, flags=re.S))
    print(f"{label}: {n} match(es) (expected {count})")
    if n != count:
        sys.exit(f"STOP: {label} — page changed, update this script. Nothing written.")
    return re.sub(pattern, lambda m: new, text, flags=re.S)


# ---------- index.html ----------
p = root / "docs" / "index.html"
s = p.read_text()

# icon: favicon + header
s = rx(s, r'<link rel="icon" type="image/svg\+xml" href="[^"]*">',
       f'<link rel="icon" type="image/svg+xml" href="{favicon}">', "favicon")
s = rx(s, r'<svg class="st-icon".*?</svg>', inline_icon, "header icon")

# #4 stronger link pills
s = once(s, """  nav.st-nav a{
    font-size:.86rem;font-weight:600;letter-spacing:.02em;
    color:var(--link);text-decoration:none;
    padding:6px 12px;border:1px solid var(--line);border-radius:999px;
    background:var(--surface);
  }
  nav.st-nav a:hover{border-color:var(--brand);}""",
"""  nav.st-nav a{
    font-size:.86rem;font-weight:600;letter-spacing:.02em;
    color:var(--link);text-decoration:none;
    padding:6px 13px;border:1.5px solid var(--brand);border-radius:999px;
    background:var(--surface);
  }
  nav.st-nav a:hover{background:var(--promise-bg);}""", "link pill style")

# #2 replace the red/amber/green dots with a padlock; #7 App Store button styles
s = once(s, """  .st-dots{display:flex;gap:7px;flex:0 0 auto;}
  .st-dots span{width:13px;height:13px;border-radius:50%;display:block;}
""",
"""  .st-lock{flex:0 0 auto;width:44px;height:44px;border-radius:12px;display:grid;place-items:center;
    background:var(--surface);border:1px solid var(--promise-line);color:var(--brand);}
  .st-lock svg{width:24px;height:24px;}
  .st-cta{display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin:16px 0 4px;}
  .st-store{font-size:.95rem;font-weight:700;text-decoration:none;background:var(--brand);color:var(--bg);
    padding:10px 20px;border-radius:999px;}
  .st-store:hover{background:var(--brand-2);}
  .st-store:focus-visible{outline:2px solid var(--brand);outline-offset:2px;}
  .st-cta span{color:var(--muted);font-size:.9rem;}
""", "dots css -> lock + button css")
s = once(s, """      <span class="st-dots" aria-hidden="true">
        <span style="background:var(--red)"></span>
        <span style="background:var(--amber)"></span>
        <span style="background:var(--green)"></span>
      </span>""",
"""      <span class="st-lock" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="11" width="14" height="9" rx="2.5"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>
      </span>""", "dots html -> padlock")

# #7 App Store button (above the section links)
s = once(s, '    <nav class="st-nav" aria-label="Sections">',
f"""    <p class="st-cta"><a class="st-store" href="{APP_STORE_URL}">Get MedTrack on the App Store</a><span>Free &middot; iPhone and iPad</span></p>
    <nav class="st-nav" aria-label="Sections">""", "App Store button")

# #5 policy date
s = rx(s, r'<p class="updated">Last updated: [^<]*</p>',
       f'<p class="updated">Last updated: {updated}</p>', "policy date")
out = {p: s}

# ---------- walkthrough.html ----------
p2 = root / "docs" / "walkthrough.html"
w = p2.read_text()
count = 0
def logo(m):
    global count; count += 1
    return f'src="data:image/svg+xml;base64,{b64}"{m.group(1)}'
w = re.sub(r'src="data:image/png;base64,[A-Za-z0-9+/=]{20000,22000}"(\s+alt="(?:MedTrack logo)?")', logo, w)
print(f"walkthrough logos: {count} match(es) (expected 3)")
if count != 3:
    sys.exit("STOP: walkthrough logos — page changed, update this script. Nothing written.")
w = once(w, "/* traffic-light motif from the app logo */", "/* traffic-light status colours */", "walkthrough css comment")
out[p2] = w

for path, text in out.items():
    if write:
        path.write_text(text); print("wrote", path.relative_to(root))
print("done" if write else "dry run only — re-run with --write to apply")
