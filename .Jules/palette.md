## 2024-05-24 - Carousel Accessibility Pattern
**Learning:** Custom carousel components in this app's promo pages lack native screen reader support and need explicit structural ARIA roles.
**Action:** Always apply `role="region"` and `aria-roledescription="carousel"` to the stage container, and `role="group"` with `aria-roledescription="slide"` to individual product cards.
