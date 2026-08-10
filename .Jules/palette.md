## 2024-10-24 - Carousels require ARIA structure
**Learning:** Dynamic UI elements like carousels need explicit ARIA roles (region, carousel, group, slide) and live regions (aria-live) for screen readers, as well as translated labels.
**Action:** Always add tablist/tab roles for dots, and polite live regions for dynamically updating text.
