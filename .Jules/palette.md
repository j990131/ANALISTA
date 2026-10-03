## 2024-10-03 - Carousel Accessibility
**Learning:** Custom carousels in this app lack explicit ARIA roles and labels, causing screen readers to miss the carousel structure and navigation controls.
**Action:** Always apply role="region", aria-roledescription="carousel" on stages, role="group", aria-roledescription="slide" on cards, and aria-labels on icon-only nav buttons.
