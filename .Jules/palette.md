
## 2024-06-18 - Dynamically Interpolated ARIA Labels and HTML Replication
**Learning:** In projects with multiple standalone HTML representations of UI components, dynamically interpolated ARIA labels in non-English interfaces (e.g., Spanish `Ver producto ${i + 1}`) need to be manually synchronized across React component code (JSX) and Vanilla JS DOM manipulation scripts to maintain consistent accessibility.
**Action:** When adding ARIA labels to dynamically mapped elements in a multi-file setup, verify that Vanilla JS implementations replicate the JSX template literals using exact string concatenation (`d.setAttribute("aria-label", "Ver producto " + (i + 1));`) and ensure dynamic attributes like `aria-selected` are properly toggled in custom render loops.
