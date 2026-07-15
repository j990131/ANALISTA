## 2026-07-15 - Accessibility Parity in Vanilla JS
**Learning:** Implementing interactive accessibility (like aria-selected on tabs) in dual implementations requires manual DOM state synchronization in vanilla HTML compared to React's declarative behavior.
**Action:** Always verify that state-driven ARIA attributes are manually toggled in the vanilla JS render loop when porting React components.
