## 2024-05-24 - Accessibility attributes for carousels
**Learning:** Carousels need dynamic ARIA attributes (`aria-selected`, `aria-label`, `role="tablist"` and `role="tab"`) synced with state. `aria-live="polite"` is important for dynamic text updates like product info. Vanilla HTML implementations require manual attribute syncing on render, whereas React handles it declaratively.
**Action:** Always verify dual implementations (React vs Vanilla HTML) sync state attributes correctly. Add appropriate ARIA labels for icon-only buttons.
