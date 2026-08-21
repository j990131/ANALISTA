## 2024-05-18 - Interactive Vanilla JS Carousels
**Learning:** Vanilla HTML implementations of interactive components like carousels lack the declarative state management of React, meaning dynamic accessibility attributes like aria-selected and aria-live content must be carefully synchronized via JavaScript on every render cycle to maintain parity with screen readers.
**Action:** Always verify that stateful ARIA attributes (e.g. aria-selected) are explicitly toggled in the vanilla JS render loop when updating interactive DOM elements.
