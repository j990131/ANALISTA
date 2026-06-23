
## 2024-06-23 - Accessibility sync in React vs HTML standalone components
**Learning:** In projects where React components have corresponding standalone HTML versions (e.g., for simple preview or embedding), accessibility attributes like `aria-live`, `aria-selected` and `aria-label` often drift and must be manually synced between JSX mappings and vanilla JS DOM manipulations to maintain full parity.
**Action:** Always verify corresponding standalone HTML files (`dental-promo.html`, `preview.html`) when updating a React component's UI attributes.
