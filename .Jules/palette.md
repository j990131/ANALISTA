## 2024-05-18 - Missing ARIA attributes on custom carousels
**Learning:** Custom carousel components in this project frequently lack proper ARIA roles (`role="region"`, `aria-roledescription="carousel"`) and slide group roles, making them completely unnavigable and meaningless for screen reader users.
**Action:** Always explicitly define `role="region"` and `aria-roledescription="carousel"` on the carousel container, and `role="group"` and `aria-roledescription="slide"` on individual generated items.
