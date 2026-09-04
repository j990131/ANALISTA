## 2024-05-24 - Custom Carousel Accessibility
**Learning:** Custom UI carousels need specific ARIA roles to be recognized by screen readers. The stage container needs role='region' and aria-roledescription='carousel', while individual items need role='group' and aria-roledescription='slide'. Also, icon-only navigation elements (arrows, dots) require explicit aria-labels.
**Action:** Always verify ARIA attributes on custom carousel components, including navigation buttons, dots, and structural elements.
