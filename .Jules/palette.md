## 2025-06-19 - DentalPromo Accessibility
**Learning:** The DentalPromo UI lacked critical screen reader context for its dynamic elements (carousel arrows, tab indicators, and updating product text). The usage of Spanish in the UI means accessibility labels should be translated accordingly for native screen readers.
**Action:** When working on dynamic carousels, always include localized `aria-label`s for navigation, `role="tablist"`/`role="tab"`/`aria-selected` for dot indicators, and `aria-live="polite"` for any text containers that update without a page load.
