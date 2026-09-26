## 2024-11-20 - Carousel Accessibility Fixes
**Learning:** Custom carousel components in vanilla JS require explicit DOM manipulation for ARIA roles (region, group) and descriptions (carousel, slide) to ensure proper screen reader navigation.
**Action:** Always verify that dynamic carousel elements are instantiated with semantic attributes like role='group' and aria-label='...' during DOM creation, not just styled visually.
