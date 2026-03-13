# CLAUDE.md — AI Assistant Guide for ANALISTA

This file provides context, conventions, and workflows for AI assistants (Claude and others) working in this repository.

---

## Project Overview

**ANALISTA** is an iOS application built with SwiftUI, targeting iPhone (currently shown running on iPhone 17 Pro Max / iOS 26.2). The app features a promotional/marketing UI for food and beverage products, including carousel-style product displays, weekend deals, and buy-one-get-one promotions.

### Visual Design Language
- Warm gradient backgrounds (peach/salmon tones)
- Serif + script font pairings for promotional copy
- Oversized product imagery with soft drop shadows
- Pill-shaped CTA buttons with decorative diamond dividers
- Color accent: amber/orange (`#F5A623` range) for product names and interactive elements

---

## Repository Structure

```
ANALISTA/
├── CLAUDE.md                  # This file
├── ANALISTA.xcodeproj/        # Xcode project configuration
├── ANALISTA/
│   ├── App/
│   │   ├── ANALISTAApp.swift  # @main entry point
│   │   └── ContentView.swift  # Root view
│   ├── Features/
│   │   ├── Promotions/        # Weekend deals, BOGO screens
│   │   ├── Menu/              # Product catalog
│   │   └── Orders/            # Cart and checkout
│   ├── Models/                # Data models (Product, Promotion, etc.)
│   ├── Views/
│   │   ├── Components/        # Reusable UI components
│   │   └── Screens/           # Full-screen views
│   ├── Resources/
│   │   ├── Assets.xcassets/   # Images, colors, icons
│   │   └── Fonts/             # Custom typefaces
│   └── Preview Content/       # SwiftUI preview assets
├── ANALISTATests/             # Unit tests (XCTest)
└── ANALISTAUITests/           # UI tests (XCUITest)
```

> **Note:** This structure reflects the intended layout. Update this section as the project evolves.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Swift 6+ |
| UI Framework | SwiftUI |
| Minimum Deployment | iOS 17.0+ |
| IDE | Xcode 16+ |
| Dependency Manager | Swift Package Manager (SPM) |
| Testing | XCTest + XCUITest |
| CI/CD | (TBD — add when configured) |

---

## Development Workflows

### Building & Running

```bash
# Open project in Xcode
open ANALISTA.xcodeproj

# Build from CLI (substitute scheme/destination as needed)
xcodebuild -scheme ANALISTA -destination 'platform=iOS Simulator,name=iPhone 17 Pro Max' build

# Run tests
xcodebuild test -scheme ANALISTA -destination 'platform=iOS Simulator,name=iPhone 17 Pro Max'
```

### Branch Strategy

| Branch pattern | Purpose |
|---|---|
| `main` | Stable, production-ready code |
| `develop` | Integration branch for features |
| `feature/<name>` | New features |
| `fix/<name>` | Bug fixes |
| `claude/<description>-<id>` | AI-assisted changes (auto-named) |

All AI-generated changes land on `claude/` branches and are reviewed before merging.

### Commit Messages

Follow Conventional Commits:

```
feat: add weekend promotion carousel
fix: correct price formatting for BOGO label
refactor: extract ProductCardView to reusable component
style: update accent color to match brand palette
test: add unit tests for PromotionViewModel
```

---

## Code Conventions

### Swift / SwiftUI

- Use `struct` for views; `class` only when reference semantics are needed.
- Prefer `@State` / `@Binding` / `@ObservableObject` / `@Observable` (Swift 5.9+) appropriately.
- Views should stay thin — extract business logic into ViewModels or Services.
- Name views descriptively: `WeekendPromotionBannerView`, `ProductCarouselView`.
- Use `PreviewProvider` (or `#Preview` macro) for all views.
- Constants and magic numbers belong in a `Constants.swift` or scoped `enum`.

### File Organization

- One type per file; file name matches type name.
- Group files by feature, not by type (Feature-first architecture).
- Assets: use semantic names (`color.accent`, `image.product.banhoney`).

### Accessibility

- All interactive elements must have `.accessibilityLabel` set.
- Support Dynamic Type by using `.font(.title)` style tokens, not fixed sizes.
- Minimum tap target: 44×44pt.

---

## Key UI Screens

### Weekend Promotion Screen
- Full-bleed arched gradient background (peach → light pink)
- Header: "Only This" (regular) + "Weekend" (script/italic)
- Product carousel showing 2 items side-by-side; active item is larger
- Product label below image in accent color
- Price pill at bottom: `$12.00 EACH` with `BUY 1 GET 1 FREE` subtitle
- Decorative diamond icons (`♦`) flanking the price pill

### Product Card Component
- Accepts `Product` model (name, image, price)
- Supports active/inactive scale states for carousel effect
- Image renders with soft shadow and slight overflow above card bounds

---

## Data Models (Expected)

```swift
struct Product: Identifiable, Codable {
    let id: UUID
    let name: String
    let imageName: String   // Asset catalog key
    let price: Decimal
    let category: Category
}

struct Promotion: Identifiable, Codable {
    let id: UUID
    let title: String
    let subtitle: String
    let validFrom: Date
    let validUntil: Date
    let deal: DealType      // e.g., .bogoFree, .percentOff(20)
    let products: [Product]
}
```

---

## Testing Guidelines

- **Unit tests**: Cover ViewModels, models, and business logic.
- **UI tests**: Cover critical user flows (view promotion, add to cart).
- Aim for ≥ 70% coverage on non-UI code.
- Use `XCTestExpectation` for async flows.
- Mock network/data layers with protocols.

---

## Common Pitfalls to Avoid

1. **Do not hardcode colors inline** — always use `Color("accent")` from the asset catalog or a design token enum.
2. **Avoid force-unwrapping** (`!`) — use `guard let` or `if let`.
3. **Do not mix business logic into View bodies** — keep views declarative.
4. **Do not commit API keys or secrets** — use `.xcconfig` + `.gitignore`.
5. **Do not skip previews** — every view should have a working `#Preview`.

---

## AI Assistant Instructions

When working in this repository:

1. **Read existing files before editing** — understand patterns already in use.
2. **Match the established SwiftUI architecture** — feature-grouped folders, thin views, ViewModels for logic.
3. **Follow the visual design language** described above when generating new views.
4. **Write tests** for any new business logic added.
5. **Update this CLAUDE.md** if you discover new conventions, add dependencies, or significantly restructure the project.
6. **Use the `claude/` branch naming convention** for all AI-driven changes.
7. **Do not push to `main` directly** — always go through a PR/review.

---

## Updating This File

This document should be kept current. Update it when:
- New dependencies are added
- Architecture decisions are made
- Folder structure changes
- New screens or features are added
- CI/CD is configured
- Deployment targets change

Last updated: 2026-03-13
