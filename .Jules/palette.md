## 2024-05-20 - Carousel Accessibility Requirements
**Learning:** Custom carousel components lack foundational ARIA roles by default. A full implementation requires `role="region"` and `aria-roledescription="carousel"` on the wrapper, and `role="group"` with `aria-roledescription="slide"` on the individual items for optimal screen reader support.
**Action:** Always verify both structural and interactive ARIA attributes when encountering custom carousels, ensuring the container hierarchy and control elements are fully labeled.
