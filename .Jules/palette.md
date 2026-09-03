## 2024-05-24 - Accessibility improvements for carousel
**Learning:** Custom carousel components in this project lack screen reader support for stage container, slides, and navigation dots. Also, icon-only navigation buttons miss ARIA labels.
**Action:** Always add role='region' and aria-roledescription='carousel' on carousel containers, role='group' and aria-roledescription='slide' on product cards, aria-label to icon-only buttons, and aria-label with aria-current on pagination dots.
