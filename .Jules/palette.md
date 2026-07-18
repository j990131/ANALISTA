## 2024-05-15 - Accessibility issue pattern in DentalPromo
**Learning:** Carousel components (like DentalPromo) natively lack screen reader visibility, particularly missing Spanish translations for navigation and role='tablist' for dot indicators.
**Action:** Always inject explicitly translated aria-label attributes (e.g., 'Producto anterior', 'Ver producto ${i + 1}') and use aria-live='polite' on dynamically changing content containers to guarantee accessibility across dual HTML/React implementations.
