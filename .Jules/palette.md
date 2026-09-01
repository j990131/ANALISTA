## 2024-05-18 - Missing ARIA Labels on Carousel Controls
**Learning:** Custom carousels in this design system often use icon-only buttons for navigation ('‹', '›') and dots for pagination without accessible names, rendering them invisible to screen readers. Furthermore, interactive components are implemented both in React (JSX) and Vanilla JS, requiring a11y improvements to be synced across both implementations.
**Action:** Always verify both React components and their vanilla HTML equivalents when adding accessibility attributes like `aria-label` to custom interactive controls.
