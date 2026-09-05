## 2024-09-05 - Custom Carousel Accessibility
**Learning:** Custom carousels in this project lack native screen reader semantics, causing them to be read as generic groups of elements without context.
**Action:** Always add `role="region"` and `aria-roledescription="carousel"` to the stage container, and `role="group"` with `aria-roledescription="slide"` to individual product cards.
