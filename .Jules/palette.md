## 2024-05-18 - Missing ARIA labels on dynamic icon buttons
**Learning:** Found that custom vanilla JS web components (like the carousel dots) often lack accessible names because they are generated dynamically without text content.
**Action:** When creating raw DOM elements iteratively (e.g., `document.createElement('button')`) for UI components, always ensure `setAttribute("aria-label", ...)` is included within the same loop if the element only contains visual indicators (like dots or icons).
