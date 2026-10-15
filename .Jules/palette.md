## 2024-05-15 - Accessible Custom Carousels for Spanish Audience
**Learning:** Custom carousels built with vanilla JS DOM manipulation lack semantic structure for screen readers, and require proper ARIA attributes (`role="region"`, `aria-roledescription="carousel"` for the stage, and `role="group"`, `aria-roledescription="slide"` for the items) dynamically added via `setAttribute`, with labels in Spanish.
**Action:** Always verify if custom JS components apply the necessary semantic ARIA roles and labels natively, ensuring localization matches the target audience (e.g., Spanish for ANALISTA).
