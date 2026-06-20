## 2024-11-20 - [ARIA Labels for Mapped React Elements]
**Learning:** When using Spanish or localized UI, dynamically rendered carousels using map() functions need accurately localized strings and indexes inside ARIA attributes (e.g., `aria-label={\`Ver producto \${i + 1}\`}`) so that assistive tech accurately voices the UI controls.
**Action:** Always ensure strings inside ARIA labels match the primary UI language, specifically injecting variables inside map functions to ensure each control has a uniquely identifiable localized label.
