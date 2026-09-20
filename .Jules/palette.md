## 2024-05-24 - Custom Carousel Accessibility Roles
**Learning:** Custom interactive carousels require explicit ARIA roles (role="region" and aria-roledescription="carousel" on the container, role="group" and aria-roledescription="slide" on items) to be properly interpreted by screen readers.
**Action:** Always add appropriate roles and aria-roledescriptions to custom carousels, and ensure nav buttons have aria-labels.
