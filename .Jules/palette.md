## 2024-07-18 - Accessibility on Dental Promo Carousel
**Learning:** Carousels and auto-updating interfaces require specific ARIA roles to be accessible, such as `role="tablist"` and `role="tab"` for dot indicators with `aria-selected`, translated `aria-label` attributes for icon-only navigation buttons, and `aria-live="polite"` for text areas that update dynamically.
**Action:** When implementing standalone and React-based carousels, assure that ARIA roles and properties correctly match the user language (e.g., Spanish) to guarantee seamless interaction with screen readers.
