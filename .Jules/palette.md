## 2024-06-16 - [Spanish ARIA Labels]
**Learning:** Carousels and interactive components require translated ARIA attributes matching the UI language (Spanish). Also, multi-file component structures (JSX and HTML previews) require synchronizing accessibility states.
**Action:** Always check the language context of the UI before applying `aria-label`s and ensure stateful elements like dots use `role="tab"` and `aria-selected` across all variations.
