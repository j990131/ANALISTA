## 2024-06-25 - Carousel Accessibility Pattern
**Learning:** Custom carousels lacking standard semantic HTML require explicit ARIA roles (`region`, `group`) and roledescriptions (`carousel`, `slide`) for screen reader compatibility, along with distinct `aria-label`s on navigation buttons to avoid icon-only ambiguity.
**Action:** Always verify custom interactive components (like carousels or tabs) against WAI-ARIA authoring practices, dynamically injecting roles and descriptive labels when building DOM elements via JavaScript.
