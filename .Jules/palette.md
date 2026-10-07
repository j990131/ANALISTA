## 2026-10-07 - Custom Carousel Accessibility Pattern
**Learning:** Custom carousels in this project need specific ARIA roles to be properly read by screen readers, replacing generic container behavior.
**Action:** Always apply `role='region'` and `aria-roledescription='carousel'` on the stage container, and `role='group'` with `aria-roledescription='slide'` on the individual product cards for optimal screen reader support.
