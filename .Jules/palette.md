## 2024-08-16 - Accessible Carousel implementation
**Learning:** Carousel components need `role="region"` with `aria-roledescription="carousel"` for the container, and `role="group"` with `aria-roledescription="slide"` for individual items. Dot indicators need `role="tablist"` and `role="tab"` with `aria-selected` to properly announce position and state to screen readers. Dynamic text containers like product names and descriptions should use `aria-live="polite"`.
**Action:** Add these aria roles and attributes by default to all carousel implementations.
