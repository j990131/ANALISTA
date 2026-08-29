## 2024-05-19 - Dynamic Carousel Accessibility
**Learning:** Native DOM manipulation for carousels in this app requires explicit tracking of `aria-selected` state for pagination dots in addition to standard `role="tab"` and `role="tablist"` attributes.
**Action:** When adding accessibility to purely vanilla JS components, always ensure dynamic state changes (like `active` index) are synced to ARIA attributes in the render loop.
