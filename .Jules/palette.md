## 2024-05-18 - Custom Carousel Accessibility
**Learning:** Custom carousel components in this project require specific ARIA roles (role='region' with aria-roledescription='carousel' on the stage, and role='group' with aria-roledescription='slide' on cards) to be properly interpreted by screen readers.
**Action:** Always apply these specific roles and aria-roledescriptions to custom carousels instead of relying on generic group or list roles.
