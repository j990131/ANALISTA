## 2024-05-24 - Carousel Screen Reader Support
**Learning:** Custom carousel components built with divs often lack semantic meaning for screen readers, making navigation impossible without ARIA roles.
**Action:** Apply `role="region"` with `aria-roledescription="carousel"` on the stage, and `role="group"` with `aria-roledescription="slide"` on the cards, and add explicit `aria-label`s to icon-only navigation buttons and pagination dots.
