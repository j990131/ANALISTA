
## 2024-06-06 - [A11y] Localized ARIA Labels for Icon Buttons in Spanish Promos
**Learning:** Icon-only navigation buttons and dot indicators in Spanish UI components require explicitly translated ARIA labels (e.g., "Producto anterior", "Ver producto N") to maintain context for screen reader users. The dot indicators mapping often requires dynamically setting the `aria-label` attribute using interpolation (e.g., `\`Ver producto \${i + 1}\``) to indicate which specific product will be selected.
**Action:** When auditing React or vanilla HTML carousels, always verify that `aria-label` is present on `nav-prev`, `nav-next`, and dynamically generated dot indicator buttons, and ensure the labels are localized to match the language of the surrounding component.
