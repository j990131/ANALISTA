## 2024-05-15 - ARIA roles for custom carousels
**Learning:** Custom carousel components built with divs need explicit semantic roles (region, group) and aria-roledescriptions (carousel, slide) since they lack native semantics.
**Action:** Always add role="region" and aria-roledescription="carousel" on the stage container, and role="group" with aria-roledescription="slide" on individual cards for optimal screen reader support.
