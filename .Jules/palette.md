## 2024-05-24 - Dynamic ARIA labels for Spanish components
**Learning:** Adding accessibility attributes to dynamic JS UI components in this app requires explicit programmatic attributes (e.g., setAttribute) in Spanish since the target audience is Spanish-speaking.
**Action:** Always inject translated ARIA labels (e.g., 'Producto anterior', 'Siguiente producto') directly during DOM element creation loops for vanilla JS components.
