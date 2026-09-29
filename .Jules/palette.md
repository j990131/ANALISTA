## 2024-05-24 - Carousel Accessibility
**Learning:** Custom carousel components in this project need explicit ARIA roles (region/group) and roledescriptions (carousel/slide) to be properly interpreted by screen readers.
**Action:** Always add role="region" and aria-roledescription="carousel" to the stage, and role="group" with aria-roledescription="slide" to product cards.
