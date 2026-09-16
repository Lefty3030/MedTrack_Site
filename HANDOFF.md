# MedTrack_Site — session handoff (seed for a fresh session)

Written 2026-09-15 by the MedTrack app session. **Open a new session in this
directory** (`/Users/wiebe/Claude/Claude_Code/MedTrack_Site`) and start here.
Delete/overwrite once the site is live.

## Goal

Build a small, static **privacy & support website for MedTrack** and deploy it on
**GitHub Pages**, so the MedTrack app's About screen can link to it (Buy Me a
Coffee + support email) instead of borrowing the SkillTrack site.

- **Target live URL**: <https://lefty3030.github.io/MedTrack_Site/>
- **Repo**: `Lefty3030/MedTrack_Site` (already created, public, `main`, remote
  wired). Pages will serve from **`docs/`** — same as SkillTrack_Site.

## What MedTrack is (for the copy)

A **private, on-device** medication tracker for Doug and his family (iPhone +
iPad, iOS only). Logging-first: a week strip / month calendar you tap to record
doses, plus supply tracking and per-medication reminders. Key posture (use this
for the Privacy section — see the app's `CONTEXT.md` and `docs/adr/` in the
MedTrack repo):

- **On-device only.** No account, no server, nothing is sent anywhere. Uninstall
  or erase without a backup = the data is gone.
- **A personal aid, not a medical record.** Doesn't replace a doctor/pharmacist
  or any official health record.
- **Encrypted backups.** A backup file is protected by a passphrase only the user
  knows; nobody (including us) can open it without that passphrase.
- The app holds **no INTERNET entitlement** and fetches nothing; links (this
  site, email) open in the system browser / Mail.

## Build brief

1. **Copy the template**: `/Users/wiebe/Claude/Claude_Code/SkillTrack_Site/docs/index.html`
   is the model — a single self-contained HTML page (inline CSS) with sections:
   **Privacy Policy**, **Support**, **Buy Me a Coffee**. Copy it to
   `docs/index.html` here, then **rebrand to MedTrack**:
   - Title/heading → MedTrack; `<title>MedTrack — Privacy &amp; Support</title>`.
   - **Rewrite the Privacy copy** for MedTrack using the posture above. Drop the
     SkillTrack-specific "no patient-identifying information / clinical logbook"
     framing — MedTrack is a personal medication tracker, not a clinical logbook.
   - Keep the **Support** section with the email
     `SkillTrack101@gmail.com` (`mailto:` link) — this is Doug's shared support
     inbox across his apps; keep it as-is unless Doug says otherwise.
   - Keep the **Buy Me a Coffee** section and button →
     `https://buymeacoffee.com/DougWiebe` (`target="_blank" rel="noopener noreferrer"`).
   - Keep the styling/quality bar of the SkillTrack page (it's clean and mobile-
     friendly); adjust colour accents to taste for MedTrack if desired.
2. **Commit** to `main`, **push** (`origin` is set).
3. **Enable GitHub Pages**: repo Settings → Pages → "Deploy from a branch" →
   `main` / `/docs`. (Or `gh api -X POST repos/Lefty3030/MedTrack_Site/pages
   -f 'source[branch]=main' -f 'source[path]=/docs'` — needs a token with the
   `pages` scope; the UI is the reliable path.) Wait for the deploy, then confirm
   the live URL renders and the coffee + email links work.

## Then: repoint the MedTrack app (back in the app session)

Once the site is live, do this small change in the **MedTrack app repo**
(`/Users/wiebe/Claude/Claude_Code/MedTrack`):

- In `lib/features/settings/about_screen.dart`, change `_supportSiteUrl` from
  `https://lefty3030.github.io/SkillTrack_Site/` → `https://lefty3030.github.io/MedTrack_Site/`.
- Update `docs/adr/0002-about-and-outbound-links.md` and `CONTEXT.md` (they
  currently name the SkillTrack site as the interim target).
- Re-run the verification bar (`flutter analyze` + `flutter test` + `flutter build
  ios --release`), then push + install on the three devices.

**Important — the About feature is staged, not shipped:** the app commit that
added the About screen (`103db70` on MedTrack `main`, pointing at the SkillTrack
site) is **committed locally but NOT pushed and NOT on any device**. It's being
held on purpose so the app can ship pointing at the *MedTrack* site from the
start — no interim SkillTrack link ever reaches a device. Repoint first, then
push + deploy once.

## Cross-references

- App repo: `Lefty3030/MedTrack` — About screen: `lib/features/settings/about_screen.dart`;
  decision: `docs/adr/0002-about-and-outbound-links.md`.
- Template site: `Lefty3030/SkillTrack_Site` → `docs/index.html`.
- Coffee: `https://buymeacoffee.com/DougWiebe` · Support email: `SkillTrack101@gmail.com`.
