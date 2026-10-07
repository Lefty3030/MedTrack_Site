# Site update for the new app icon (prepared 2026-10-06, apply in a few days)

The app icon changed from a white/mint capsule on teal to an indigo Bauhaus composition (coral circle, amber half-disc,
mint capsule, white dot). It ships with MedTrack 1.1.1. Source art: `assets/brand/app_icon.svg` in the app repo.

## When to apply
Apply **after the 1.1.1 build with the new icon is live on the App Store**, so the site and the store match
(or earlier, if Doug prefers; the site carries no version numbers).

## What changes (icon only)
| Where | What it is today | Change |
|---|---|---|
| `docs/index.html` line ~11 | favicon: inline SVG data URI, teal capsule | new icon SVG as data URI |
| `docs/index.html` lines ~141-153 | header `<svg class="st-icon">`, teal capsule | new icon inline SVG, new `aria-label` |
| `docs/walkthrough.html` (3 places) | `<img>` base64 192px PNG "MedTrack logo" (brand row, closing slide, one with empty alt) | same image as an SVG data URI (keeps the rounded corners; a PNG would get white corners) |
| `docs/walkthrough.html` line ~130 | CSS comment "traffic-light motif from the app logo" | reworded (the new logo has no traffic lights) |

## What does NOT change (deliberate)
- **Page colours stay teal** (`--brand:#2E7D6B` etc., "MedTrack Teal" tokens). The app's own screens are still teal, and the
  walkthrough shows them, so a teal site matches the app UI; only the icon changed. Recolouring the site indigo would be a
  separate design decision for Doug.
- The walkthrough's embedded app screenshots (JPEG) — they don't show the icon. Re-check only if the app UI changes.
- Support email, privacy copy, coffee link — unrelated.

## How to apply
```bash
cd /Users/wiebe/Claude/Claude_Code/MedTrack_Site
python3 prep/apply_icon.py            # dry run: prints what would change
python3 prep/apply_icon.py --write    # edits docs/index.html and docs/walkthrough.html
git diff --stat                       # expect only those two files
```
The script stops without writing if a pattern doesn't match (expects 1 favicon, 1 header icon, 3 walkthrough logos), so
if the pages were edited in the meantime it fails loudly instead of half-applying. Tested 2026-10-06 against copies of
the current pages (all replacements matched; header SVG parses as valid XML); the real `docs/` was not touched.

Then: open `docs/index.html` in a browser (light and dark mode) and check the header icon and tab favicon; open
`docs/walkthrough.html` and check the logo on the first and last slides; commit, push to `main`; Pages redeploys in a
minute or two. Hard-refresh the live site (favicons cache hard).

## Files
- `prep/icon.svg` — the rounded-square icon artwork used by the script.
- `prep/apply_icon.py` — the one-shot updater described above.
