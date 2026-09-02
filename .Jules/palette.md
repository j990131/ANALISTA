## 2024-09-02 - Carousel accessibility
**Learning:** Carousels often use icon-only buttons for navigation ("<" and ">") and unlabelled dots for indicators, causing screen readers to announce "unlabelled button".
**Action:** Always add explicit `aria-label` attributes to icon-only carousel controls indicating their specific action (e.g., "Previous product", "Next product") and dot indicators (e.g., "Product 1").
