## 2024-07-06 - Dental Promo Carousel Accessibility
**Learning:** Carousels that dynamically render DOM elements (like dots) need their ARIA attributes (`role`, `aria-label`, `aria-selected`) synchronized manually in vanilla JS, whereas React handles this declaratively. Additionally, screen readers need `aria-live="polite"` on dynamically changing product info to announce carousel changes.
**Action:** Always replicate React ARIA attribute updates inside the state update functions (like `setActive` or the rendering loops) of vanilla JS implementations to maintain parity.
