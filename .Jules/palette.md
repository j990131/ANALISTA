## 2025-06-05 - Missing ARIA Labels in Spanish Promos
**Learning:** Icon-only navigation buttons and indicator dots in the Spanish localized promotional components lacked ARIA labels. This breaks screen-reader accessibility, particularly since visually implicit indicators (like left/right chevrons or colored dots) have no semantic meaning to assistive tech.
**Action:** Always ensure that structural elements like carousel chevrons and pagination dots have localized `aria-label`s (e.g., "Producto anterior", "Siguiente producto", "Ver {item.name}") mapped dynamically when needed.
