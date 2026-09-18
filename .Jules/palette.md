## 2024-09-18 - Custom Carousel Accessibility
**Learning:** Custom carousel components in this app's promo pages require explicit ARIA roles (region/carousel) and descriptions (slide) because they don't use native slider elements, causing screen readers to miss the interactive grouping.
**Action:** Always apply `role="region"`, `aria-roledescription="carousel"` to the stage container, and `role="group"`, `aria-roledescription="slide"` to the individual cards when building custom Javascript-driven carousels.
