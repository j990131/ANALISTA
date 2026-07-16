## 2024-05-20 - Missing ARIA Labels on Carousel
**Learning:** Carousel navigation, dots and dynamic content containers need explicit ARIA roles, labels and attributes in Spanish to be accessible for screen readers, and vanilla HTML scripts require explicit aria-selected management.
**Action:** Added aria-label to buttons, role="tablist", role="tab", aria-selected to dots, and aria-live="polite" to the product info container to improve accessibility.
