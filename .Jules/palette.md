## 2025-01-01 - Carousel ARIA Semantics
**Learning:** Custom carousel components built with vanilla JS require explicit ARIA roles (region, group) and aria-roledescription (carousel, slide) alongside aria-labels to be properly announced by screen readers.
**Action:** Always add role="region" and aria-roledescription="carousel" to custom carousel containers, and role="group" with aria-roledescription="slide" to its children cards.
