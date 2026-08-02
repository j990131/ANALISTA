## 2024-08-02 - ARIA Roles for Dynamic UI Elements
**Learning:** Dynamic UI elements like carousels need specific ARIA roles (`role="tablist"`, `aria-live="polite"`, etc.) and translated labels for accessibility in non-English apps.
**Action:** Always ensure dual implementations (React and vanilla HTML) have synchronized state attributes (`aria-selected`) and proper localized ARIA labels.
