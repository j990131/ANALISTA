## 2024-07-17 - Dual Implementation Accessibility Sync
**Learning:** Carousels in dual implementations (vanilla HTML vs React) require manual JavaScript syncing of `aria-selected` attributes and `aria-live="polite"` regions in vanilla HTML to match React's declarative behavior.
**Action:** Always verify that state attributes like `aria-selected` and `aria-live` announcements are manually synchronized via JavaScript when porting React components to standalone HTML previews.
