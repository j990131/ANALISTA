## 2024-09-09 - Carousel Accessibility
**Learning:** Custom carousel components built with vanilla JS require dynamic ARIA attributes (role="group", aria-roledescription="slide") applied to the individual generated elements (cards), in addition to the static container roles, for optimal screen reader support.
**Action:** Always ensure dynamic UI components update their accessibility tree state in tandem with the visual DOM manipulation.
