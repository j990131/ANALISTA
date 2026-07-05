## 2025-07-05 - ARIA Parity in Vanilla HTML vs React Components
**Learning:** When adding accessibility attributes to dynamic components (like a custom carousel) implemented in both Vanilla JavaScript/HTML and React, state-driven ARIA properties (like `aria-selected`) must be manually synced via imperative DOM operations in the vanilla implementation to achieve parity with the declarative React rendering.
**Action:** Always verify state updates in vanilla scripts manually set corresponding ARIA attributes rather than just adding static attributes to the initial markup.
