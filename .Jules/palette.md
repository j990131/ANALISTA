## 2024-05-24 - Custom Carousel Accessibility
**Learning:** Custom carousel components in this project require specific ARIA roles to ensure optimal screen reader support: `role="region"` and `aria-roledescription="carousel"` on the stage container, and `role="group"` with `aria-roledescription="slide"` on individual product cards.
**Action:** Always apply these specific ARIA attributes when implementing or updating custom carousel components to ensure consistent accessibility.
