## 2024-09-07 - Add accessibility to custom carousel
**Learning:** Custom carousel components in this app's components need specific roles and aria-roledescriptions for optimal screen reader support.
**Action:** Use role='region' and aria-roledescription='carousel' on the stage container, and role='group' with aria-roledescription='slide' on the individual product cards.
