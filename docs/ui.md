# UI Component Standards

## Overview
This document establishes coding standards for the Calendar Dashboard UI components.

## Critical Rule
**ABSOLUTELY NO custom components should be created, only use shadcn ui components.**

All UI elements must be built exclusively using shadcn UI library. Custom component creation is strictly prohibited to maintain consistency, reduce maintenance burden, and leverage well-tested, accessible components.

## Component Guidelines

### Permitted Components
- All components from the shadcn UI library are permitted
- Standard HTML elements with minimal styling for layout purposes

### Prohibited
- Custom React components for UI elements
- Custom CSS-only components
- Non-shadcn third-party UI libraries (except for utility libraries like date-fns)

## Styling Standards
- Use shadcn UI's built-in theming system
- Leverage CSS variables for consistency
- Minimize custom CSS - prefer using shadcn's component variants

## Date Formatting
All dates must be formatted using date-fns library with ordinal format:
- Format: "1st Sept 2026", "2nd Jan 2025", "23rd Dec 2024"
- Use date-fns utilities with custom ordinal suffix logic

## Dashboard Layout
The calendar dashboard uses shadcn UI components exclusively:
- Date picker for selecting dates
- Card components for session display
- Badge components for session type indicators
- All UI interactions handled through shadcn UI components

## Implementation Notes
- All templates must reference the shadcn UI CDN
- No custom component files should be created
- Maintain semantic HTML structure
- Ensure accessibility standards are met through shadcn UI's built-in features
