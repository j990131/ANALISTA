## 2024-06-08 - [A11y Spanish ARIA & Dynamic Text]
**Learning:** This app requires translated ARIA labels (e.g., "Producto anterior") for accessibility and `aria-live="polite"` on dynamically changing text containers (like the active product info) so screen readers gracefully announce changes as the carousel updates. Dynamic tabs also need properly calculated `aria-selected` and interpolated labels (e.g., `Ver producto ${i + 1}`).
**Action:** Always ensure ARIA labels match the primary language of the component and use `aria-live` regions when content updates without a page load.
