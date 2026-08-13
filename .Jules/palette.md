## 2024-08-13 - [Missing ARIA labels on Carousels]
**Learning:** In dual-implementation setups (HTML and React), icon-only navigation buttons and pagination dots frequently lack ARIA labels, making them inaccessible.
**Action:** Add descriptive ARIA labels (e.g., 'Producto anterior', 'Ver producto N') directly to both the static HTML elements and dynamically generated DOM components to ensure screen reader support.
