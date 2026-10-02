## 2024-10-24 - Custom Carousel Accessibility
**Learning:** Custom diagonal carousels require explicit ARIA roles (region/carousel and group/slide) for optimal screen reader support, as their DOM structure doesn't inherently convey list semantics.
**Action:** Always add role='region' and aria-roledescription='carousel' to the stage container, and role='group' with aria-roledescription='slide' to the individual cards in custom carousel implementations.
