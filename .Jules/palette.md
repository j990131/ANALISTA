## 2024-08-09 - [Missing ARIA labels on navigation buttons]
**Learning:** Icon-only navigation buttons and dot indicators lack `aria-label` attributes, which impairs accessibility for screen readers in Spanish UI elements.
**Action:** Added explicit translated ARIA labels (e.g., 'Producto anterior', 'Producto siguiente') and dynamically interpolated labels for mapped elements (e.g., 'Ver producto ${i + 1}') to ensure accessibility.
