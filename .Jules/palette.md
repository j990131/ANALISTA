## 2024-05-24 - Accessible Custom Carousel
**Learning:** Custom carousels need specific ARIA roles (region, carousel, group, slide) to be fully understood by screen readers, unlike native elements which have built-in accessibility semantics.
**Action:** Always add role="region" and aria-roledescription="carousel" to custom carousel containers, and role="group" and aria-roledescription="slide" to their individual slides.
