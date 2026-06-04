## 2024-06-04 - Localized Context is Important for A11y

**Learning:** When making accessibility improvements in localized applications (like the Spanish DentalPromo page), generic english `aria-labels` are harmful. Screen readers will read English labels with Spanish pronunciation, which can be very confusing to end users.

**Action:** Ensure all `aria-label` text completely matches the language of the surrounding component.
