## 2024-05-24 - Custom Carousel Accessibility
**Learning:** Custom carousel components in the project require specific ARIA roles (region/carousel for container, group/slide for cards) to be properly announced by screen readers.
**Action:** Always apply role="region" and aria-roledescription="carousel" to carousel stages, and role="group" with aria-roledescription="slide" to product cards in future carousel implementations.
