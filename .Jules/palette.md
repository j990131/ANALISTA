## 2024-09-07 - Carousel Accessibility Enhancements
**Learning:** Custom carousel components built with vanilla JS require dynamic DOM manipulation for ARIA attributes on cloned or dynamically generated cards, while the container shell needs static `role="region"` and `aria-roledescription="carousel"`.
**Action:** Ensure dynamic elements in standard project patterns get `.setAttribute()` applied immediately upon creation rather than waiting for render cycles.
