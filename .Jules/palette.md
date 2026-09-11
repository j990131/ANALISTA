## 2024-05-24 - Carousel Accessibility Pattern
**Learning:** Custom carousel components in this design system require specific ARIA roles (region, group) and roledescriptions (carousel, slide) for optimal screen reader support.
**Action:** Always apply role='region' and aria-roledescription='carousel' to the stage container, and role='group' with aria-roledescription='slide' to individual product cards.
