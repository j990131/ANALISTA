## 2024-05-15 - Accessible Custom Carousels
**Learning:** Custom carousel components need specific ARIA roles to be properly identified by screen readers, such as role="region" and aria-roledescription="carousel" on the stage container, and role="group" with aria-roledescription="slide" on cards.
**Action:** Always apply these standard roles to custom carousels, and ensure all navigation buttons and dots have explicit aria-labels.
