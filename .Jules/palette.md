## 2024-07-26 - Accessible Spanish UI Carousels
**Learning:** Dynamic UI elements in this project require explicitly translated ARIA labels (e.g., 'Producto anterior') and dynamically interpolated labels for mapped elements (e.g., 'Ver producto ${i + 1}') to ensure accessibility.
**Action:** Always implement role="tablist", role="tab", aria-live="polite", and dynamic aria-selected in both React components and their corresponding standalone HTML versions for consistency.
