## 2024-08-12 - Dental Promo Carousel Accessibility
**Learning:** Dynamic UI elements like carousels need explicit ARIA roles (region, carousel, group, slide) and aria-live regions for dynamic text updates to be accessible. Vanilla JS implementations require manual syncing of state attributes like aria-selected.
**Action:** Always verify dual implementations (React and Vanilla JS) for consistent accessibility enhancements, particularly focusing on manual DOM attribute management in Vanilla JS.
