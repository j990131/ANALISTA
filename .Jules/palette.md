## 2024-05-24 - Carousel Accessibility Pattern
**Learning:** Custom carousels in this app frequently lack appropriate ARIA roles and descriptions, reducing screen reader compatibility.
**Action:** Always apply role="region", aria-roledescription="carousel" on the carousel container and role="group", aria-roledescription="slide" on the individual items.
