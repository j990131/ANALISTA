## 2024-05-24 - Dynamic Carousel Accessibility
**Learning:** Carousels need explicit screen reader roles (`role='tablist'` / `role='tab'`) and dynamic state updates like `aria-selected`. A common pitfall is dynamic content containers lacking `aria-live='polite'`, which causes screen readers to silently miss product detail changes during navigation.
**Action:** Always ensure dynamic description containers in carousels use `aria-live='polite'` and navigation dots manage `aria-selected` state explicitly in both React and Vanilla JS.
