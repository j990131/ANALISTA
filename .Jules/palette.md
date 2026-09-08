## 2024-09-08 - Custom Carousel Accessibility
**Learning:** Custom carousel components in the project require specific ARIA attributes (role='region' and aria-roledescription='carousel' on the stage container, and role='group' with aria-roledescription='slide' on the individual product cards) for optimal screen reader support.
**Action:** When enhancing custom carousels, apply these specific roles and aria-roledescriptions in addition to standard aria-labels.
