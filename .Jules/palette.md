## 2024-05-18 - [Carousel Accessibility]
**Learning:** Carousel widgets frequently lack required ARIA attributes, making them inaccessible to screen readers.
**Action:** Always add `role="region"`, `aria-roledescription="carousel"`, and `aria-label` to the carousel container. Add `role="group"`, `aria-roledescription="slide"`, and `aria-label` to individual slides. Ensure navigation buttons have descriptive `aria-label`s.

## 2024-09-23 - [Icon Button Accessibility]
**Learning:** Icon-only navigation buttons in the dental promo carousel lack text alternatives for screen readers.
**Action:** Always add descriptive `aria-label`s to icon-only buttons to ensure they are announced correctly to assistive technologies.
