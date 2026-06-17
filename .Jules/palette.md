## 2026-06-17 - Localized ARIA Labels for A11y Components
**Learning:** When adding ARIA labels like 'Producto anterior' instead of 'Previous product' to UI elements (like paginators) in localized or single-language apps, it's critical to ensure the screen reader text matches the primary language of the UI to avoid confusing screen reader experiences.
**Action:** Always verify the language context of the UI and provide translated, localized strings for attributes like `aria-label` and interpolated labels (e.g., 'Ver producto ${i+1}') rather than assuming default English strings.
