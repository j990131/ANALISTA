## 2024-05-18 - Localized ARIA Labels and Carousel Semantics
**Learning:** For custom carousels and UI components built in localized languages (like Spanish in DentalPromo), standard ARIA patterns (`role="tab"`, `aria-live="polite"`) must be paired with explicitly translated labels (e.g., `aria-label="Producto anterior"`, `aria-label="Ver producto 1"`) for true accessibility.
**Action:** Always ensure ARIA label text strictly matches the component's localization language and apply `aria-live="polite"` to dynamically changing product info areas.
