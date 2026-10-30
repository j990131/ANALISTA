## 2026-03-13 - Add aria-labels for slider buttons in dental promo
**Learning:** Found that custom web component carousels using pure DOM sometimes miss ARIA labels on simple UI control buttons, particularly icon-only next/prev navigation buttons or slider dot indicators.
**Action:** Adding explicit `aria-label` to slider navigation buttons and explicitly setting attributes via `setAttribute` for dynamic controls such as dot indicators.
