## 2024-07-27 - Added Missing ARIA Labels to Navigation Controls
**Learning:** Carousels and product galleries in this app's components frequently omit ARIA labels on navigation buttons (prev/next) and dot indicators. Since these are icon-only or visual-only buttons, screen reader users cannot identify their purpose.
**Action:** Always verify ARIA labels on `<button>` elements, especially those containing only arrows (‹/›) or used as pagination dots. Map them with appropriate labels like 'Producto anterior' and 'Producto siguiente' based on the app's Spanish localization.
