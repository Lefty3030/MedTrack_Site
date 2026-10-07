#!/usr/bin/env python3
"""Swap the old teal capsule icon for the new indigo MedTrack icon on the site.

Dry run by default (prints what it would change). Add --write to edit docs/ in place.
Source of truth for the artwork: prep/icon.svg (same shapes as the app's assets/brand/app_icon.svg).
Touches only the icon: the site's teal page colours are deliberately left alone (the app UI is still teal).
"""
import base64, re, sys, urllib.parse
from pathlib import Path

root = Path(__file__).resolve().parent.parent
write = "--write" in sys.argv
svg = (root / "prep" / "icon.svg").read_text().strip()
compact = re.sub(r">\s+<", "><", svg)

b64 = base64.b64encode(compact.encode()).decode()
favicon = "data:image/svg+xml," + urllib.parse.quote(compact, safe="/:=,;")
inline = compact.replace(
    "<svg ",
    '<svg class="st-icon" role="img" aria-label="MedTrack icon: a coral circle, amber half-disc and mint capsule on an indigo rounded square" ', 1)

def sub(text, pattern, repl, label, expect):
    new, n = re.subn(pattern, lambda m: repl, text, flags=re.S)
    print(f"{label}: {n} replaced (expected {expect})")
    if n != expect:
        sys.exit(f"STOP: {label} matched {n}, expected {expect} — page changed, update this script")
    return new

p = root / "docs" / "index.html"
s = p.read_text()
s = sub(s, r'<link rel="icon" type="image/svg\+xml" href="[^"]*">',
        f'<link rel="icon" type="image/svg+xml" href="{favicon}">', "index.html favicon", 1)
s = sub(s, r'<svg class="st-icon".*?</svg>', inline, "index.html header icon", 1)
out = {p: s}

p2 = root / "docs" / "walkthrough.html"
w = p2.read_text()
count = 0
def repl(m):
    global count; count += 1
    return f'src="data:image/svg+xml;base64,{b64}"{m.group(1)}'
w = re.sub(r'src="data:image/png;base64,[A-Za-z0-9+/=]{20000,22000}"(\s+alt="(?:MedTrack logo)?")', repl, w)
print(f"walkthrough.html logos: {count} replaced (expected 3)")
if count != 3: sys.exit("STOP: expected 3 logo images — check by hand")
w = w.replace('/* traffic-light motif from the app logo */', '/* traffic-light status colours */')
out[p2] = w

for path, text in out.items():
    if write: path.write_text(text); print("wrote", path.relative_to(root))
print("done" if write else "dry run only — re-run with --write to apply")
