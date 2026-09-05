## 2024-09-05 - Carousel Accessibility
**Learning:** Custom carousel components require role='region' and aria-roledescription='carousel' on the stage container, and role='group' with aria-roledescription='slide' on the individual product cards for optimal screen reader support.
**Action:** Always implement these specific ARIA roles when building custom interactive carousels instead of relying on default div semantics.
