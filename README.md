# King Kups preview

Independent website concept for presentation to King Kups, McKinney, Texas. Not commissioned or approved by the business. Research performed October 7, 2026 before implementation. The old `kingkups.com` domain is referenced publicly but did not serve an active site during validation; see [research](docs/RESEARCH.md).

## Website

Static HTML, CSS and one small progressive-enhancement script. No framework, package install, build step, analytics, backend or remote font dependency. All production asset paths are relative for GitHub Pages project hosting. Three real sourced photographs have responsive WebP variants; fonts are local WOFF2 with included OFL licenses.

Primary journeys: menu, direct phone contact, truck location and official schedule updates, catering inquiry. The optional catering helper prepares a mailto draft. It does not send messages, store submissions or confirm bookings; the visitor reviews and sends in their own email client. Direct contact links remain useful without JavaScript.

## Run and verify

```powershell
python -m http.server 4187 --bind 127.0.0.1
python scripts/check-site.py
node --check script.js
```

Open the local server for development only. The required deliverable is the public GitHub Pages URL. Browser QA includes desktop, 390px, another narrow mobile size, form validation, anchored navigation, keyboard focus and asset loading. Evidence and limits live in [QA report](docs/QA_REPORT.md).

Optional asset regeneration: install Pillow in a development environment, place the three original JPGs listed in [asset sources](docs/ASSET_SOURCES.md) in `.asset-originals/`, then run `python scripts/optimize-assets.py`. Original downloads, CLI tools, logs and QA artifacts are ignored. Production has no dependency on these tools.

## Publish

Create a public repository named `king-kups-preview`, commit and push `main`, enable GitHub Pages from `main` at `/`. `.nojekyll` prevents Jekyll processing. After publication verify the actual public URL, images, styles, scripts, fonts, links and desktop/mobile layouts. The preview carries robots noindex/nofollow and a footer concept disclosure.

Published and verified October 7, 2026. Public preview: [King Kups](https://gabi0102souza-stack.github.io/king-kups-preview/). Public repository: [gabi0102souza-stack/king-kups-preview](https://github.com/gabi0102souza-stack/king-kups-preview), branch `main`. GitHub Pages serves `main` at `/` over HTTPS. Files were committed directly to the repository through the authenticated GitHub browser interface; the local checkout tracks `origin/main`. The Pages build and deployment succeeded, and the actual public site was tested on desktop and both required mobile widths.

## Content decisions and official launch

No unverified prices, award badge, live opening status, testimonials or active delivery marketplace. Hours are clearly a listed reference with conflicting sources documented and an immediate confirmation path. Social recommendations carry source/date context. Photos are publicly viewable, not openly licensed; secure owner/rightsholder permission or replace with authorized photographs before an official commercial launch. Confirm menu, operational details, catering terms, branding and old domain ownership with the owner.

Required documents: [Research](docs/RESEARCH.md), [Asset sources](docs/ASSET_SOURCES.md), [QA report](docs/QA_REPORT.md), [Creative direction](CREATIVE_DIRECTION.md), [Site strategy](SITE_STRATEGY.md), [Self-critique](SELF_CRITIQUE.md).
