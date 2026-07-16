## 2024-07-16 - DentalPromo Accessibility
**Learning:** Dynamic UI elements in this project (like carousels) lack screen reader support for navigation arrows, pagination dots, and dynamically updating text, requiring explicitly translated ARIA labels for accessibility.
**Action:** Add `aria-label`, `aria-live='polite'`, `role='tablist'`, and `role='tab'` with dynamic `aria-selected` attributes to similar marketing UI components in the future.
