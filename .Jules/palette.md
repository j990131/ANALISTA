## 2023-10-27 - Carousel Accessibility
**Learning:** Dynamic UI elements like carousels require explicit ARIA roles (region, tablist, tab, group) and states (aria-selected, aria-live) to be accessible to screen readers, especially when custom DOM elements are used for stages and pagination dots.
**Action:** Always apply role='tablist' to dot containers, role='tab' and aria-selected to individual dots, and aria-live='polite' to dynamically changing text regions in future carousel implementations.
