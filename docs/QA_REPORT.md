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

Pending publication. Public URL rendering, all asset responses, desktop/mobile behavior and live link destinations still require verification. Local QA alone is not completion.

## Limits

No actual phone call, email transmission, booking, payment or physical visit. No live synchronization with social feeds. External platforms can require login or restrict automated reads. Original photography rights and operational facts remain owner-confirmation items.
