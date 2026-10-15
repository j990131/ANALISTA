## 2024-05-18 - Accessibility on Custom Vanilla JS Components
**Learning:** For custom web components built with raw DOM manipulation (`document.createElement`), accessibility attributes (`role`, `aria-roledescription`, `aria-label`) should be set iteratively via `setAttribute` within the same loop that builds the component to ensure each item is properly announced to screen readers.
**Action:** Always verify that dynamically generated elements in vanilla JavaScript have `setAttribute` called during creation to apply appropriate ARIA roles and labels.
