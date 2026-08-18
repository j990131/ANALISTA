
## 2024-08-18 - Carousel Accessibility Pattern
**Learning:** Custom carousels in this project (both React and Vanilla HTML) need strict adherence to W3C ARIA carousel patterns because they rely on decorative text for navigation (e.g. `‹`, `›`) and don't natively announce state changes.
**Action:** When implementing or updating custom carousels, always apply `role="region"` and `aria-roledescription="carousel"` to the stage container, `role="group"` with `aria-roledescription="slide"` to individual cards, and `aria-live="polite"` to dynamically updating info areas.
