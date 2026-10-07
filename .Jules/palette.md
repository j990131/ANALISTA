## 2023-10-24 - Accessibility for Custom Carousels
**Learning:** Custom vanilla JS carousels require explicit ARIA roles (region for container, group for slides) and `aria-roledescription` (carousel/slide) to be properly interpreted by screen readers.
**Action:** Always add `role="region"`, `aria-roledescription="carousel"`, and context-specific `aria-label` attributes to custom interactive component containers in vanilla HTML/JS projects.
