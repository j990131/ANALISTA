## 2026-08-14 - Carousel Accessibility Improvements
**Learning:** Dynamic carousels (both React and Vanilla HTML) need synchronized ARIA attributes like `aria-selected` on tabs and `aria-live='polite'` on dynamically updated text containers for proper screen reader support. The dual implementation requires manual state syncing in vanilla JS compared to declarative React.
**Action:** Always map interactive carousel dots/cards to `role='tab'` with dynamic `aria-selected`, and ensure text changes are announced.
