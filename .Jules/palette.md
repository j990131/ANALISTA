## 2024-10-25 - Missing ARIA labels in dynamic custom carousels
**Learning:** Icon-only navigation buttons and dynamically generated pagination dots in vanilla JS carousels frequently lack ARIA labels, making the interactive elements inaccessible to screen readers in this app's components.
**Action:** When building or reviewing custom carousels, ensure `aria-label` attributes are added to both static HTML navigation arrows and dynamically injected into DOM elements (using `setAttribute`) during loop iterations.
