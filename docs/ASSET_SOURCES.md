# Asset sources

Retrieved October 7, 2026. All photographs are real assets displayed in the King Kups listing on [Visit McKinney](https://www.visitmckinney.com/listing/king-kups-679), with matching business address and telephone. No AI or stock food photographs are used.

| Local file(s) | Original and source | Purpose | Rights / preview notes |
|---|---|---|---|
| `assets/food-{480,800,960}.webp` | [Original JPG](https://www.visitmckinney.com/sites/mckinney/media/f06e672fb33fd2bd.jpg), also [listing AVIF](https://www.visitmckinney.com/sites/mckinney/img/m-f06e672fb33fd2bd-1920.avif) | Large hero: actual King Kups food on a branded wooden surface | Photographer not named. Tourism page is all-rights-reserved; no open license is claimed. Public concept uses credited contextual imagery. Permission is required for an owner-approved official launch. |
| `assets/wonton-{480,800,960}.webp` | [Original JPG](https://www.visitmckinney.com/sites/mckinney/media/61eef36639d9b4d0.jpg) | Signature-food section | Same rights status. The listing calls the image fried wontons; exact item identity is not independently confirmed. Alt text stays factual and visual. |
| `assets/truck-{600,1000,1365}.webp` | [Original JPG](https://www.visitmckinney.com/sites/mckinney/media/a1b222847be2465a.jpg) | Truck, observed brand colors and local identity | Same rights status. Photo depicts the real truck; it does not guarantee today's truck location or current wrap. |
| `assets/fonts/anton-latin.woff2` | [Google Fonts CDN](https://fonts.gstatic.com/s/anton/v27/1Ptgg87LROyAm3Kz-C8.woff2), [upstream](https://github.com/google/fonts/tree/main/ofl/anton) | Display headings and concept wordmark | SIL Open Font License. Included as `assets/fonts/Anton-OFL.txt`. |
| `assets/fonts/dm-sans-latin.woff2` | [Google Fonts CDN](https://fonts.gstatic.com/s/dmsans/v17/rP2Yp2ywxg089UriI5-g4vlH9VoD8Cmcqbu0-K4.woff2), [upstream](https://github.com/google/fonts/tree/main/ofl/dmsans) | Body text and controls, variable weight | SIL Open Font License. Included as `assets/fonts/DM-Sans-OFL.txt`. |
| Embedded SVG favicon / wordmark | New typographic concept made in HTML/SVG, informed by real brand colors | Preview identity at small sizes | Not an official supplied logo. Does not reproduce the illustrated profile artwork. |
| CSS checkered motif / location SVG | Original simple CSS geometry / geometric pin | Basket-liner accent and location affordance | Decorative checks are hidden from assistive technology. |

Processing: only orientation correction, proportional resizing and WebP compression. No food manipulation, invented ingredients, object insertion, generated backgrounds or generative editing. Hero crop is CSS presentation; source image is preserved in ignored `.asset-originals/` and is not committed twice. Responsive variants are produced by `scripts/optimize-assets.py`. Wonton source decodes to 960×785; the initially reported 784-pixel height was approximate.

Identity caution: the hero resembles folded taco shells, while the listing's alt text calls it wontons. The site does not label that photograph as a specific menu item. Photos should be replaced or explicitly licensed with the owner before a commercial official launch. Footer credits link to the tourism source.
