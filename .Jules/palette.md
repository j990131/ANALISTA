## 2024-05-18 - Carousel Accessibility Pattern
**Learning:** Custom carousel components need specific ARIA roles to be properly announced by screen readers.
**Action:** Always add role="region" and aria-roledescription="carousel" to the stage container, and role="group" and aria-roledescription="slide" to the dynamically generated individual product cards.
