## 2024-05-20 - Carousel Accessibility Patterns
**Learning:** Dynamic UI elements like carousels need specific ARIA roles (region, group, tablist, tab) and dynamic state management (aria-selected, aria-live) across both HTML and React implementations to be properly interpreted by screen readers.
**Action:** Always verify dual implementations have manual state sync (e.g. keydown handlers, setAttribute for aria-selected) in vanilla HTML to match React's declarative behavior.
