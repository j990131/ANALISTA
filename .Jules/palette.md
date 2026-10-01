## 2024-05-24 - Accessible Carousel Component
**Learning:** Custom UI carousels need specific ARIA roles (`role="region"` and `aria-roledescription="carousel"` for the container, `role="group"` and `aria-roledescription="slide"` for items) to be correctly announced by screen readers, replacing non-semantic divs.
**Action:** Always add these specific ARIA roles and descriptions to any custom carousel implementation in the future to ensure screen reader compatibility.
