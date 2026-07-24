## 2024-07-24 - Accessible Carousels
**Learning:** Dynamic carousels require explicit ARIA roles and live regions for screen readers. The UI components are in Spanish and require explicitly translated ARIA labels.
**Action:** Always apply role='tablist' to dot containers, aria-live='polite' to dynamic text, and translate dynamic labels like `Ver producto ${i + 1}`.
