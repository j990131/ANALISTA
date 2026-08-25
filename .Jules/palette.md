## 2024-08-25 - Carousel Accessibility Pattern
**Learning:** Dynamic UI elements like carousels need specific ARIA roles (region, carousel, group, slide) and dynamic state management (aria-selected, aria-live) for screen reader support in both vanilla HTML and React.
**Action:** Always include role="region" and aria-roledescription="carousel" on stage containers, role="group" on slides, and manage aria-selected states for pagination tabs manually when using vanilla HTML.
