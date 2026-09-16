# MedTrack_Site — DONE (2026-09-15)

This handoff is **complete**. Kept as a short record; nothing here is pending.

## What shipped

- **Site is live**: <https://lefty3030.github.io/MedTrack_Site/> — a single
  self-contained `docs/index.html` (Privacy Policy · Support · Buy Me a Coffee),
  rebranded from the SkillTrack_Site template to MedTrack (teal-green accents on
  the app's own seed `#2E7D6B`, a capsule icon, MedTrack privacy copy: on-device
  only, a personal aid not a medical record, passphrase-encrypted backups).
- **GitHub Pages**: enabled, serving `main` / `/docs`. HTTPS enforced.
- **Support email** `SkillTrack101@gmail.com` and **coffee link**
  `https://buymeacoffee.com/DougWiebe` carried over unchanged.

## App repoint — also done

Back in the MedTrack app repo (`Lefty3030/MedTrack`), the About screen was
repointed off the interim SkillTrack site onto this one, before the About
feature ever reached a device:

- `lib/features/settings/about_screen.dart` → `_supportSiteUrl` +
  `https://lefty3030.github.io/MedTrack_Site/`; ADR 0002 + CONTEXT.md updated.
- Verification bar green (analyze clean, 82 tests, iOS release build), commits
  `103db70` (About screen) + `90c0017` (repoint) pushed to `main`.
- Installed on all three devices (Doug's iPhone, Douglas's iPad, Candace's iPad)
  via wireless `flutter install --release -d <udid>`.

## Editing the site later

It's just `docs/index.html`. Edit, commit, push to `main`; Pages redeploys in a
minute or two. Live URL and links unchanged.
