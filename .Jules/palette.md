## 2026-09-24 - Carousel Accessibility Pattern
**Learning:** Custom carousel components built with vanilla JS require explicit ARIA roles (region/carousel for container, group/slide for items) and descriptive labels for screen reader compatibility.
**Action:** Always apply `role="region"` and `aria-roledescription="carousel"` on custom carousel stages, and `role="group"` with `aria-roledescription="slide"` on generated cards to ensure screen readers announce them properly.
