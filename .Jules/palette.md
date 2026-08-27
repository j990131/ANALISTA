## 2024-05-24 - Accessibility for Dynamic Vanilla JS Carousels
**Learning:** For interactive accessibility in dual implementations (vanilla HTML vs React components), state attributes like aria-selected and focus management must be manually implemented and synced via JavaScript in the vanilla HTML versions to achieve parity with React's declarative behavior.
**Action:** Always manually apply aria-selected dynamically and use setAttribute() for roles like 'tab' and 'group' on dynamically generated DOM elements.
