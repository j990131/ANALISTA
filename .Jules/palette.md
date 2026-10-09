## 2024-05-24 - Custom Carousel Accessibility
**Learning:** Custom carousel components in this project frequently lack proper structural semantics (like role='region', role='group', and aria-roledescription) and label associations for screen readers on dynamic elements like cards and dot indicators.
**Action:** When working on custom carousels, always ensure the container has role='region' and aria-roledescription='carousel', cards have role='group' and aria-roledescription='slide', and dynamically created navigation elements (like dots) receive explicit ARIA labels.
