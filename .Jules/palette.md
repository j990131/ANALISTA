## 2024-11-20 - [A11y] Screen Reader Friendly Carousels in Spanish
**Learning:** For interactive UI elements (like carousels and paginators) localized in Spanish, relying solely on icons or unlabelled elements ignores a huge segment of users. Furthermore, syncing states like `aria-selected` manually is critical when dealing with dual implementations (React vs Vanilla JS).
**Action:** Always provide explicitly translated `aria-label`s on icon-only buttons (e.g. "Producto anterior") and use `aria-live="polite"` on dynamic text containers so content is properly announced.
