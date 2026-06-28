
## 2024-05-24 - Accessibility upgrades for Dynamic Carousel
**Learning:** Carousels often rely purely on visual cues (like scaling or offsets) and `onClick` handlers for interactions, neglecting screen readers and keyboard users. State representations like "active dot" or "current product" require explicit mapping to semantic ARIA roles.
**Action:** Always provide explicit keyboard equivalents (e.g., `onKeyDown` watching for 'Enter' or ' ') alongside `onClick` on non-button interactable elements like custom cards. Additionally, map UI constructs logically: dot containers map to `role="tablist"`, individual dots to `role="tab"` with `aria-selected` tracking the active state, and dynamic text updating on interaction to `aria-live="polite"` regions.
