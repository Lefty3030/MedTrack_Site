# Site update: new app icon + design fixes (prepared 2026-10-06, apply in a few days)

The app icon changed from a white/mint capsule on teal to an indigo Bauhaus composition (coral circle, amber half-disc,
mint capsule, white dot). It ships with MedTrack 1.1.1. Source art: `assets/brand/app_icon.svg` in the app repo.

## When to apply
Apply **after the 1.1.1 build with the new icon is live on the App Store**, so the site and the store match
(or earlier, if Doug prefers; the site carries no version numbers).

## What changes
| # | Where (`docs/index.html` unless noted) | Today | Change |
|---|---|---|---|
| icon | favicon (line ~11) and header `<svg class="st-icon">` | teal capsule | new indigo icon (inline SVG), new `aria-label` |
| icon | `walkthrough.html`, 3 logo `<img>`s | base64 192px PNG | same art as an SVG data URI (a PNG would get white corners); CSS comment about the "traffic-light logo" reworded |
| 2 | privacy callout | red/amber/green dots (read as a status light, left over from the old logo) | padlock tile in the brand colour (works in light and dark) |
| 4 | section link pills | thin pale border, easy to miss | 1.5px brand-colour outline, tinted fill on hover |
| 5 | "Last updated" under Privacy Policy | 15 September 2026 | the date the script is run |
| 7 | new button above the link pills | none | "Get MedTrack on the App Store" (+ "Free · iPhone and iPad") linking to `https://apps.apple.com/us/app/medtrack/id6812911967` |

Notes:
- The App Store URL came from Apple's public lookup for bundle `com.dougwiebe.medtrack` (app id 6812911967).
- The button is plain text styled in the site's colours, **not** Apple's official "Download on the App Store" badge. That badge is
  Apple artwork with usage rules; download it from Apple's marketing resources and swap it in if you want it.
- The policy date: the privacy wording itself hasn't changed, so only keep #5 if you're happy showing the date of this site update.
- Item 3 from the review (wrapping nav row) is not included; the nav still wraps "Buy Me a Coffee" onto a second line on phones.

## What does NOT change (deliberate)
- **Page colours stay teal** (`--brand:#2E7D6B` etc., "MedTrack Teal" tokens). The app's own screens are still teal, and the
  walkthrough shows them; only the icon changed.
- The walkthrough's embedded app screenshots (JPEG), support email, privacy copy, coffee link.

## How to apply
```bash
cd /Users/wiebe/Claude/Claude_Code/MedTrack_Site
python3 prep/apply_site_update.py            # dry run: prints what would change
python3 prep/apply_site_update.py --write    # edits docs/index.html and docs/walkthrough.html
git diff --stat                       # expect only those two files
```
The script stops without writing if a pattern doesn't match (it expects exactly one match for each index.html edit and three walkthrough logos), so
if the pages were edited in the meantime it fails loudly instead of half-applying. Tested 2026-10-06 against copies of
the current pages (all replacements matched); the edited copy was viewed at phone width in light and dark mode. The real
`docs/` was not touched.

Then: open `docs/index.html` in a browser (light and dark mode) and check the header icon and tab favicon; open
`docs/walkthrough.html` and check the logo on the first and last slides; commit, push to `main`; Pages redeploys in a
minute or two. Hard-refresh the live site (favicons cache hard).

## Files
- `prep/icon.svg` — the rounded-square icon artwork used by the script.
- `prep/apply_site_update.py` — the one-shot updater described above.
