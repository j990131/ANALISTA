## 2024-05-24 - Custom Carousel Accessibility
**Learning:** Custom carousel components require specific ARIA roles for optimal screen reader support: role='region' and aria-roledescription='carousel' on the stage container, and role='group' with aria-roledescription='slide' on the individual product cards.
**Action:** Always apply these roles and roledescriptions when enhancing custom carousels, alongside ARIA labels for navigation buttons.
