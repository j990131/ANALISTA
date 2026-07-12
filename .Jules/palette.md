## 2024-07-12 - Dental Promo UI Accessibility Improvements
**Learning:** Carousels and their navigation controls often lack ARIA roles and labels, impacting accessibility. Icon-only buttons ('‹' and '›') need descriptive labels. Product descriptions should be announced when updated dynamically.
**Action:** Always add 'aria-label' to icon-only buttons. Use 'role="tablist"' and 'role="tab"' for custom dot indicators. Use 'aria-live="polite"' on dynamic text content sections.
