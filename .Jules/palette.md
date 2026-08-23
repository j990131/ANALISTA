## 2023-10-27 - Carousel Pagination Accessibility
**Learning:** Icon-only navigation buttons (`‹` and `›`) and pagination dots are frequently implemented without ARIA labels, rendering them silent or confusing for screen reader users. Furthermore, pagination dots lack state indication.
**Action:** Always add descriptive `aria-label`s to icon-only controls. For pagination dots, include a dynamic `aria-current="true"` state to indicate the currently active slide, ensuring synchronization between the visual state and the accessibility tree in both vanilla JS and React implementations.
