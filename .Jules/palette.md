## 2024-09-26 - Custom Carousel Accessibility
**Learning:** Custom carousel components in this project lack native semantic structure, making them inaccessible to screen readers without proper roles.
**Action:** Always add role='region', aria-roledescription='carousel' to the stage container, and role='group', aria-roledescription='slide' to product cards.
