## 2024-11-04 - Screen Reader Support for Promotional Carousel
**Learning:** Icon-only navigation buttons and dynamically generated carousel cards/indicators lack context for screen readers in vanilla JS implementations.
**Action:** Always add Spanish `aria-label`s to navigation arrows and dynamically generated dot buttons, and add `role="group"` with `aria-roledescription="diapositiva"` to carousel cards to ensure a fully accessible experience for the target Spanish-speaking audience.
