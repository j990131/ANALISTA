## 2023-08-28 - ARIA Setup for Custom Dual Carousel Components
**Learning:** Adding accessible ARIA roles and attributes to a custom HTML/Vanilla JS vs React implementation of the same component requires mirroring both the markup and the dynamic JavaScript logic to ensure screen readers correctly interpret the dynamically updating tab and slide structure.
**Action:** When working on components that have dual implementation (vanilla + react) within the codebase, explicitly ensure the vanilla script modifies all `aria-selected` roles manually that react renders declaratively.
