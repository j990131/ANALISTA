## 2023-10-25 - Carousel Accessibility
**Learning:** Custom carousel components in the project lacked screen reader support, requiring `role='region'` on the stage and `aria-roledescription='carousel'` for proper identification.
**Action:** Always add ARIA roles, labels, and live regions to custom interactive widgets like carousels to ensure accessibility for screen reader users.
