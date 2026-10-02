## 2024-10-02 - Custom Carousel Screen Reader Support
**Learning:** Custom carousel components built without libraries require strict manual ARIA mapping (`role='region'`, `aria-roledescription='carousel'`, and `role='group'`/`aria-roledescription='slide'` for items) to be parsed correctly by screen readers, otherwise they are just announced as generic containers.
**Action:** Always verify custom interactive widgets like carousels get explicit ARIA roles and roledescriptions when they aren't using native structural elements like lists or standard buttons.
