## 2024-08-30 - Carousel Accessibility Pattern
**Learning:** Custom carousel components built with dynamic DOM injection require specific ARIA roles (region for stage, group for slides, tablist/tab for pagination) and aria-live='polite' for screen reader compatibility when elements animate or change dynamically.
**Action:** Always apply role='region', aria-roledescription='carousel', and synchronize aria-selected states on pagination dots when building non-native slider components.
