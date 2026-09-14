## 2024-05-24 - Screen Reader Support for Custom Carousels
**Learning:** Custom carousel components in marketing promotional UI lack inherent screen reader context and require explicit ARIA roles (region/group) and roledescriptions (carousel/slide) for optimal navigation.
**Action:** Always apply role='region', aria-roledescription='carousel' to the stage and role='group', aria-roledescription='slide' to product cards in custom carousels.
