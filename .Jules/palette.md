## 2024-03-24 - [Carousel Accessibility]
**Learning:** Custom carousel components in the project lacked essential ARIA roles (`region`, `carousel`, `slide`, `tablist`, `tab`) and dynamic state attributes (`aria-selected`, `aria-live`).
**Action:** Always ensure that custom built carousels are fully annotated with ARIA attributes and that dynamic states (like `aria-selected` on dots and `aria-live` on text containers) are updated alongside visual changes in both React and vanilla JS implementations.
