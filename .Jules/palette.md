## 2024-10-24 - Custom Carousel Accessibility
**Learning:** Custom carousels in promotional components lack standard screen reader cues, making them appear as generic un-navigable elements.
**Action:** Always apply `role="region"` and `aria-roledescription="carousel"` to the carousel container, and `role="group"` with `aria-roledescription="slide"` to individual slides for optimal screen reader support.
