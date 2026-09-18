## 2024-09-18 - Added ARIA attributes to custom carousel
**Learning:** Custom carousel components built with vanilla JS require explicit `role="region"`, `aria-roledescription="carousel"`, and focusable slide/dot elements with descriptive `aria-label`s for screen reader support.
**Action:** Always apply standard ARIA roles and descriptions when building custom non-native interactive UI elements like carousels.
