---
name: 21st-dev
description: Search and import UI components from 21st.dev into HyperFrames compositions. Use when the user says "find a component from 21st.dev", "use a 21st.dev component", "add a UI element from the registry", or wants to pull pre-built animated components into a video composition.
---

# 21st.dev — Design Component Registry

[21st.dev](https://21st.dev) is an AI Agent Registry and UI component marketplace. It offers pre-built animated components, AI prompt interfaces, chat UIs, and motion patterns that can be adapted for HyperFrames compositions.

## What 21st.dev offers

- Animated UI components (prompt boxes, cards, loaders, transitions)
- Agent interaction patterns
- Motion-graphic building blocks
- Community-built design templates

## How to use in Framesmith

### Step 1: Search the registry

Point the user to: `https://21st.dev/home`

Ask the user what kind of component they need:
- Animation type (entrance, loop, transition)
- Visual style (minimal, glassmorphism, editorial, dark UI)
- Purpose (title card, data visualization, CTA, caption style)

### Step 2: Fetch and inspect the component

When the user provides a 21st.dev component URL, fetch it to read the HTML/CSS/JS source:

```
WebFetch the component URL and extract:
- HTML structure
- CSS (especially keyframes, transforms, transitions)
- JavaScript (animation logic)
```

### Step 3: Adapt for HyperFrames

Convert the component to HyperFrames-compatible HTML:

1. **Remove React/JSX** — HyperFrames uses plain HTML, not React
2. **Convert CSS animations to GSAP** — replace `@keyframes` with GSAP timelines for deterministic rendering
3. **Add HyperFrames timing attributes:**
   ```html
   <div class="clip" data-start="0" data-duration="3" data-track-index="1">
     <!-- component content here -->
   </div>
   ```
4. **Replace component colors with brand tokens:**
   ```css
   /* Replace generic colors with Hihnala tokens */
   background: var(--hihnala-surface);
   color: var(--hihnala-text);
   border-color: var(--hihnala-border-quiet);
   ```
5. **Register the GSAP timeline:**
   ```js
   window.__timelines = window.__timelines || {};
   window.__timelines["component-id"] = gsap.timeline({ paused: true });
   ```

### Step 4: Validate

After adapting:
1. Run `npx hyperframes lint` — fix any errors
2. Preview in Studio (`npx hyperframes preview`)
3. Verify the component renders correctly frame-by-frame

## Brand adaptation rules

All 21st.dev components must be adapted to the Hihnala brand before use:
- Replace any generic font with Source Serif 4 (headings) or Plus Jakarta Sans (body)
- Replace generic backgrounds with `--hihnala-bg` or `--hihnala-surface`
- Replace primary accent colors with `--hihnala-ember`
- Apply the double-bezel card technique to any elevated container
- No `Math.random()` or `Date.now()` — replace with seeded or static values

## Limitations

- Components with Canvas/WebGL may not render correctly in headless Chrome — test carefully
- React/Vue/Svelte components must be rewritten as plain HTML+CSS+GSAP
- Very complex animations may need to be simplified for deterministic rendering
- Always test at draft quality first before final render

## Useful 21st.dev URLs

- Registry home: `https://21st.dev/home`
- Agent docs: `https://21st.dev/agents/docs`
- Search: use the search on the website — no public API currently available
