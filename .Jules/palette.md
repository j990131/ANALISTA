## 2024-05-18 - Carousel ARIA Accessibility
**Learning:** Custom carousel components built natively without external libraries often lack structural meaning for screen readers. Merely adding 'aria-label' to navigation buttons is insufficient if the context (the carousel stage and slides) is missing.
**Action:** Always implement `role="region"` with `aria-roledescription="carousel"` on carousel containers, and `role="group"` with `aria-roledescription="slide"` on product cards for optimal screen reader support.
