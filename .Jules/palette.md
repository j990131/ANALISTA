## 2024-10-05 - Carousel Accessibility Pattern
**Learning:** Custom carousel components in this design system require specific ARIA roles for optimal screen reader support.
**Action:** Always apply role='region' and aria-roledescription='carousel' on the stage container, and role='group' with aria-roledescription='slide' on individual product cards.
