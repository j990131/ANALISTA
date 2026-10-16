## 2024-05-24 - Dynamic ARIA Labels in Vanilla JS
**Learning:** In Spanish-localized vanilla JS custom web components, dynamically generated pagination dots and icon-only navigation arrows frequently lack `aria-label`s, preventing screen readers from understanding the carousel controls.
**Action:** Always iteratively add translated `aria-label` attributes (e.g., `setAttribute`) when dynamically building carousel navigation in DOM loops.
