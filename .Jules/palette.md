## 2024-05-23 - Custom Carousel Accessibility
**Learning:** Custom carousel components in this app's design system require specific ARIA attributes (`role='region'`, `aria-roledescription='carousel'` on the container, and `role='group'`, `aria-roledescription='slide'` on the items) for optimal screen reader support.
**Action:** Always apply these specific ARIA roles and descriptions to any custom carousel components moving forward.
