## 2024-05-24 - Accessibility for Raw DOM Elements
**Learning:** When vanilla JavaScript dynamically constructs UI components using `document.createElement`, ARIA labels and semantic roles are often overlooked compared to declarative HTML, leaving screen readers with empty unlabelled buttons and div groups.
**Action:** Always verify if `document.createElement` loops correctly apply accessibility standards (like `.setAttribute("aria-label", ...)`) during component initialization.
