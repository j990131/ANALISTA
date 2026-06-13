## 2024-05-24 - Accessibility for Spanish UIs
**Learning:** Dynamically updating Spanish UI components require explicitly translated ARIA labels (e.g., 'Producto anterior', 'Ver producto ${i+1}') and `aria-live='polite'` on product info containers to ensure accessibility.
**Action:** Always verify ARIA label translations and add `aria-live` to dynamic components.
