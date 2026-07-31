## 2024-07-31 - Accessible Carousel ARIA Attributes
**Learning:** In Spanish UI implementations of custom carousels, role mapping (role="region", aria-roledescription="carousel", role="group", aria-roledescription="slide") and Spanish localized aria-labels must be synced between standalone HTML and React components to maintain screen reader accessibility.
**Action:** Always verify dual implementations to ensure state attributes like aria-selected and keyboard handlers are explicitly implemented in vanilla HTML to match Reacts declarative behavior.
