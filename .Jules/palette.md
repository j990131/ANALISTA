## 2024-05-24 - Custom Carousel Accessibility
**Learning:** Custom carousel components in this project lack native screen reader semantics, causing them to be read as unstructured content rather than an interactive gallery.
**Action:** Always apply role="region" and aria-roledescription="carousel" to the stage container, and role="group" with aria-roledescription="slide" on individual cards to ensure optimal screen reader support.
