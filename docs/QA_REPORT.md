# QA report

October 7, 2026. Independent presentation concept. Browser used: Codex in-app browser (Chromium). No contact message, order or booking was sent during QA.

## Local results

| Check | Observed result |
|---|---|
| Structural verification | `python scripts/check-site.py` passes: one H1, unique IDs, 29 valid/nonempty link targets, all 13 local asset files, three responsive images with factual alt/dimensions, labeled fields and all required documents. |
| JavaScript | `node --check script.js` passes. Browser error/warning log empty during tested flows. |
| Desktop | 1440×900: full composition, menu columns and catering inspected visually. Document width 1425px (scrollbar), viewport 1440px; no page overflow. |
| Mobile | 390×844 and 320×740 inspected visually. Document widths 375px and 305px; no page overflow. Hero changed after inspection to expose food sooner. Desktop layout becomes a deliberate vertical sequence. |
| Navigation | Header menu/catering links and mobile Find the truck dock reach corresponding sections. Direct telephone/email/maps/social hrefs checked. |
| Keyboard | First Tab focuses visible Skip to content with solid focus ring. Native links, summary, form fields and submit control remain keyboard-operable. |
| Form invalid case | Guest count 0 rejected; no result created. Required date/location and date minimum are native constraints. |
| Form valid case | January 20, 2027; 50 guests; `McKinney & Frisco, TX`; Work event produces correctly URL-encoded mailto draft with those values. No email app was opened and nothing was sent. |
| Form editing | Changing a field hides an earlier draft, preventing an outdated draft from appearing current. |
| Actual bug corrected | Initial occasion choices were malformed; corrected to six properly declared options and selected Work event successfully. |
| Fonts/images | Local fonts loaded; all three photographs decoded successfully after scrolling. Mobile selected 480px food variants and 600px truck variant. Hero uses fetchpriority high; other photos are lazy. |
| Preview safeguards | robots meta noindex/nofollow, robots.txt disallow, concept/approval disclosure and source attribution present. |
| Without JavaScript | Tested a temporary copy with the script omitted: all ten menu rows, local fonts, images and direct phone/email CTAs remain available; optional draft helper stays hidden. This fixture is ignored and not published. |
| Accessibility source inspection | Semantic landmarks/headings, factual alts, labels, focus styles, adequate large controls, reduced-motion CSS and useful non-JS contact links. This is not a formal WCAG certification or assistive-technology audit. |

Evidence files are stored locally in ignored `artifacts/`, including desktop hero/menu and mobile hero/menu/inquiry screenshots. Decorative ticker intentionally clips within its own overflow-hidden container; its off-screen items do not create page scrolling.

## Public deployment

**Published and verified:** [public preview](https://gabi0102souza-stack.github.io/king-kups-preview/), [repository](https://github.com/gabi0102souza-stack/king-kups-preview), branch `main`. GitHub Pages is configured to serve `main` at `/`. The [initial Pages deployment](https://github.com/gabi0102souza-stack/king-kups-preview/actions/runs/37656784894) completed successfully. Final documentation and the Maps/schedule correction are committed to the same branch.

| Public check | Observed result |
|---|---|
| HTTP and integrity | 17 production files returned HTTP 200 with expected HTML/CSS/JS/WebP/WOFF2/text content types. SHA-256 of every response matches its local source. Evidence: ignored `artifacts/public-http-check.json`. |
| Desktop | Actual public URL inspected at 1440×900. Document width 1425px, no page overflow. Hero, menu, story, catering and location inspected. |
| Mobile | Actual public URL inspected at 390×844 and 320×740. Document widths 375px and 305px, no page overflow. Header, deliberate food crop, vertical menu, catering inquiry and persistent truck/contact dock checked. |
| Images/fonts/script | All three photographs load from published responsive WebP URLs; local fonts load; the progressive inquiry helper is enabled. No error/warning console entries during tested flows. |
| Form/navigation | Menu and truck anchors work. The public catering helper prepares the correctly encoded draft for January 20, 2027, 50 guests, McKinney & Frisco, TX, Work event. No message was sent. Phone/email/social links use the verified business contacts. |
| Maps correction | A directions URL attempted a route from an unavailable origin. Changed to a place search, labeled Open in Maps. The search opens the correct King Kups listing with the matching address/phone and Exxon landmark. |
| Schedule correction | Expanded Google Maps weekly hours: Tuesday/Friday 11 AM–8:30 PM; Saturday closed. Official Instagram and Restaurantji differ on Saturday. The preview now asks visitors to confirm Saturday with the truck and cites Google Maps for the listed weekday times. |
| Contrast | Source palette checks: ink/paper 16.33:1, muted/paper 6.55:1, teal/paper 4.55:1, gold/paper 5.40:1, ink/aqua 9.99:1. Focus indicators and reduced-motion styles are present. |
| Preview safeguards | Public HTML retains noindex/nofollow, robots.txt disallows crawling, footer identifies the independent concept, and photo/source attribution remains available. |

Public screenshots: `artifacts/public-desktop.jpg`, `artifacts/public-desktop-full.jpg`, `artifacts/public-mobile-390.jpg`, `artifacts/public-mobile-320.jpg`. These are local QA evidence, intentionally excluded from the production repository. No Lighthouse score or formal WCAG certification is claimed.

## Limits

No actual phone call, email transmission, booking, payment or physical visit. No live synchronization with social feeds. External platforms can require login or restrict automated reads. Original photography rights and operational facts remain owner-confirmation items.
