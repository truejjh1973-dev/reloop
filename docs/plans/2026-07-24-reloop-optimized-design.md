# ReLoop Selective CSS Optimization Design

## Purpose

Create an improved branch version of the ReLoop homepage using `reloop-optimized.css` as a reference design system while preserving the current Style 2 identity. The audience remains SHAD Grade 10 reviewers, schools, nonprofits, and small businesses. The page should feel credible, modern, environmentally responsible, and achievable as a student venture.

## Chosen approach

Use selective integration rather than replacing `shared.css`. The reference stylesheet is a broad 1,392-line system whose global reset, Inter font stack, generic emerald palette, and component selectors do not map directly to the current HTML. A full replacement would flatten the existing serif/sans-serif title pairing, alter the ReLoop palette, and incorrectly apply `aspect-ratio` and grid rules to whole sections.

The optimized branch keeps the existing teal, mint, cream, and yellow palette and the current Trebuchet/Georgia pairing. It imports the useful structural ideas: an explicit token layer for spacing, radii, shadows, and transitions; 48-pixel touch targets; stronger interactive states; reduced-motion support; a skip link; predictable sticky-navigation offsets; and more legible form states.

## Visual system

The memorable element remains the circular laptop orbit. Refinement is concentrated around it rather than adding another visual motif. Navigation gains a controlled glass surface and subtle elevation. Buttons use consistent motion, shadows, and pressed states. Customer cards receive restrained borders, focus-within states, and a smaller lift. The device passport keeps its handmade rotated-card character but gains a cleaner shadow and border. The video retains its single-focus presentation.

Section spacing stays within the previously approved 82–108 pixel range. Body colors remain dark enough for comfortable reading. Mobile layouts remain single-column where appropriate, with a full menu and 48-pixel interactive targets.

## Accessibility and behavior

Add a keyboard-visible “Skip to main content” link and a focusable main landmark. Add `scroll-margin-top` so anchored sections are not hidden by the sticky navigation. Extend reduced-motion behavior to transitions and smooth scrolling. Keep strong yellow focus rings against teal surfaces.

Form controls receive names, autocomplete hints, required states, better hover/focus/invalid styling, and short helper text. The form remains demonstrational: no network submission or new backend behavior is introduced.

## Verification

Validate HTML structure, CSS syntax/whitespace, media references, and Git diff scope. Verify the optimized branch in a real browser at desktop and mobile breakpoints. Confirm the video metadata loads as 30 seconds at 1280×720, the menu remains usable, anchor offsets work, keyboard focus is visible, and the browser console has no errors.
