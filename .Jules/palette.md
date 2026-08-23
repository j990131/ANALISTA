## 2024-05-24 - Dynamic Carousel Accessibility
**Learning:** Carousel structures need hierarchical ARIA roles (region > group) for screen readers to interpret them correctly as sliders, while dynamic state elements (like pagination dots) benefit from tablist/tab patterns, and text updates require aria-live regions.
**Action:** Always implement this dual structure (carousel roledescriptions + tablist for dots + aria-live for text) for any custom promotional sliders in this design system.
