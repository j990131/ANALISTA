## 2024-05-15 - [Carousel Accessibility Improvement]
**Learning:** Custom carousel components built with vanilla JS require explicit DOM manipulation for ARIA state parity (`aria-selected`, `aria-live`) and descriptive roles (`aria-roledescription="carousel"/"slide"`) since they lack native React/framework state handling.
**Action:** Always verify keyboard focus states and implement explicit `aria-selected` toggling within vanilla JS updates or state update functions for dual/custom components.
