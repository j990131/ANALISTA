## 2024-09-06 - Accessible Custom Carousel
**Learning:** Custom carousel components built manually with JavaScript or React map often lack screen-reader accessible roles and navigation labels, relying entirely on visual cues.
**Action:** When implementing custom carousels, always add role='region' and aria-roledescription='carousel' to the stage container, role='group' and aria-roledescription='slide' to the individual cards, and explicitly label next/previous controls using aria-label.
