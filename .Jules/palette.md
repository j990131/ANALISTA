## 2026-08-06 - [Accessible Carousel Tabs]
**Learning:** Dynamic custom carousels with dot indicators require role="tablist" on the container and role="tab" with aria-selected states on the dots for proper screen reader support, especially when localized (e.g., Spanish ARIA labels).
**Action:** Always add tab roles and aria-selected syncing to custom dot paginators in Vanilla JS and React.
