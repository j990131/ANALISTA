## 2024-07-13 - Dental Promo Accessibility
**Learning:** Dynamic carousels require `aria-live="polite"` on info containers so screen readers announce changes, and icon-only navigation needs translated `aria-label` attributes for non-English UIs.
**Action:** Always verify that interactive elements in custom carousels have proper ARIA attributes, especially in multi-language projects.
