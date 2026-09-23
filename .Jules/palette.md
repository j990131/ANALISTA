## 2023-10-25 - Custom Carousel Accessibility
**Learning:** Custom carousel components in this project lack native accessibility features, requiring explicit ARIA roles (region/carousel for container, group/slide for items) to support screen readers properly.
**Action:** Always apply `role="region"`, `aria-roledescription="carousel"` on custom carousel containers and `role="group"`, `aria-roledescription="slide"` on their items during micro-UX enhancements.
