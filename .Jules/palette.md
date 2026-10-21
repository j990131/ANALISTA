## 2024-10-21 - Added ARIA labels to carousel navigation
**Learning:** Custom vanilla JS carousels often lack ARIA attributes on pagination dots because they are generated dynamically.
**Action:** When generating interactive elements via `document.createElement`, iteratively set `aria-label` using `setAttribute` to ensure dynamic accessibility.
