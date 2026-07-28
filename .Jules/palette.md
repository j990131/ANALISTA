## 2024-07-28 - Accessible Spanish Carousels
**Learning:** Carousels in this project are highly dynamic. We must use Spanish translations for ARIA roles, provide dynamically interpolated labels for mapped pagination items, and utilize aria-live='polite' on changing text regions.
**Action:** Always verify components both in vanilla HTML and React, ensuring state synchronization for aria-selected and role updates manually in the vanilla versions.
