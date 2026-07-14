## 2026-07-14 - DentalPromo Carousel Accessibility
**Learning:** Carousels and dynamic product info containers require explicit `role="tablist"`/`role="tab"` relationships with `aria-selected` state management and `aria-live="polite"` for screen readers to properly interpret the active items and updates in Spanish.
**Action:** Always add ARIA roles, states, localized labels, and live regions to dynamic carousel components in both React and vanilla HTML implementations.
