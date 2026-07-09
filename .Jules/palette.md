## 2026-07-09 - Dynamic Carousel Accessibility
**Learning:** Dynamic carousels require `aria-live` for text changes to be announced. Spanish UI requires translated ARIA labels (e.g. 'Producto anterior'). Interactive dots need `role="tab"`, `aria-selected`, and a grouping `role="tablist"` container.
**Action:** Apply these patterns consistently across React and standalone HTML files when building carousels.
