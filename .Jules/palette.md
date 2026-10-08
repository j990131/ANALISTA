## 2024-10-24 - Custom Carousel Accessibility
**Learning:** Custom carousel components built with vanilla JS often lack semantic meaning, causing them to be read poorly by screen readers.
**Action:** Always apply `role="region"` and `aria-roledescription="carousel"` to the container, use `role="group"` and `aria-roledescription="slide"` on individual items, and add descriptive `aria-label`s to all icon-only navigation buttons and dots.
