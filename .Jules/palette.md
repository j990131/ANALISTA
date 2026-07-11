## 2024-05-24 - Accessibility for dynamic UI carousels
**Learning:** Dynamic UI elements in this project like carousels require explicit ARIA translation (e.g. "Producto anterior") and must utilize role="tablist", role="tab", aria-selected, and aria-live="polite" to maintain screen reader accessibility.
**Action:** Always replicate React ARIA property syncs (like aria-selected logic and labels) identically in corresponding vanilla HTML previews.
