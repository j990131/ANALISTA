## 2024-05-24 - Add ARIA attributes to Carousel
**Learning:** Custom carousel components in this project frequently lack native accessibility features, requiring manual addition of ARIA roles and descriptions to ensure proper screen reader support.
**Action:** Always verify and manually add `role="region"`, `aria-roledescription="carousel"`, `role="group"`, and `aria-roledescription="slide"` to custom interactive components like carousels.
