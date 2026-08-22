## 2024-08-22 - Carousel Accessibility Pattern
**Learning:** Custom carousels need specific ARIA roles (region, carousel, group, slide) and aria-live regions for dynamic text updates to be properly announced by screen readers.
**Action:** Always implement role="tablist"/role="tab" for carousel dots and aria-live="polite" for dynamic product information containers in custom vanilla JS components.
