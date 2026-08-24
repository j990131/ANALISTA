## 2024-08-24 - Accessibility for Icon-only Buttons
**Learning:** Found multiple instances of navigation arrows and dot indicators in carousels across the application (both vanilla HTML and React versions) that lacked ARIA labels, making them invisible or unclear to screen reader users.
**Action:** Always verify that icon-only buttons (`‹`, `›`, and empty dots) have descriptive `aria-label` attributes to ensure they are fully accessible to screen readers, and enforce this pattern in both vanilla HTML templates and React components.
