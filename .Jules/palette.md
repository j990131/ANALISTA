## 2023-10-24 - Added ARIA attributes to dental promo carousel
**Learning:** Custom carousel components built with vanilla JS often lack structural accessibility; using 'region' and 'carousel' on the container, alongside dynamic 'group'/'slide' on generated items, bridges this gap without affecting visual styles.
**Action:** Always verify that dynamic DOM creation scripts include explicit `setAttribute` calls for ARIA roles when building custom interactive widgets.
