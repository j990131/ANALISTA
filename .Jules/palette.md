## 2024-09-14 - Carousel ARIA Accessibility Pattern
**Learning:** Custom carousels frequently miss critical ARIA roles and labels on navigation buttons (icon-only), stage (region), and cards (group/roledescription), which makes them inaccessible to screen readers.
**Action:** When inspecting carousels in marketing promos, actively look for role="region", aria-roledescription="carousel", and ensure icon-only arrows have clear `aria-label`s.
