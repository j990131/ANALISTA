## 2024-05-18 - [Accessibility on Dynamic Content]
**Learning:** Carousels changing content visually require `aria-live="polite"` on the wrapper of the changed text to automatically announce updates to screen readers. Adding static ARIA attributes is not enough if screen readers are not alerted to content changes.
**Action:** Always wrap text that dynamically updates due to state changes (like product info in a carousel) with `aria-live="polite"` or `aria-live="assertive"`.
