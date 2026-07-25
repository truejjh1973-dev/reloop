# ReLoop Optimized Branch Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Produce an independent Git branch that selectively integrates the useful design-system, accessibility, and responsive ideas from `reloop-optimized.css` into the existing ReLoop homepage.

**Architecture:** Keep `index.html` and `shared.css` as the production entry points. Add semantic and form-accessibility markup in HTML, then extend the existing `.eco` design with scoped tokens and component refinements so the generic reference stylesheet never overrides the established brand.

**Tech Stack:** Static HTML5, CSS3, native browser video, GitHub Pages.

---

### Task 1: Record the approved design

**Files:**
- Create: `docs/plans/2026-07-24-reloop-optimized-design.md`
- Create: `docs/plans/2026-07-24-reloop-optimized-implementation.md`

**Step 1:** Document why selective integration is safer than replacing `shared.css`.

**Step 2:** Record visual, accessibility, responsive, and verification criteria.

**Step 3:** Confirm both documents are present with `git status --short`.

### Task 2: Improve semantic navigation and form markup

**Files:**
- Modify: `index.html`

**Step 1:** Add a skip link before the navigation and add `id="main-content"` plus `tabindex="-1"` to the main landmark.

**Step 2:** Add accessible names, `required`, autocomplete, numeric input constraints, and helper text to the quote form without introducing backend submission.

**Step 3:** Bump the stylesheet query version to prevent stale GitHub Pages caching.

**Step 4:** Parse the HTML with Python’s standard `html.parser`; expect no parser exception.

### Task 3: Integrate the reference design-system ideas

**Files:**
- Modify: `shared.css`
- Reference: `reloop-optimized.css`

**Step 1:** Add scoped spacing, radius, shadow, transition, and navigation-height tokens to `.eco`.

**Step 2:** Add the skip-link, anchor offset, antialiasing, and stronger reduced-motion rules.

**Step 3:** Refine navigation, buttons, video frame, cycle cards, customer cards, device passport, and form controls using existing ReLoop colors and typography.

**Step 4:** Preserve the approved section spacing, three-customer illustrations, and limited motion vocabulary.

**Step 5:** Run `git diff --check`; expect no whitespace errors.

### Task 4: Verify responsive behavior

**Files:**
- Verify: `index.html`
- Verify: `shared.css`
- Verify: `media/reloop-intro-30s.mp4`

**Step 1:** Inspect at 1440×1000 and confirm two-column hero, row video heading, three customer cards, and visible focus states.

**Step 2:** Inspect at 412×915 and confirm mobile menu, single-column content, full-width video, and 48-pixel interactive targets.

**Step 3:** Confirm video metadata reports 30 seconds, 1280×720, and no media error.

**Step 4:** Confirm browser console contains no errors.

### Task 5: Commit the branch version

**Files:**
- Stage only the design documents, `index.html`, `shared.css`, and the supplied `reloop-optimized.css` reference.

**Step 1:** Review `git diff --stat` and `git status --short`.

**Step 2:** Commit with `git commit -m "Optimize ReLoop design system and accessibility"`.

**Step 3:** Push with `git push -u origin codex/reloop-optimized`.

**Step 4:** Report the branch name, commit, verification results, and how to preview without changing `main`.
