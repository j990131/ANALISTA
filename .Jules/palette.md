## 2024-05-18 - Carousel Accessibility
**Learning:** Custom carousel components require specific ARIA attributes for optimal screen reader support, including role="region" and aria-roledescription="carousel" on the stage container, and role="group" and aria-roledescription="slide" on individual cards.
**Action:** Always add these specific roles and roledescriptions when building or modifying custom carousels, along with appropriate aria-labels for navigation buttons.
